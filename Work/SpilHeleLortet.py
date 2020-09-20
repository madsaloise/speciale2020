#Imports
import numpy as np
import pandas as pd
from scipy.optimize import linprog
#Importerer DataPrep
from DataPrep import ImportExcelFile 
from DataPrep import ImportFrekvenser 
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe, Path) 
# ImportFrekvenser(Path)
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0. Stien angives med R'Sti.xlsx'
# Vælger man flere input med 1 vil den bare returnere kolonnenavnene, just dont 

#Winrates Data
PathWin = r'C:\Users\Mads\Desktop\Speciale\Kode\Git\Data\Winrates_Data_2.xlsx'
#Frekvens Data
PathFrek = r'C:\Users\Mads\Desktop\Speciale\Kode\Git\Data\Frekvenser.xlsx'

deck_names = ImportExcelFile(1,0,0, PathWin)
winrates = ImportExcelFile(0,1,0, PathWin)
data = ImportExcelFile(0,0,1, PathWin)
frekvenser = ImportFrekvenser(PathFrek)

#Dominans, Syntax: ElimineringDomStrat(deck, winrates)
from ElimineringDomineredeStrat import ElimineringDomStrat
ElimineringDomStrat(deck_names, winrates)

#Importerer Nash
#Syntax: solvemixednash(decks, winrates)
from MixedEquilibriumWinrates import solvemixednash
#Printer
print("Optimal sammensætning af deck i et mixed-nash equilibrium er: " + str(solvemixednash(deck_names, winrates, 0)) + ". Andre decks spilles med en sandsynlighed på 0.")
#Level-K Model, 
#Syntax: levelksolve(decks, winrates, levels), level 0 antages at spille uniformt. For k spillere skrives levels som k-1.
from LevelKModelTeori import levelksolve
print(list(levelksolve(deck_names, winrates, 4)))

#CH Model, syntax: CHSolve(winrates, MatriceStørrelse, AntalSimuleringer = 10), level 0 antages at spille uniformt. For k spillere skrives levels som k-1.
import CHModel
from CHModel import CHSolve
print(CHSolve(winrates, deck_names, 0.5))

from MixedEqVSFrekvensGraf import MixedEqGraph
# Syntax: MixedEqGraph(Vores_Nash, Frekvenser)
MixedEqGraph(solvemixednash(deck_names, winrates, 1), frekvenser)
