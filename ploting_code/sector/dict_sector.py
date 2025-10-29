#%%
"""dict_sector.py"""
#This file creating a dictionnaire that link the scetor to bigger sector to understand the economy
# Author: julietlg@stud.ntnu.no
# Date: 16.10.2025
# changing the code making a plott for emissions per sector
# Author: dominiwm@stud.ntnu.no
# Date: 22.10.2025

#%% importing library
import pandas as pd
import matplotlib.pyplot as plt

#%% Importing datasets
df_pol = pd.read_csv("../clean_dataset/pollutant_data.csv")
df_sectors = pd.read_excel("../ploting_code/sector/sectors_list.xlsx")

#%% Create a dictionnaire
dict_sectors = dict(zip(df_sectors["sectorName"], df_sectors["supersectorName"]))

#%% Create new column
df_pol["supersectorName"] = df_pol["sectorName"].map(dict_sectors)

#%% Create a pie chart
data_per_supersectors = df_pol["supersectorName"].value_counts()
labels_supersectors = df_pol["supersectorName"].unique()
data_per_sectors = df_pol["sectorName"].value_counts()
labels_sectors = df_pol["sectorName"].unique()

# Pie chart for super sectors
plt.figure(figsize=(8, 8))
plt.pie(data_per_supersectors, labels=labels_supersectors, autopct='%1.1f%%', startangle=90, textprops={'fontfamily': 'Segoe UI', 'fontsize': 12})
plt.title("Amount of data by super sector", fontsize=18, fontfamily="Segoe UI")
plt.savefig("../ploting_code/Plots/Pie_SuperSectors.png", dpi=300)
plt.show()

# Pie chart for sectors
plt.figure(figsize=(8, 8))
plt.pie(data_per_sectors, labels=labels_sectors, autopct='%1.1f%%', startangle=90, textprops={'fontfamily': 'Segoe UI', 'fontsize': 12})
plt.title("Amount of data by sector", fontsize=18, fontfamily="Segoe UI")
plt.savefig("../ploting_code/Plots/Pie_Sectors.png", dpi=300)
plt.show()

#%% Absolute emissions per sector
emissions_per_sector = df_pol.groupby("sectorName")["value"].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(emissions_per_sector.index, emissions_per_sector.values, color='tab:blue')
plt.xticks(rotation=90)
plt.xlabel("Sector", fontsize=14, fontfamily="Segoe UI")
plt.ylabel("Total Emissions (kt)", fontsize=14, fontfamily="Segoe UI")
plt.title("Total Emissions by Sector", fontsize=16, fontfamily="Segoe UI")
plt.tight_layout()
plt.savefig("../ploting_code/Plots/Total_Emissions_by_Sector.png", dpi=300)
plt.show()

# %%
