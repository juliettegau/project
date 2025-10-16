#%%
"join_code.py"
#This file is for merging the cleaned datasets
# Author: dominiwm@stud.ntnu.no
# Date: 16.10.2025
# %%
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# %%
# import files
df_GDP = pd.read_csv(r"clean_dataset\cleaned gdp_population_gdp per capita dataset.csv")
# %%
