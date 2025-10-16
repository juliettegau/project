import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load data
data_nox = pd.read_csv(r'C:\Users\jujug\Documents\Ecole\4. NTNU\PYTHON\project\clean_dataset\cleaned_NOx_database.csv')

# Different sectors
sectors = data_nox['sectorName'].unique()
year = 2000
country = 'Germany'

data_germany_2000 = data_nox[(data_nox['year'] == year) & (data_nox['country'] == country)]
data_germany_2000_by_sector = data_germany_2000.groupby('sectorName')['value'].mean()

plt.hist(data_germany_2000_by_sector, bins=10, edgecolor='black')
plt.show()