#%%
"""ploting_code.py"""
#This file is a first try to plot data from the grouped_data
# Author: julietlg@stud.ntnu.no
# Date: 21.10.2025

#%% Importing librairy
import pandas as pd
import matplotlib.pyplot as plt

#%% Downloading dataset
df_grouped = pd.read_csv('join_code\merged_grouped_dataset.csv')

#%% Mask

#per country
mask_ge = df_grouped['country'] == 'Germany'
mask_se = df_grouped['country'] == 'Sweden'
mask_gr = df_grouped['country'] == 'Greece'

#per polluant
mask_nox = df_grouped['pollutantName'] == 'NOx'
mask_sox = df_grouped['pollutantName'] == 'SOx'
df_nox = df_grouped[mask_nox]
df_sox = df_grouped[mask_sox]
#per years

#%% plotting Nox over the year for every country
fig, ax1 = plt.subplots(figsize=(10, 5))

# Tracer les lignes
ax1.plot(df_nox[mask_ge]['year'], df_nox[mask_ge]['value'], marker='o', label='Germany')
ax1.plot(df_nox[mask_se]['year'], df_nox[mask_se]['value'], marker='o', label='Sweden')
ax1.plot(df_nox[mask_gr]['year'], df_nox[mask_gr]['value'], marker='o', label='Greece')

# Mise en forme
ax1.set_title("")
ax1.set_xlabel("Year")
ax1.set_ylabel("NOX (kt)")
ax1.legend()
ax1.grid(True)

# Affichage
plt.tight_layout()
plt.show()

#%% plotting Sox over the year for every country
fig, ax1 = plt.subplots(figsize=(10, 5))

# Tracer les lignes
ax1.plot(df_sox[mask_ge]['year'], df_sox[mask_ge]['value'], marker='o', label='Germany')
ax1.plot(df_sox[mask_se]['year'], df_sox[mask_se]['value'], marker='o', label='Sweden')
ax1.plot(df_sox[mask_gr]['year'], df_sox[mask_gr]['value'], marker='o', label='Greece')

# Mise en forme
ax1.set_title("")
ax1.set_xlabel("Year")
ax1.set_ylabel("SOx (kt)")
ax1.legend()
ax1.grid(True)

# Affichage
plt.tight_layout()
plt.show()

# %% Nox et GPD
fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(df_nox[mask_ge]['GDP_USD'], df_nox[mask_ge]['value'], label="Germany")
ax.scatter(df_nox[mask_se]['GDP_USD'], df_nox[mask_se]['value'], label="Sweden")
ax.scatter(df_nox[mask_gr]['GDP_USD'], df_nox[mask_gr]['value'], label="Greece")

# Mise en forme
ax.set_xlabel("GDP (USD)")
ax.set_ylabel("NOx Emissions")
ax.set_title("Link NOx and GDP ?")
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.show()
# %% sox et GPD
fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(df_sox[mask_ge]['GDP_USD'], df_sox[mask_ge]['value'], label="Germany")
ax.scatter(df_sox[mask_se]['GDP_USD'], df_sox[mask_se]['value'], label="Sweden")
ax.scatter(df_sox[mask_gr]['GDP_USD'], df_sox[mask_gr]['value'], label="Greece")

# Mise en forme
ax.set_xlabel("GDP (USD)")
ax.set_ylabel("SOx Emissions")
ax.set_title("Link SOx and GDP ?")
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.show()

# %%
