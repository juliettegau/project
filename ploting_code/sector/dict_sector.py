#%%
"""dict_sector.py"""
#This file creating a dictionnaire that link the scetor to bigger sector to understand the economy
# Author: julietlg@stud.ntnu.no
# Date: 16.10.2025
# changing the code making a plott for emissions per sector and changing the font
# Author: dominiwm@stud.ntnu.no
# Date: 22.10.2025

#%% importing libraries
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
labels_supersectors = data_per_supersectors.index
data_per_sectors = df_pol["sectorName"].value_counts()
labels_sectors = data_per_sectors.index  

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

#%% Absolute emissions per supersector
emissions_per_supersector = df_pol.groupby("supersectorName")["value"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 6))
bars = plt.bar(emissions_per_supersector.index, emissions_per_supersector.values, color=['tab:blue', 'tab:orange', 'tab:green', 'tab:red'])

plt.xlabel("Supersector", fontsize=14, fontfamily="Segoe UI")
plt.ylabel("Total Emissions (kt)", fontsize=14, fontfamily="Segoe UI")
plt.title("Total Emissions by Supersector", fontsize=18, fontfamily="Segoe UI")

plt.text(0, bars[0].get_height(), f'{bars[0].get_height():,.0f}', ha='center', va='bottom', fontfamily="Segoe UI", fontsize=12)
plt.text(1, bars[1].get_height(), f'{bars[1].get_height():,.0f}', ha='center', va='bottom', fontfamily="Segoe UI", fontsize=12)
plt.text(2, bars[2].get_height(), f'{bars[2].get_height():,.0f}', ha='center', va='bottom', fontfamily="Segoe UI", fontsize=12)
plt.text(3, bars[3].get_height(), f'{bars[3].get_height():,.0f}', ha='center', va='bottom', fontfamily="Segoe UI", fontsize=12)

plt.tight_layout()
plt.savefig("../ploting_code/Plots/Total_Emissions_by_Supersector.png", dpi=300)
plt.show()

# %%
