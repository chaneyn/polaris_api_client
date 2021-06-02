POLARIS API CLIENT
===================

The following steps walk through how to install HydroBlocks and run it over the SGP site in Oklahoma

**1. Clone the polaris_api_client repository.**

```
git clone https://github.com/chaneyn/polaris_api_client.git
cd polaris_api_client
```

**2. Create a conda environment named polaris_api_client from the yml file. Note that the only current yml file in the repository is for a linux64 machine.** 

```
conda env create -f yml/polaris_api_client_linux64.yml
source activate polaris_api_client
```

**3. Install the package.**

```
python setup.py install
cd ..
```

**4. Test the example.**

```
python polaris_api_example.py
```
