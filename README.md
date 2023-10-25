# Data from National Aeronautics and Space Administration (NASA)

### This repo contains data files from 

## NASA's Goddard Institute for Space Studies (GISS)

NASA requests the following:  "When referencing the GISTEMP v4 data, please cite both this website as well our most recent scholarly publication about the analysis. In citing the website, be sure to include the date of access".

And I am very happy to do that:

- GISTEMP Team, 2023: GISS Surface Temperature Analysis (GISTEMP), version 4. NASA Goddard Institute for Space Studies. Dataset accessed 20YY-09-19 at data.giss.nasa.gov/gistemp/.

- Lenssen, N., G. Schmidt, J. Hansen, M. Menne, A. Persin, R. Ruedy, and D. Zyss, 2019: Improvements in the GISTEMP uncertainty model. J. Geophys. Res. Atmos., 124, no. 12, 6307-6326, doi:10.1029/2018JD029522.

---

### The files in this folder include the following:

#### Data

Tables of Global and Hemispheric Monthly Means and Zonal Annual Means
Combined Land-Surface Air and Sea-Surface Water Temperature Anomalies (Land-Ocean Temperature Index, L-OTI)
The following are plain-text files in tabular format of temperature anomalies, i.e. deviations from the corresponding 1951-1980 means.

- Global-mean monthly, seasonal, and annual means, 1880-present, updated through most recent month: CSV

- Northern Hemisphere-mean monthly, seasonal, and annual means, 1880-present, updated through most recent month: CSV

- Southern Hemisphere-mean monthly, seasonal, and annual means, 1880-present, updated through most recent month: CSV

- Zonal annual means, 1880-present, updated through most complete year: CSV

#### Programs

The following programs support the article [2023 was the Hottest Summer Ever](#)

- `giss.ipynb` is a Jupyter Note book that draws various charts concerning the 2023 record summer tempertures and how they are related to CO2 emissions.

 - `readdata.py` is a simple helper library for reading the GISS files


