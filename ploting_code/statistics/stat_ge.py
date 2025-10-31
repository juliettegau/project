#%%
"""stat_code_1.py"""
#This file is use to do fit a linaer function and to do some statitics test
# Author: julietlg@stud.ntnu.no
# Date: 28.10.2025

#%% Importing librairies
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import os 

# %%  load the data
data = pd.read_csv(r'../../join_code/merged_grouped_dataset.csv')

# %% select data
data_ge = data[(data["country"] == "Germany")&(data["pollutantName"] == "NOx")]
data_ge = data_ge.drop(["country","pollutantName", "Country Name","Year"],axis = 1)

x = data_ge["value"]
y = data_ge["GDP_USD"]

# %% linear fit

# Linear fit: y = a*x + b
a, b = np.polyfit(x, y, 1)

# Compute fitted line
y_fit = a * x + b

# Compute R² (coefficient of determination)
ss_res = np.sum((y - y_fit) ** 2)          # Residual sum of squares
ss_tot = np.sum((y - np.mean(y)) ** 2)     # Total sum of squares
r2 = 1 - (ss_res / ss_tot)

# Display results
print(f"Slope (a) = {a:.3f}")
print(f"Intercept (b) = {b:.3f}")
print(f"R² = {r2:.3f}")

# Plot data points and fit
plt.scatter(x, y, label='Data', color='blue')
plt.plot(x, y_fit, label=f'Fit: y = {a:.2f}x + {b:.2f} (R²={r2:.2f})', color='red')
plt.xlabel('NOx (kt)')
plt.ylabel('GPD (USD)')
plt.legend()
plt.title('Linear Fit of Nox emissions and GPD of Germany')
plt.show()


# %% Test Statitics

# Significance level
alpha = 0.05

# --- 1) Compute Pearson correlation ---
r, p_value = stats.pearsonr(x, y)
n = len(x)
df = n - 2  # degrees of freedom

# --- 2) Compute t-statistic manually (for verification) ---
t_stat = r * np.sqrt(df / (1 - r**2))

# --- 3) Fisher z-transformation for confidence interval ---
z = np.arctanh(r)                      # Fisher transformation
se_z = 1 / np.sqrt(n - 3)              # Standard error of z
z_crit = stats.norm.ppf(1 - alpha/2)   # Critical value for 95% CI
z_ci = (z - z_crit * se_z, z + z_crit * se_z)
r_ci = (np.tanh(z_ci[0]), np.tanh(z_ci[1]))  # Back-transform to r-scale

# --- 4) Decision rule ---
if p_value < alpha:
    decision = "Reject H0: there is a significant linear correlation."
else:
    decision = "Fail to reject H0: no significant linear correlation."

# --- 5) Optional: permutation test (non-parametric check) ---
n_perm = 10000
rng = np.random.default_rng(42)
perm_r = np.empty(n_perm)
for i in range(n_perm):
    y_perm = rng.permuted(y)
    perm_r[i] = np.corrcoef(x, y_perm)[0, 1]
p_perm = np.mean(np.abs(perm_r) >= abs(r))

# --- 6) Print summary ---
print("=== Pearson Correlation Test ===")
print(f"Sample size (n): {n}")
print(f"Correlation coefficient (r): {r:.4f}")
print(f"t-statistic: {t_stat:.4f}")
print(f"Degrees of freedom: {df}")
print(f"p-value (two-tailed): {p_value:.4e}")
print(f"95% CI for r (Fisher method): [{r_ci[0]:.4f}, {r_ci[1]:.4f}]")
print(f"Permutation test p-value (n={n_perm}): {p_perm:.4e}")
print(f"Decision at α = {alpha}: {decision}")

# %%
