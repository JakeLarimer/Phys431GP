import pandas as pd

class GP_DATA:
    def __init__(self):
        self.__GCSCAT = None
        self.__GCS = None
    
    # GCSCAT - Globular Cluster Systems of Galaxies Catalog Data
    def GCSCAT(self):
        if self.__GCSCAT == None:
            self.__GCSCAT = pd.read_csv('GCSCAT.csv')
        # Returns pandas dataframe of GCSCAT data
        return self.__GCSCAT

    # Full GCSCAT DATA
    def GCS(self):
        if self.__GCS == None:
            self.__GCS = pd.read_csv('GCS_table.csv', na_values=["nd"])
            # ensure all distances are numeric
            df["D_Mpc"] = pd.to_numeric(df["D_Mpc"], errors="coerce")
        # Returns pandas dataframe of GCSCAT data
        return self.__GCSCAT
        