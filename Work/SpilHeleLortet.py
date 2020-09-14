#Imports
import numpy as np
import pandas as pd
from scipy.optimize import linprog


#Importerer DataPrep
from DataPrep import ImportExcelFile 
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe) 
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0
# Vælger man flere med et vil den bare returnere kolonnenavnene, just dont 

deck_names = ImportExcelFile(1,0,0)
winrates = ImportExcelFile(0,1,0)
data = ImportExcelFile(0,0,1)

#Dominans, Syntax: ElimineringDomStrat(deck, winrates)
from ElimineringDomineredeStrat import ElimineringDomStrat
ElimineringDomStrat(deck_names, winrates)

#Importerer Nash
#Syntax: solvemixednash(decks, winrates)
from MixedEquilibriumWinrates import solvemixednash
#Printer
print("Optimal sammensætning af deck i et mixed-nash equilibrium er: " + str(solvemixednash(deck_names, winrates)) + ". Andre decks spilles med en sandsynlighed på 0.")

#Level-K Model, 
#Syntax: levelksolve(decks, winrates, levels), level 0 antages at spille uniformt. For k spillere skrives levels som k-1.
from LevelKModelTeori import levelksolve
print(list(levelksolve(deck_names, winrates, 4)))
'''
#CH Model, syntax: CHSolve(decks, winrates, levels), level 0 antages at spille uniformt. For k spillere skrives levels som k-1.
from CHLoop import CHSolve
print(list(CHSolve(deck_names, winrates, 4)))'''