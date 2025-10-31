#%%
"""Cleaned_Data_Set_GDP_and_Population.py"""
#This file is for cleaning and merging GDP and Population datasets
# Author: dominiwm@stud.ntnu.no
# Date: 15.10.2025

#%% 
# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#%%
# Import GDP & Population dataset
df_Population = pd.read_excel(r"C:\Users\domin\.Python Course\Population total.xlsx", sheet_name="Data", skiprows=3)
df_GDP = pd.read_excel(r"C:\Users\domin\.Python Course\GDP_absolute.xlsx", sheet_name="Data", skiprows=3)
df_Population
#%%
df_GDP
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
p
# %%
g
# %%
# Merge files + calculation per-capita
res = pd.merge(g, p, on=["Country Name", "Year"])
res["gdp_per_capita"] = res["GDP_USD"] / res["Population"]
res["Year"] = res["Year"].astype(int)
res
# %%
countries = ["Greece", "Sweden", "Germany"]
res = (res[res["Country Name"].isin(countries)] 
       [["Country Name", "Year", "Population", "GDP_USD", "gdp_per_capita"]]
       .sort_values(["Country Name", "Year"]).reset_index(drop=True))
res
# %%
# Save file
save_path = r"C:\Users\domin\.Python Course\cleaned gdp_population_gdp per capita dataset.csv"
res.to_csv(save_path, index=False)

# %% 
# Plot for GDP per capita 1990+
pivoted_gdppc = res.pivot(index="Year", columns="Country Name", values="gdp_per_capita")

plt.figure(figsize=(10, 6))
plt.plot(pivoted_gdppc.index, pivoted_gdppc['Germany'], label='Germany', color='tab:blue', linewidth=2)
plt.plot(pivoted_gdppc.index, pivoted_gdppc['Sweden'], label='Sweden', color='tab:green', linewidth=2)
plt.plot(pivoted_gdppc.index, pivoted_gdppc['Greece'], label='Greece', color='tab:red', linewidth=2)

plt.title("GDP per capita (1990+)", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("Year", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("US$ per person", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.legend(fontsize=12, prop={"family": "Segoe UI"})
plt.tight_layout()
plt.savefig("../ploting_code/Plots/GDP_per_capita.png", dpi=300)
plt.show()


# %% 
# Plot GDP absolute Current US$
pivoted_gdp = res.pivot(index="Year", columns="Country Name", values="GDP_USD")

plt.figure(figsize=(10, 6))
plt.plot(pivoted_gdp.index, pivoted_gdp['Germany'], label='Germany', color='tab:blue', linewidth=2)
plt.plot(pivoted_gdp.index, pivoted_gdp['Sweden'], label='Sweden', color='tab:green', linewidth=2)
plt.plot(pivoted_gdp.index, pivoted_gdp['Greece'], label='Greece', color='tab:red', linewidth=2)

plt.title("GDP (current US$) (1990+)", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("Year", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("US$", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.legend(fontsize=12, prop={"family": "Segoe UI"})
plt.tight_layout()
plt.savefig("../ploting_code/Plots/GDP_absolute.png", dpi=300)
plt.show()


# %% 
# Plot Population 1990+
pivoted_pop = res.pivot(index="Year", columns="Country Name", values="Population")

plt.figure(figsize=(10, 6))
plt.plot(pivoted_pop.index, pivoted_pop['Germany'], label='Germany', color='tab:blue', linewidth=2)
plt.plot(pivoted_pop.index, pivoted_pop['Sweden'], label='Sweden', color='tab:green', linewidth=2)
plt.plot(pivoted_pop.index, pivoted_pop['Greece'], label='Greece', color='tab:red', linewidth=2)

plt.title("Population (1990+)", fontsize=18, fontfamily="Segoe UI")
plt.xlabel("Year", fontsize=16, fontfamily="Segoe UI")
plt.ylabel("People", fontsize=16, fontfamily="Segoe UI")
plt.grid(True)
plt.legend(fontsize=12, prop={"family": "Segoe UI"})
plt.tight_layout()
plt.savefig("../ploting_code/Plots/Population.png", dpi=300)
plt.show()

# %%
