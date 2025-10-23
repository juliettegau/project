#%%
"""dict_sector.py"""
#This file creating a dictionnaire that link the scetor to bigger sector to understand the economy
# Author: julietlg@stud.ntnu.no
# Date: 16.10.2025

#%% importing the libraries
import pandas as pd
import matplotlib.pyplot as plt


#%% Downloading the file
df_pol = pd.read_csv("clean_dataset/pollutant_data.csv")
df_sectors = pd.read_excel("sectors_list.xlsx")


#%% Create a dictionnaire
dict_sectors = dict(zip(df_sectors["sectorName"], df_sectors["supersectorName"]))

#%% Create new column
df_pol["supersectorName"] = df_pol["sectorName"].map(dict_sectors)


#%% Create a pie chart
data_per_supersectors = df_pol["supersectorName"].value_counts()
labels_supersectors = df_pol["supersectorName"].unique()
data_per_sectors = df_pol["sectorName"].value_counts()
labels_sectors = df_pol["sectorName"].unique()

# Pie chart for super sect
plt.figure(figsize=(8, 8))
plt.pie(data_per_supersectors, labels=labels_supersectors, autopct='%1.1f%%', startangle=90)
plt.title("Amount of data by super sector")
plt.show()

# Pie chart for sect
plt.figure(figsize=(8, 8))
plt.pie(data_per_sectors, labels=labels_sectors, autopct='%1.1f%%', startangle=90)
plt.title("Amount of data by sector")
plt.show()
# %%
