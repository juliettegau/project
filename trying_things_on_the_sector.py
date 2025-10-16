#%%
"""Cleaned_Data_Set_GDP_and_Population.py"""
#This file is for understanding the sector in the pollutants database and trying to add gdp data by sector
# Author: julietlg@stud.ntnu.no
# Date: 16.10.2025

#%% importing the libraries
import pandas as pd
import matplotlib.pyplot as plt


#%% Downloading the file
df_pol = pd.read_csv("clean_dataset/pollutant_data.csv")

#%% Understanding the sector column
sectors = df_pol["sectorName"].unique()
print(sectors)

# %% Identifying the bigger sectors

super_sectors = [
    "Energy & Industry",
    "Transport",
    "Agriculture",
    "Residential & Commercial",
    "Natural & Waste"]

#%% Linking the sectors to the super sectors

# map_to_super_sector look for key word in sectorName in order to group by super sector
def map_to_super_sector(sector):
    s = str(sector).lower()

    #Energy & Industry
    if any(k in s for k in [
        "energy", "electricity", "heat", "power", "refining", "fuel", "combustion",
        "cement", "glass", "lime", "chemical", "ammonia", "acid", "nickel", "lead",
        "iron", "steel", "copper", "aluminium", "metal", "pulp", "paper", "print",
        "manufacturing", "industry", "industrial", "mining", "quarry", "solid fuels"
    ]):
        return "Energy & Industry"

    #Transport
    elif any(k in s for k in [
        "aviation", "maritime", "shipping", "navigation", "transport", "road",
        "vehicle", "bus", "car", "mopeds", "motorcycle", "train", "railway",
        "pipeline", "off-road", "mobile (including military", "automobile"
    ]):
        return "Transport"

    #Agriculture
    elif any(k in s for k in [
        "agriculture", "fishing", "forestry", "fertilizer", "fertilisers",
        "manure", "livestock", "urine", "dung", "soil", "broilers", "cattle",
        "hens", "sheep", "goats", "horses", "swine", "buffalo", "mules",
        "asses", "poultry", "field burning", "organic fertiliser"
    ]):
        return "Agriculture"

    #Residential & Commercial
    elif any(k in s for k in [
        "residential", "commercial", "institutional", "household", "gardening",
        "stationary combustion in manufacturing", "building", "services"
    ]):
        return "Residential & Commercial"

    #Natural & Waste
    elif any(k in s for k in [
        "waste", "incineration", "sewage", "cremation", "forest fire",
        "natural", "venting", "flaring", "open burning"
    ]):
        return "Natural & Waste"
    elif "total" in s or "NATIONAL" in s:
        return "NATIONAL TOTAL FOR COMPLIANCE"
    else:
        return "Other"

#%% Create an new column called supersectorName, we use the previous mapping function

df_pol["supersectorName"] = df_pol["sectorName"].apply(map_to_super_sector)


### Plotting year 1990 in Germany Nox emissions by super sector ###
#%% Selecting the data for year 1990, country Germany and pollutant NOx
df_pol_1990_de_nox = df_pol[(df_pol["year"] == 1990) & (df_pol["country"] == "Germany") & (df_pol["pollutantName"] == "NOx")]
df_pol_1990_de_nox_grouped = df_pol_1990_de_nox.groupby("supersectorName")["value"].sum().reset_index()
x_sticks = df_pol_1990_de_nox_grouped["supersectorName"]
print(df_pol_1990_de_nox_grouped)

#%% Plotting the data
fig, fig1 = plt.subplots(figsize=(10, 6))
fig1.bar(df_pol_1990_de_nox_grouped["supersectorName"],
       df_pol_1990_de_nox_grouped["value"])
fig1.set_title("NOx Emissions in Germany in 1990 by Super Sector") 
fig1.set_ylabel("Emissions (in tonnes)")
fig1.set_xlabel("Super Sector")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
