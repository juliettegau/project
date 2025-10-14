import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#%% Load data

file_path = r"C:\Users\jujug\Documents\Ecole\4. NTNU\PYTHON\dataset\NOx_database.csv"
data = pd.read_csv(
    file_path,
    sep="\t",
    encoding="utf-8-sig",
    engine="python",      
    dtype=str,            
)

#%% Reshape data
data_nox = data.copy()

# Filter only NOx pollutant
data_nox = data_nox[data_nox["pollutantName"] == "NOx"]

# Remove NaN values
mask_NaN = data_nox["value"].isna()
data_nox = data_nox[~mask_NaN]
print(data_nox.shape)

# Drop columns that are not needed
columns_to_drop = ['countryCode', 'notation','sectorCode','formatName','parentSectorCode','notation']
data_nox = data_nox.drop(columns=columns_to_drop)
print(data_nox.head(), data_nox.info())

data_nox.to_csv(r"C:\Users\jujug\Documents\Ecole\4. NTNU\PYTHON\project\clean_dataset\cleaned_NOx_database.csv", index=False)