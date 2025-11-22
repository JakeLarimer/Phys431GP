# Data from Harris, Harris and Alessi (2013)
# test code to recreate Figure 1. 

# import pandas  and numpy for data analysis
import pandas as pd
import numpy as np

# import pyplot for plotting
import matplotlib.pyplot as plt

# GCS data file
file_name = "GCS_table.csv"

# load GCS data into dataframe
df = pd.read_csv(file_name, na_values=["nd"])

# list out DataFrame columns for future reference
print(df.columns)

# ensure all distances are numeric
df["D_Mpc"] = pd.to_numeric(df["D_Mpc"], errors="coerce")
print(df["D_Mpc"])

# create list of bins for distances
dist_bins = np.arange(0,261,2)

# count up number of galaxies at each distance
plt.hist(df['D_Mpc'], bins=dist_bins)
plt.title("GC Systems [Figure 1]")
plt.ylabel("Number of Galaxies")
plt.xlabel("Distance (Mpc)")
plt.show()