import pandas as pd

class GP_DATA:
    def __init__(self):
        self.__GCSCAT = None

    # GCSCAT - Globular Cluster Systems of Galaxies Catalog Data
    def GCSCAT(self):
        if self.__GCSCAT == None:
            self.__GCSCAT = pd.read_csv('GCSCAT.csv')
        # Returns pandas dataframe of GCSCAT data
        return self.__GCSCAT

