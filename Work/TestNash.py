import numpy as np
import pandas as pd
import string
from sympy import symbols, Eq, solve
from DataPrep import ImportExcelFile 
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe) 
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0
# Vælger man flere med et vil den bare returnere kolonnenavnene 

deck_names = ImportExcelFile(1,0,0)
winrates = ImportExcelFile(0,1,0)
data = ImportExcelFile(0,0,1)
payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
print(payoffs)