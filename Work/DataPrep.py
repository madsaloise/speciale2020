#Preparing Data from excel to multiple lists for rows and columns
import numpy as np
import pandas as pd

#Importerer
def ImportExcelFile(decknames, winrates, dataframe, Path):
    df = pd.read_excel (Path)

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

def ImportFrekvenser(Path):
    df = pd.read_excel (Path)
    column_names = list(df.columns)
    Row_list =[] 
    # Iterate over each row 
    for i in range((df.shape[0])):  
        # the current row denoted by "i" 
        Row_list.append(list(df.iloc[i, :])) 
    return Row_list

