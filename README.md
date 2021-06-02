POLARIS API CLIENT
===================

The following steps walk through how to install and test the POLARIS api:

**1. Clone the polaris_api_client repository.**

```
git clone https://github.com/chaneyn/polaris_api_client.git
cd polaris_api_client
```

**2. Create a conda environment named polaris_api_client from the yml file. The current yml files are for osx64 and linux64 machines.** 

```
linux64 -> conda env create -f yml/polaris_api_client_linux64.yml
osx64 -> conda env create -f yml/polaris_api_client_osx64.yml
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

**POLARIS soil properties general information** 

#Variable - Description,Units
silt - silt percentage, %
sand - sand percentage, %
clay - clay percentage, %
bd - bulk density, g/cm3
theta_s - saturated soil water content, m3/m3
theta_r - residual soil water content, m3/m3
ksat - saturated hydraulic conductivity, log10(cm/hr)
ph - soil pH in H2O, N/A
om - organic matter, log10(%)
lambda - pore size distribution index (brooks-corey), N/A
hb - bubbling pressure (brooks-corey), log10(kPa)
n - measure of the pore size distribution (van genuchten), N/A
alpha - scale parameter inversely proportional to mean pore diameter (van genuchten), log10(kPa-1)

#Depth from surface
1. 0-5 cm
2. 5-15 cm
3. 15-30 cm
4. 30-60 cm
5. 60-100 cm
6. 100-200 cm

#Statistics provided per layer and variable:
1. mean - Arithmetic mean
1. mode - Mode
1. p50 - Median
1. p5 - 5th percentile
1. p95 - 95th percentile

#Resolutions
1. 1 arcsec (~30 meters)

#Notes
*05/01/2019 - The variables hb, alpha, ksat, om are in log10 space. 
*05/01/2019 - Due to file size constraints, the 1 arcsec database is split into 1x1 degree tiffs. Each variable/layer/statistic has its own virtual raster that acts as the "glue" of all the smaller 1x1 degree chunks. For more information on virtual rasters see https://www.gdal.org/gdal_vrttut.html. 
*06/02/2019 - The variables hb and alpha were originally reported to have the units of log10(cm) and log10(cm-1) respectively. This was a typo. The correct units are log10(kPa) and log10(kPa-1) respectively. 
