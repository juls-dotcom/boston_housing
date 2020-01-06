import pandas as pd


# Checking for missing data
def show_NAs(dataf):
    """
    Describe NAs in dataframe
    
    :param dataf:
    :return: dataframe describing NAs in param dataframe
    """
    NAs = pd.concat([dataf.isnull().sum()], axis=1, keys=['NAs'])
    return NAs[NAs.sum(axis=1) > 0]
