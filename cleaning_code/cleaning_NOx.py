import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


file_path = r"C:\Users\jujug\Documents\Ecole\4. NTNU\PYTHON\dataset\NOx_database.csv"

# Load the dataset
df = pd.read_csv(file_path, sep='\t', encoding='utf-8')

#print(df.head())
#print(df.info())

dfNOX = df.copy()
dfNOX = dfNOX[dfNOX['pollutantName'] == 'NOx']

#print(df['country'].unique())
#print(dfNOX['formatName'].unique())

dfNOX_germany = dfNOX[dfNOX['country'] == 'Germany']
print(dfNOX_germany.head())
plt.plot(dfNOX_germany['year'], dfNOX_germany['value'], 'o')
plt.title('NOx in Germany')
plt.xlabel('Year')
plt.ylabel('NOx (in kt)')
plt.show()

dfNOX_greece = dfNOX[dfNOX['country'] == 'Greece']
print(dfNOX_greece.head())
plt.plot(dfNOX_greece['year'], dfNOX_greece['value'], 'o')
plt.title('NOx in Greece')
plt.xlabel('Year')
plt.ylabel('NOx (in kt)')
plt.show()

dfNOX_finland = dfNOX[dfNOX['country'] == 'Finland']
print(dfNOX_finland.head())
plt.plot(dfNOX_finland['year'], dfNOX_finland['value'], 'o')
plt.title('NOx in Finland')
plt.xlabel('Year')
plt.ylabel('NOx(in kt)')
plt.show()

dfNOX_france = dfNOX[dfNOX['country'] == 'France']
print(dfNOX_france.head())
plt.plot(dfNOX_france['year'], dfNOX_france['value'], 'o')
plt.title('NOx in France')
plt.xlabel('Year (in kt)')
plt.show()

dfNOX_germany_sector = dfNOX_germany.groupby("sectorName")["value"].mean()

# Création du camembert
plt.figure(figsize=(8, 8))
plt.pie(
    dfNOX_germany_sector, 
    labels=dfNOX_germany_sector.index, 
    autopct='%1.1f%%',   # Affiche le pourcentage
    startangle=90,
    colors=plt.cm.tab20.colors  # Palette sympa
)
plt.title("Répartition de la pollution NOx par secteur")
plt.show()