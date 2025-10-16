#%%
"""Cleaned_Data_Set_GDP_and_Population.py"""
#This file is for cleaning and merging GDP and Population datasets
# Author: dominiwm@stud.ntnu.no
# Date: 15.10.2025
#%%
import pandas as pd
#%%
import matplotlib.pyplot as plt
# Import GDP & Population dataset
#%%
df_Population = pd.read_excel(
    r"C:\Users\domin\.Python Course\Population total.xlsx",
    sheet_name="Data",
    skiprows=3)
#%%
df_GDP = pd.read_excel(
    r"C:\Users\domin\.Python Course\GDP_absolute.xlsx",
    sheet_name="Data",
    skiprows=)
# %%
# Explore data structure
df_Population.head()
#%%
df_GDP.head()
# %%
df_Population.shape
#%%
df_GDP.shape
# %%
df_Population.describe()
#%%
df_GDP.describe()
# %%
# Countries of interest
countries = ["Greece", "Sweden", "Germany"]
# %%
# Years to keep (1990+)
years = [str(y) for y in range(1990, 2025)]
pop_keep = ["Country Name"] + [y for y in years if y in df_Population.columns]
gdp_keep = ["Country Name"] + [y for y in years if y in df_GDP.columns]
# %%
# Long format tables
p = df_Population[pop_keep].melt("Country Name", var_name="Year", value_name="Population")
g = df_GDP[gdp_keep].melt("Country Name", var_name="Year", value_name="GDP_USD")
# %%
# Merge + per-capita
res = pd.merge(g, p, on=["Country Name", "Year"])
res["gdp_per_capita"] = res["GDP_USD"] / res["Population"]
res["Year"] = res["Year"].astype(int)
# %%
countries = ["Greece", "Sweden", "Germany"]
res = (res[res["Country Name"].isin(countries)]
       [["Country Name", "Year", "Population", "GDP_USD", "gdp_per_capita"]]
       .sort_values(["Country Name", "Year"])
       .reset_index(drop=True))

res.head()
# %%
# Save to laptop
save_path = r"C:\Users\domin\.Python Course\gdp_pop_percap_1990on_GRC_SWE_DEU.csv"
res.to_csv(save_path, index=False)
print("Saved to:", save_path)

# %%
# Basic plots
for col, title, ylabel in [
    ("gdp_per_capita", "GDP per capita (1990+)", "US$ per person"),
    ("GDP_USD",        "GDP (current US$) (1990+)", "US$"),
    ("Population",     "Population (1990+)", "People"),
]:
    pivoted = res.pivot(index="Year", columns="Country Name", values=col)
    ax = pivoted.plot(title=title)
    ax.set_xlabel("Year")
    ax.set_ylabel(ylabel)
    plt.show()
# %%
