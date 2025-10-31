#%%
"join_code.py"
#This file is for merging the cleaned datasets
# Author: dominiwm@stud.ntnu.no
# Date: 16.10.2025
# %%
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# %%
# import files
df_GDP = pd.read_csv("../clean_dataset/cleaned gdp_population_gdp per capita dataset.csv")
df_pollutant = pd.read_csv("../clean_dataset/pollutant_data.csv")
# %%
#check if it worked
df_GDP
df_pollutant
# %%
#merge datasets
df_merged = pd.merge(df_GDP,df_pollutant, left_on=["Country Name", "Year"],right_on=["country", "year"], how="inner")
df_merged
#%%
#remove rows with sector 'NATIONAL TOTAL FOR COMPLIANCE'
df_merged_clean = df_merged[df_merged['sectorName'] != 'NATIONAL TOTAL FOR COMPLIANCE']
df_merged_clean
#%% drop duplicate columns
df_merged_clean = df_merged_clean.drop(columns=['Country Name', 'Year'])
df_merged_clean
# %%
# save merged dataset
df_merged_clean.to_csv("merged_dataset.csv", index=False)

# %%
# NOx and SOx into separate columns
df_merged_clean_seperate_NOx_SOx = df_merged_clean.pivot(index=["country", "year", "sectorName", "Population", "GDP_USD", "gdp_per_capita"], columns="pollutantName", values="value").reset_index()
df_merged_clean_seperate_NOx_SOx

# %%
# save merged and seperated dataset
df_merged_clean_seperate_NOx_SOx.to_csv("merged_dataset.csv", index=False)
# %%
# group all values with the same year and sum the values of the pollutants
df_merged_grouped_year = df_merged_clean.groupby(['country', 'year', 'pollutantName'], as_index=False)['value'].sum()
df_merged_grouped_year

# %% 
# Merge grouped dataset with merged dataset to get GDP and population values
df_merged_grouped_year = pd.merge(df_merged_grouped_year, df_GDP, left_on=["country", "year"], right_on=["Country Name", "Year"], how="left")
df_merged_grouped_year

#%% drop duplicate columns
df_merged_grouped_year = df_merged_grouped_year.drop(columns=['Country Name', 'Year'])
df_merged_grouped_year

# %%
# save merged and grouped dataset
df_merged_grouped_year.to_csv("merged_grouped_dataset.csv", index=False)
# %%
# NOx and SOx into separate columns
df_merged_seperate_NOx_SOx = df_merged_grouped_year.pivot(index=["country", "year", "Population", "GDP_USD", "gdp_per_capita"], columns="pollutantName", values="value").reset_index()
df_merged_seperate_NOx_SOx
# %%
# save merged, grouped and seperated dataset
df_merged_seperate_NOx_SOx.to_csv("merged_grouped_seperate_NOx_SOx.csv", index=False)

# %%
