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
from MixedEquilibriumWinrates import solvemixednash
#Syntax:
# solvemixednash(decks, winrates)
# decks = kolonnenavne
# winrates = rækkenavne (rækkenavne er en liste over winrates, print den for at tjekke den. Misledende navn..)
WinRatesMixedEq = list(solvemixednash(deck_names, winrates))

print(WinRatesMixedEq)
#Mixed Nash Equilibrium
print("Optimal sammensætning af deck i et mixed-nash equilibrium er: " + str(WinRatesMixedEq))

#Level-K Model, syntax: levelksolve(decks, winrates, levels), level 0 antages at spille uniformt. For k spillere skrives levels som k-1.
from LevelKModelTeori import levelksolve
print(list(levelksolve(deck_names, winrates, 4)))

#CH Model, syntax: CHSolve(decks, winrates, levels), level 0 antages at spille uniformt. For k spillere skrives levels som k-1.
from CHLoop import CHSolve
print(list(levelksolve(deck_names, winrates, 4)))