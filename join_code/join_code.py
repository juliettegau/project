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
df_GDP = pd.read_csv(r"clean_dataset\cleaned gdp_population_gdp per capita dataset.csv")
df_pollutant = pd.read_csv(r"clean_dataset\pollutant_data.csv")
# %%
#check if it worked
df_GDP
df_pollutant
# %%
#merge datasets
df_merged = pd.merge(df_GDP,df_pollutant,left_on=["Country Name", "Year"],right_on=["country", "year"],how="inner")
print(df_merged.head())
# %%
# save merged dataset
df_merged.to_csv("merged_dataset.csv", index=False)
# %%
