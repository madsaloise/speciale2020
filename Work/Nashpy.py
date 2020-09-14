import nashpy as nash
import numpy as np
import pandas as pd
from DataPrep import ImportExcelFile 
#tager en krig at beregne. Se jupyter notebook
deck_names = ImportExcelFile(1,0,0)
winrates = ImportExcelFile(0,1,0)

payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]

A = np.array(payoffs)
B = np.negative(A)

#Fejlen er bullshit
rps = nash.Game(A, B)
print(rps)
eqs = rps.support_enumeration()
print(list(eqs))