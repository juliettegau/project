# Author:Juliette@ntnu something
# Date: 09.10.2025
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


file_path = r"C:\Users\jujug\Documents\Ecole\4. NTNU\PYTHON\dataset\NOx_database.csv"

df = pd.read_csv(file_path, sep='\t', encoding='utf-8')
print(df.head())
