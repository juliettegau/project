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
df_merged = pd.merge(df_GDP,df_pollutant,left_on=["Country Name", "Year"],right_on=["country", "year"],how="inner")
print(df_merged.head())
#%%
#remove rows with sector 'NATIONAL TOTAL FOR COMPLIANCE'
df_merged_clean = df_merged[df_merged['sectorName'] != 'NATIONAL TOTAL FOR COMPLIANCE']
print(df_merged_clean)
# %%
# save merged dataset
df_merged_clean.to_csv("merged_dataset.csv", index=False)
# %%
# group all values with the same year and sum the values of the pollutants
df_merged_grouped_year = df_merged_clean.groupby(['country', 'year', 'pollutantName'], as_index=False)['value'].sum()
print(df_merged_grouped_year)

# %% 
# Merge grouped dataset with merged dataset to get GDP and population values
df_merged_grouped_year = pd.merge(df_merged_grouped_year, df_GDP, left_on=["country", "year"], right_on=["Country Name", "Year"], how="left")
print(df_merged_grouped_year)

# %%
# save merged and grouped dataset
df_merged_grouped_year.to_csv("merged_grouped_dataset.csv", index=False)
# %%
