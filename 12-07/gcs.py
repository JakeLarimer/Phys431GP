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
#df = df.apply(pd.to_numeric, errors='coerce')

# load GC color data into another dataframe
df_color = pd.read_csv('blue_red_GC.txt')
#df_color = df_color.apply(pd.to_numeric, errors='coerce')

# add GCS data to galaxies we have color info on
df_combined = pd.merge(df, df_color, 
                       left_on='Galaxy', 
                       right_on='Galaxy Name', 
                       how='inner')

# save combined
# df_combined.to_csv('GC_combined.csv', index=False)

# plot GC velocity dispersion vs red and blue
x = np.linspace(np.log(df_combined['sig_e_km/s']).min(), np.log(df_combined['sig_e_km/s']).max(), 1000)
plt.suptitle('Galaxy Velocity Dispersion vs. Peak Color of Globular Clusters')

plt.subplot(2,1,2)
m_1, b_1 = np.polyfit(np.log(df_combined['sig_e_km/s']), df_combined['Red Peak'], 1)
plt.plot(np.log(df_combined['sig_e_km/s']), df_combined['Red Peak'], '.', color='tab:red')
plt.plot(x, m_1*x + b_1, '--', color='tab:red', label=f'{m_1:.3f}x + {b_1:.3f}')
plt.xlabel('log Velocity Dispersion [km/s]')
plt.ylabel('Red Color Magnitude')
plt.grid()
plt.legend()

plt.subplot(2,1,1)
m_2, b_2 = np.polyfit(np.log(df_combined['sig_e_km/s']), df_combined['Blue Peak'], 1)
plt.plot(np.log(df_combined['sig_e_km/s']), df_combined['Blue Peak'], '.', color='tab:blue')
plt.plot(x, m_2*x + b_2, '--', color='tab:blue', label=f'{m_2:.3f}x + {b_2:.3f}')
plt.xlabel('log Velocity Dispersion [km/s]')
plt.ylabel('Blue Color Magnitude')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# plot GC mass versus luminosity
plt.title('Globular Cluster Mass vs. Galaxy Luminosity')
plt.plot(df['lg_M_G_M_sun'], df['M_V^T'], '.', color='tab:purple', markersize=8)
plt.xlabel("log(M_GC/M_sun)")
plt.ylabel("M_V^T")
plt.grid()
plt.show()