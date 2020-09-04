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

deck_names = ImportExcelFile(1,0,0)
winrates = ImportExcelFile(0,1,0)
data = ImportExcelFile(0,0,1)

#Importerer 
from MixedEquilibriumWinrates import solve
#Syntax:
# solve(decks, winrates)
# decks = kolonnenavne
# winrates = rækkenavne (rækkenavne er en liste over winrates, print den for at tjekke den. Misledende navn..)
WinRatesMixedEq = list(solve(deck_names, winrates))

print(WinRatesMixedEq)
#Mixed Nash Equilibrium
print("Optimal sammensætning af deck i et mixed-nash equilibrium er: " + str(WinRatesMixedEq))

#Level-K Model, syntax: levelksolve(decks, winrates), level 0 antages at spille uniformt
from LevelKModelTeori import levelksolve
print(list(levelksolve(deck_names, winrates)))