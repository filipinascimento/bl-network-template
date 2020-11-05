#!/usr/bin/env python

import sys
import os.path
from os.path import join as PJ
import re
import json
import numpy as np
from tqdm import tqdm
import igraph as ig
import jgf
import pandas as pd

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numbers

# Auxiliary functions
def isFloat(value):
	if(value is None):
		return False
	try:
		numericValue = float(value)
		return np.isfinite(numericValue)
	except ValueError:
		return False


def isNumberObject(value):
	return isinstance(value, numbers.Number)

class NumpyEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
			np.int16, np.int32, np.int64, np.uint8,
			np.uint16, np.uint32, np.uint64)):
			ret = int(obj)
		elif isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
			ret = float(obj)
		elif isinstance(obj, (np.ndarray,)): 
			ret = obj.tolist()
		else:
			ret = json.JSONEncoder.default(self, obj)

		if isinstance(ret, (float)):
			if math.isnan(ret):
				ret = None

		if isinstance(ret, (bytes, bytearray)):
			ret = ret.decode("utf-8")

		return ret


# Functions to deal with product.json
results = {"errors": [], "warnings": [], "brainlife": [], "datatype_tags": [], "tags": []}

def warning(msg):
	global results
	results['warnings'].append(msg) 
	#results['brainlife'].append({"type": "warning", "msg": msg}) 
	print(msg)

def error(msg):
	global results
	results['errors'].append(msg) 
	#results['brainlife'].append({"type": "error", "msg": msg}) 
	print(msg)

def exitApp():
	global results
	with open("product.json", "w") as fp:
		json.dump(results, fp, cls=NumpyEncoder)
	if len(results["errors"]) > 0:
		sys.exit(1)
	else:
		sys.exit()

def exitAppWithError(msg):
	global results
	results['errors'].append(msg) 
	#results['brainlife'].append({"type": "error", "msg": msg}) 
	print(msg)
	exitApp()


# Choosing config file
configFilename = "config.json"
argCount = len(sys.argv)
if(argCount > 1):
		configFilename = sys.argv[1]

# Defining paths
outputDirectory = "output"

if(not os.path.exists(outputDirectory)):
		os.makedirs(outputDirectory)

# Reading config file
with open(configFilename, "r") as fd:
		config = json.load(fd)

# Loading the network using igraph
networks = jgf.igraph.load(config["network"], compressed=True)

# Warn that only one network will be considered if multiple networks exist in the same file.
if(len(networks)>1):
	warning("Input files have more than one network. Only the first entry was used to compose the report.")
	
if(len(networks)==0):
	exitAppWithError("The network file should contain at least one network.")
else:
	network = networks[0]

# Calculating and plotting degree distribution to report.pdf
degrees = network.degree()
fig = plt.figure(figsize= (6,3.0))
ax = plt.axes()
ax.hist(degrees,density=True)
ax.set_xlabel("Degree")
ax.set_ylabel("Density")
plt.tight_layout()
fig.savefig(PJ(outputDirectory,"report.pdf"))
plt.close(fig)

exitApp()