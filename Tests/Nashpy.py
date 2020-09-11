import nashpy as nash
import numpy as np
import pandas as pd
#Importerer DataPrep
df = pd.read_excel (r'C:\Users\Mads\Desktop\Speciale\Kode\Git\Data\Winrates_Data_Artikel.xlsx')
Row_list =[] 
# Iterate over each row 
for i in range((df.shape[0])):  
    # the current row denoted by "i" 
    Row_list.append(list(df.iloc[i, :])) 
afkast = [[u for u in [(j/50.0)-1 for j in i]] for i in Row_list]
A = afkast 

spil = np.array(A)
#print(afkast)
rps = nash.Game(spil, spil2)
print(rps)
eqs = rps.support_enumeration()
for eq in eqs:
    print(eq)

