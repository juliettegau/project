import pandas as pd
import matplotlib.pyplot as plt




path =  r"/Users/emmasjostrom/Desktop/TEP4221/NEC_NFR19_2025_25.05.26.csv"

df = pd.read_csv(path, sep="\t")   
print(df.head())
print(df.tail())


df_se = df[(df["countryCode"] == "SE") | (df["country"] == "Sweden")]
df_pl= df[(df["countryCode"] == "PL") | (df["country"] == "Poland")]

# Check result

print(f"Number of rows for Sweden: {len(df_se)}")
print(df_se["pollutantName"].unique())
#print(df["country"].unique()[:50])

# Filter for SOx only
df_sox = df_se[df_se["pollutantName"].str.strip().str.upper() == "SOX"]
df_sox1= df_pl[df_pl["pollutantName"].str.strip().str.upper() == "SOX"]
print(df_sox.head())
print(f"Number of rows for SOx: {len(df_sox)}")

df_sox1["value"] = pd.to_numeric(df_sox1["value"], errors="coerce")
df_sox["value"] = pd.to_numeric(df_sox["value"], errors="coerce")

sox_by_year = (
    df_sox.groupby("year")["value"]
    .sum()
    .reset_index()
)

print(sox_by_year)

sox_by_year1 = (
    df_sox1.groupby("year")["value"]
    .sum()
    .reset_index()
)



plt.plot(sox_by_year["year"], sox_by_year["value"], marker="o", label="Sweden")
plt.plot(sox_by_year1["year"], sox_by_year1["value"], marker="o", label="Poland")

plt.title("SOx Emissions Over Time")
plt.xlabel("Year")
plt.ylabel("Emissions (t)")
plt.grid(True)
plt.legend()  # shows which line is which
plt.show()





# --- Country 1 ---
plt.figure(figsize=(8,5))
plt.plot(sox_by_year["year"], sox_by_year["value"], marker="o", color="tab:blue")
plt.title("SOx Emissions Over Time — Sweden")
plt.xlabel("Year")
plt.ylabel("Emissions (kt)")
plt.grid(True)
plt.show()

# --- Country 2 ---
plt.figure(figsize=(8,5))
plt.plot(sox_by_year1["year"], sox_by_year1["value"], marker="o", color="tab:orange")
plt.title("SOx Emissions Over Time — Poland")
plt.xlabel("Year")
plt.ylabel("Emissions (kt)")
plt.grid(True)
plt.show()



# Create 1 row and 2 columns of subplots — separate axes
fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # no sharey

# --- Left plot ---
axes[0].plot(sox_by_year["year"], sox_by_year["value"], marker="o", color="tab:blue")
axes[0].set_title("SOx Emissions — Sweden")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Emissions (kt)")
axes[0].grid(True)

# --- Right plot ---
axes[1].plot(sox_by_year1["year"], sox_by_year1["value"], marker="o", color="tab:orange")
axes[1].set_title("SOx Emissions — Poland")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Emissions (kt)")
axes[1].grid(True)

plt.tight_layout()
plt.show()





#%%
import pandas as pd
import matplotlib.pyplot as plt



#%% Downloading the file 
path =  r"/Users/emmasjostrom/Desktop/TEP4221/NEC_NFR19_2025_25.05.26.csv"

df = pd.read_csv(path, sep="\t")   
#test

#%% Sorting out the relevant countries

df_se = df[(df["countryCode"] == "SE") | (df["country"] == "Sweden")]
df_de= df[(df["countryCode"] == "DE") | (df["country"] == "Germany")]
df_gr= df[(df["countryCode"] == "GR") | (df["country"] == "Greece")]


#%% Filter for SOx only
df_se_sox = df_se[df_se["pollutantName"].str.strip().str.upper() == "SOX"]
df_de_sox= df_de[df_de["pollutantName"].str.strip().str.upper() == "SOX"]
df_gr_sox= df_gr[df_gr["pollutantName"].str.strip().str.upper() == "SOX"]

#%% sorting out the relevant columns and merging the dataframes
cols = ["countryCode", "country", "sectorName", "year", "value", "unit"]
df_sox_all = (
    pd.concat([df_se_sox, df_de_sox, df_gr_sox], ignore_index=True)
      .loc[:, cols]
      .dropna(subset=["value"])  # valgfritt: dropp rader uten verdi
      .sort_values(["countryCode", "year", "sectorName"])
)
#reading the data to a csv file
df_sox_all.to_csv("sox_data.csv", index=False, encoding="utf-8")







#%% Summing it all not really cleaning the data


df_se_sox["value"] = pd.to_numeric(df_se_sox["value"], errors="coerce")
df_de_sox["value"] = pd.to_numeric(df_de_sox["value"], errors="coerce")
df_gr_sox["value"] = pd.to_numeric(df_gr_sox["value"], errors="coerce")

se_sox_by_year = (
    df_se_sox.groupby("year")["value"]
    .sum()
    .reset_index()
)



de_sox_by_year = (
    df_de_sox.groupby("year")["value"]
    .sum()
    .reset_index()
)
gr_sox_by_year = (
    df_gr_sox.groupby("year")["value"]
    .sum()
    .reset_index()
)



plt.plot(se_sox_by_year["year"], se_sox_by_year["value"], marker="o", label="Sweden")
plt.plot(de_sox_by_year["year"], de_sox_by_year["value"], marker="o", label="Germany")
plt.plot(gr_sox_by_year["year"], gr_sox_by_year["value"], marker="o", label="Greece")


plt.title("SOx Emissions Over Time")
plt.xlabel("Year")
plt.ylabel("Emissions (t)")
plt.grid(True)
plt.legend()  # shows which line is which
plt.show()


#%%



#%%








