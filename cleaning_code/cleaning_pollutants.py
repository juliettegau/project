#%%
"""Cleaned_Data_Set_GDP_and_Population.py"""
#This file is for cleaning the database of NOx and SOx
# Author: emmasjo@stud.ntnu.no
# Date: 16.10.2025

#%%
import pandas as pd
import matplotlib.pyplot as plt

#%% Importing the file
path =  r"/Users/emmasjostrom/Desktop/TEP4221/NEC_NFR19_2025_25.05.26.csv"

df = pd.read_csv(path, sep="\t")   
#test
#%% Sorting out the relevant countries

df_se = df[(df["countryCode"] == "SE") | (df["country"] == "Sweden")]
df_de= df[(df["countryCode"] == "DE") | (df["country"] == "Germany")]
df_gr= df[(df["countryCode"] == "GR") | (df["country"] == "Greece")]

#%% Filter for SOx only
df_se_sox_nox = df_se[df_se["pollutantName"].str.strip().str.upper().isin(["SOX", "NOX"])]
df_de_sox_nox = df_de[df_de["pollutantName"].str.strip().str.upper().isin(["SOX", "NOX"])]
df_gr_sox_nox = df_gr[df_gr["pollutantName"].str.strip().str.upper().isin(["SOX", "NOX"])]

#%% sorting out the relevant columns and merging the dataframes
cols = [ "country", "sectorName", "year", "pollutantName","value", "unit"]
df_sox_all = (
    pd.concat([df_se_sox_nox, df_de_sox_nox, df_gr_sox_nox], ignore_index=True)
      .loc[:, cols]
      .dropna(subset=["value"])  
      .sort_values(["country", "year", "sectorName"])
)

#storing data in a csv file
df_sox_all.to_csv(r"/Users/emmasjostrom/Desktop/project/clean_dataset/pollutant_data.csv", index=False, encoding="utf-8")


#%% add the path 





#%%



#%%




