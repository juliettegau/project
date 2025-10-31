#%%
"""sector_plot.py"""
#This file create a plot for the repartition of emissions by sector for a select year and pollutant
# Author: julietlg@stud.ntnu.no
# Date: 31.10.2025
# changing the code making a plott for emissions per sector and changing the font
# Author: dominiwm@stud.ntnu.no
# Date: 22.10.2025

#%% importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import os


#%% Importing datasets
df_pol = pd.read_csv(r"../../clean_dataset/pollutant_data.csv")
df_sectors = pd.read_excel(r"sectors_list.xlsx")

#%% Create a dictionnaire
dict_sectors = dict(zip(df_sectors["sectorName"], df_sectors["supersectorName"]))

#%% Create new column
df_pol["supersectorName"] = df_pol["sectorName"].map(dict_sectors)

##### PIE CHART ######

#%% Select a country 
country_select = "Sweden" 
year_select = 2000
pollutant_select = "SOx"
df_pie = df_pol[
    (df_pol["country"] == country_select) &
    (df_pol["year"] == year_select) &
    (df_pol["pollutantName"] == pollutant_select)
]

#%%
#Dropping national blabla
df_pie = df_pie[df_pie["sectorName"] != "NATIONAL TOTAL FOR COMPLIANCE"]

# Create a pie chart 
data_per_supersectors = df_pie.groupby("supersectorName")["value"].sum()
total_emissions = round(df_pie["value"].sum())
labels_supersectors = data_per_supersectors.index

plt.figure(figsize=(8, 8))
plt.pie(data_per_supersectors, labels=labels_supersectors, autopct='%1.1f%%', startangle=90, textprops={'fontfamily': 'Segoe UI', 'fontsize': 12})
plt.title(f"Emissions of {pollutant_select} by supersectors in {year_select} in {country_select} -- Total = {total_emissions} kt", fontsize=18, fontfamily="Segoe UI")
plt.savefig(f"pie-{pollutant_select}-{country_select}-{year_select}.png")
plt.show()


##### BY TIME ######s
#%%
# Sorting data
df_time = df_pol[
    (df_pol["country"] == country_select) &
    (df_pol["pollutantName"] == pollutant_select)
]
df_time = df_time[df_time["sectorName"] != "NATIONAL TOTAL FOR COMPLIANCE"]

# Group by
data_per_supersectors_time = (
    df_time.groupby(["supersectorName", "year"])["value"]
    .sum()
    .reset_index()
)

# Plot
plt.figure(figsize=(10, 6))

# One line per sector
for supersector, data in data_per_supersectors_time.groupby("supersectorName"):
    plt.plot(
        data["year"],
        data["value"],
        marker="o",
        linewidth=2,
        label=supersector
    )

plt.title(f"Evolution of {pollutant_select} emissions by supersector in {country_select}", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel(f"{pollutant_select} (kt)", fontsize=14)
plt.grid(True)
plt.legend(title="Supersectors", fontsize=10)
plt.tight_layout()

plt.savefig(f"time-{pollutant_select}-{country_select}.png", dpi=300)
plt.show()

# %%
