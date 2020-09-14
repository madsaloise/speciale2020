#Preparing Data from excel to multiple lists for rows and columns

import numpy as np

import pandas as pd

#Importerer
def ImportExcelFile(decknames, winrates, dataframe):
    df = pd.read_excel (r'C:\Users\Mads\Desktop\Speciale\Kode\Git\Data\Winrates_Data_2.xlsx')

    column_names = list(df.columns)

    if decknames == 1: 
        return column_names
    else:
        if dataframe == 1:
            return df
        else: 
            if winrates == 1:
                Row_list =[] 
                # Iterate over each row 
                for i in range((df.shape[0])):  
                    # the current row denoted by "i" 
                    Row_list.append(list(df.iloc[i, :])) 
                    
                return Row_list
            else:
                "Set one of the inputs to 1"
