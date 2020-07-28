#Imports
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import linprog


#Importerer DataPrep
from DataPrep import ImportExcelFile 
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe) 
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0
# Vælger man flere med et vil den bare returnere kolonnenavnene 

column_names = ImportExcelFile(1,0,0)
row_names = ImportExcelFile(0,1,0)
data = ImportExcelFile(0,0,1)

#Importerer 
from MixedEquilibriumWinrates import solve
#Syntax:
# solve(decks, winrates)
# decks = kolonnenavne
# winrates = rækkenavne (rækkenavne er en liste over winrates, print den for at tjekke den. Misledende navn..)
print(list(solve(column_names, row_names)))
