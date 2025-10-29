#%%
"""ploting_code.py"""
#This file is to plot data from the grouped_data
# Author: julietlg@stud.ntnu.no
# Date: 21.10.2025
# changing the code
# Author: dominiwm@stud.ntnu.no
# Date: 22.10.2025

#%% Importing library
import pandas as pd
import matplotlib.pyplot as plt

#%% Importing dataset
df_grouped = pd.read_csv('../join_code/merged_grouped_dataset.csv')

#%% Creating masks to subset the DataFrame into country and pollutant specific DataFrames

#per country
mask_ge = df_grouped['country'] == 'Germany'
mask_se = df_grouped['country'] == 'Sweden'
mask_gr = df_grouped['country'] == 'Greece'

#per polluant
mask_nox = df_grouped['pollutantName'] == 'NOx'
mask_sox = df_grouped['pollutantName'] == 'SOx'
df_nox = df_grouped[mask_nox]
df_sox = df_grouped[mask_sox]

#%%
# NOx Plots per country

# Germany
plt.figure(figsize=(10, 5))
plt.plot(df_nox[mask_ge]['year'], df_nox[mask_ge]['value'], marker='o', linewidth=2, color='tab:blue')
plt.title("NOx emissions - Germany", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("Year", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("NOx (kt)", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.tight_layout()
plt.savefig("../ploting_code/Plots/NOx_Germany.png", dpi=300)
plt.show()

# Sweden
plt.figure(figsize=(10, 5))
plt.plot(df_nox[mask_se]['year'], df_nox[mask_se]['value'], marker='o', linewidth=2, color='tab:green')
plt.title("NOx emissions - Sweden", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("Year", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("NOx (kt)", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.tight_layout()
plt.savefig("../ploting_code/Plots/NOx_Sweden.png", dpi=300)
plt.show()

# Greece
plt.figure(figsize=(10, 5))
plt.plot(df_nox[mask_gr]['year'], df_nox[mask_gr]['value'], marker='o', linewidth=2, color='tab:red')
plt.title("NOx emissions - Greece", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("Year", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("NOx (kt)", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.tight_layout()
plt.savefig("../ploting_code/Plots/NOx_Greece.png", dpi=300)
plt.show()


#%%
# SOx Plots per country

# Germany
plt.figure(figsize=(10, 5))
plt.plot(df_sox[mask_ge]['year'], df_sox[mask_ge]['value'], marker='o', linewidth=2, color='tab:blue')
plt.title("SOx emissions - Germany", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("Year", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("SOx (kt)", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.tight_layout()
plt.savefig("../ploting_code/Plots/SOx_Germany.png", dpi=300)
plt.show()

# Sweden
plt.figure(figsize=(10, 5))
plt.plot(df_sox[mask_se]['year'], df_sox[mask_se]['value'], marker='o', linewidth=2, color='tab:green')
plt.title("SOx emissions - Sweden", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("Year", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("SOx (kt)", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.tight_layout()
plt.savefig("../ploting_code/Plots/SOx_Sweden.png", dpi=300)
plt.show()

# Greece
plt.figure(figsize=(10, 5))
plt.plot(df_sox[mask_gr]['year'], df_sox[mask_gr]['value'], marker='o', linewidth=2, color='tab:red')
plt.title("SOx emissions - Greece", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("Year", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("SOx (kt)", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.tight_layout()
plt.savefig("../ploting_code/Plots/SOx_Greece.png", dpi=300)
plt.show()

# %% NOx and GDP per country

# Germany
plt.figure(figsize=(8, 5))
plt.scatter(df_nox[mask_ge]['GDP_USD'], df_nox[mask_ge]['value'], label="Germany", color='tab:blue')
plt.title("NOx and GDP - Germany", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("GDP (USD)", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("NOx Emissions (kt)", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.tight_layout()
plt.savefig("../ploting_code/Plots/NOx_GDP_Germany.png", dpi=300)
plt.show()

# Sweden
plt.figure(figsize=(8, 5))
plt.scatter(df_nox[mask_se]['GDP_USD'], df_nox[mask_se]['value'], label="Sweden", color='tab:green')
plt.title("NOx and GDP - Sweden", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("GDP (USD)", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("NOx Emissions (kt)", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.tight_layout()
plt.savefig("../ploting_code/Plots/NOx_GDP_Sweden.png", dpi=300)
plt.show()

# Greece
plt.figure(figsize=(8, 5))
plt.scatter(df_nox[mask_gr]['GDP_USD'], df_nox[mask_gr]['value'], label="Greece", color='tab:red')
plt.title("NOx and GDP - Greece", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("GDP (USD)", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("NOx Emissions (kt)", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.tight_layout()
plt.savefig("../ploting_code/Plots/NOx_GDP_Greece.png", dpi=300)
plt.show()


# %% SOx and GDP per country

# Germany
plt.figure(figsize=(8, 5))
plt.scatter(df_sox[mask_ge]['GDP_USD'], df_sox[mask_ge]['value'], label="Germany", color='tab:blue')
plt.title("SOx and GDP - Germany", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("GDP (USD)", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("SOx Emissions (kt)", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.tight_layout()
plt.savefig("../ploting_code/Plots/SOx__GDP_Germany.png", dpi=300)
plt.show()

# Sweden
plt.figure(figsize=(8, 5))
plt.scatter(df_sox[mask_se]['GDP_USD'], df_sox[mask_se]['value'], label="Sweden", color='tab:green')
plt.title("SOx and GDP - Sweden", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("GDP (USD)", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("SOx Emissions (kt)", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.tight_layout()
plt.savefig("../ploting_code/Plots/SOx__GDP_Sweden.png", dpi=300)
plt.show()

# Greece
plt.figure(figsize=(8, 5))
plt.scatter(df_sox[mask_gr]['GDP_USD'], df_sox[mask_gr]['value'], label="Greece", color='tab:red')
plt.title("SOx and GDP - Greece", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("GDP (USD)", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("SOx Emissions (kt)", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.tight_layout()
plt.savefig("../ploting_code/Plots/SOx_GDP_Greece.png", dpi=300)
plt.show()

