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

## POLARIS soil properties general information** 

*Spatial resolution*
1 arcsec (~30 meters)
 
Variable id - Description, Units
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

#Layers - Depth from surface
1. 0_5 - 0-5 cm
2. 5_15 - 5-15 cm
3. 15_30 - 15-30 cm
4. 30_60 - 30-60 cm
5. 60_100 - 60-100 cm
6. 100_100 - 100-200 cm

#Other information
*The variables hb, alpha, ksat, om are in log10 space.  
*The units of hb and alpha are log10(kPa) and log10(kPa-1) respectively. 

#Citation
Chaney, N.W., Minasny, B., Herman, J.D., Nauman, T.W., Brungard, C.W., Morgan, C.L., McBratney, A.B., Wood, E.F. and Yimam, Y., 2019. POLARIS soil properties: 30‐m probabilistic maps of soil properties over the contiguous United States. Water Resources Research, 55(4), pp.2916-2938.

#License
POLARIS is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.
