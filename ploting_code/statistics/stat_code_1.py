#%%
"""stat_code_1.py"""
#This file is use to do some satitucs on the df and to show correlation between variables
# Author: julietlg@stud.ntnu.no
# Date: 26.10.2025

#%% Importing librairies
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import os 

# %%  load the data
data = pd.read_csv(r'../../join_code/merged_grouped_dataset.csv')

# %% select data
data_ge = data[(data["country"] == "Germany")&(data["pollutantName"] == "NOx")]
data_ge = data_ge.drop(["country","pollutantName", "Country Name","Year"],axis = 1)

# %% calculate corr
corr = data_ge.corr()

# %% Plot corr
colors = ["darkred", "white", "darkred"]
cmap = LinearSegmentedColormap.from_list("custom", colors, N=256)

plt.figure(figsize=(10, 6))
sns.heatmap(
    corr,
    cmap=cmap,      # ta colormap
    annot=True,     # affiche les valeurs
    center=0,       # centre la couleur claire sur corr=0
    vmin=-1, vmax=1 # pour que -1 et +1 soient la même intensité
)
plt.show()
# %% Test de statitics Spearman non lin
from scipy.stats import spearmanr

r, p = spearmanr(data_ge["value"], data_ge["GDP_USD"])
print(r, p)
if p < 0.05 :
    print('Hypothesis valid, p-value :',p)

# %% Test de statitics Pearson lin
from scipy.stats import pearsonr

x = data_ge["value"]
y = data_ge["GDP_USD"]

r, p = pearsonr(x, y)

print("Coefficient de corrélation :", r)
print("p-value :", p)

# %%
