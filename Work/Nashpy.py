import nashpy as nash
import numpy as np
import pandas as pd
#Importerer DataPrep
df = pd.read_excel (r'C:\speciale2020\Data\Winrates_Data_Artikel.xlsx')
Row_list =[] 
# Iterate over each row 
for i in range((df.shape[0])):  
    # the current row denoted by "i" 
    Row_list.append(list(df.iloc[i, :])) 
print(Row_list)
afkast = [[u for u in [(j/50.0)-1 for j in i]] for i in Row_list]
print(afkast)
A = np.array(afkast)
print("a is:")
print(A)
B = np.negative(A)
print("b is:")
print(B)
rps = nash.Game(A, B)
print("rps is: ")
print(rps)

eqs = rps.support_enumeration()
print(list(eqs))

