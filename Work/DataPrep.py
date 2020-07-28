''' hs_gto.py

Calculates a game theory optimal deck selection strategy for hearthstone laddering. 

Utilities in the payoff matrix are based on win-rates from the tempostorm website '''

import seaborn as sns

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from scipy.optimize import linprog

#Importerer
def ImportExcelFile(Kolonner, Rækker, dataframe):
    df = pd.read_excel (r'C:\Users\Mads\Desktop\Speciale\Kode\Git\Data\Winrates_Data.xlsx')

    column_names = list(df.columns)

    
    if Kolonner == 1: 
        return column_names
    else:
        if dataframe == 1:
            return df
    '''
    Row_list =[] 
  
    # Iterate over each row 
    for index, rows in df.iterrows(): 
        # Create list for the current row 
    
        my_list =[rows.Date, rows.Event, rows.Cost] 
      
        # append the list to the final list 
        Row_list.append(my_list) 
    
        '''
    #if Rækker == 1:
    #    return Rowlist

