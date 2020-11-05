[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
<!-- [![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.1-blue.svg)](https://doi.org/10.25663/brainlife.app.435) -->

# Network Results Template
Brainlife App template for network neuroscience. This is a sample App that loads a network and export the degree distribution as pdf. Fork or copy this repository and change `main.py` with your code.

### Authors
- [Filipi N. Silva](https://filipinascimento.github.io)

### Contributors
- [Franco Pestilli](https://liberalarts.utexas.edu/psychology/faculty/fp4834)

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations
1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

2. Bassett, Danielle S., and Olaf Sporns. "Network neuroscience." Nature neuroscience 20, no. 3 (2017): 353. [https://doi.org/10.1038/nn.4502](https://doi.org/10.1038/nn.4502)

<!-- 3. Costa, L. da F., Francisco A. Rodrigues, Gonzalo Travieso, and Paulino Ribeiro Villas Boas. "Characterization of complex networks: A survey of measurements." Advances in physics 56, no. 1 (2007): 167-242.[https://doi.org/10.1080/00018730601170527](https://doi.org/10.1080/00018730601170527) -->

## Running the App 

<!-- ### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/brainlife.app.435](https://doi.org/10.25663/brainlife.app.435) via the "Execute" tab. -->

### Running Locally (on your machine)
Singularity is required to run the package locally.

1. git clone this repo.

```bash
git clone <repository URL>
cd <repository PATH>
```

2. Inside the cloned directory, edit `config-sample.json` with your data or use the provided data.

3. Rename `config-sample.json` to `config.json` .

```bash
mv config-sample.json config.json
```

4. Launch the App by executing `main`

```bash
./main
```

### Sample Datasets

A sample dataset is provided in folder `data` and `config-sample.json`

## Output

The output is a HTML report with figures in PDF and PNG.

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install the python packages defined in `environment.yml`, then you can run the code directly from python using:  

```bash
./main.py config.json
```

