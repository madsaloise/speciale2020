from scipy import optimize
import numpy as np
from CHModelBetaDist import CHSolve
from CHModelBetaDistAfrund import CHSolveAfrund
import matplotlib.pyplot as plt
from DataPrep import ImportExcelFile 
from DataPrep import ImportFrekvenser 
import math
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe, Path) 
# ImportFrekvenser(Path)
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0. Stien angives med R'Sti.xlsx'
# Vælger man flere input med 1 vil den bare returnere kolonnenavnene, just dont 


#Winrates Data
PathWin = r'C:\speciale2020\Data\Winrates_Data_2_169.xlsx'
#Frekvens Data
PathFrek = r'C:\speciale2020\Data\Frekvenser_169.xlsx'

deck_names = ImportExcelFile(1,0,0, PathWin)
winrates = ImportExcelFile(0,1,0, PathWin)
data = ImportExcelFile(0,0,1, PathWin)
frekvenser = ImportFrekvenser(PathFrek)

sum_func1 = lambda x: math.log10(sum(f_one(x[0], x[1])))
sum_func2 = lambda x: math.log10(sum(f_two(x[0], x[1])))
def f_one(alpha, beta):
    NumberOfGames = []
    count = 0
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    Diff_Probs = []
    count2 = 0
    for j in ShareOfGames:
        Diff_Probs.append((ShareOfGames[count2] - 100* CHSolve(deck_names, winrates, 5, alpha, beta, 0, MLE = 1)[count2])**2)
        count2 += 1
    return Diff_Probs

def f_two(alpha, beta):
    NumberOfGames = []
    count = 0
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    Diff_Probs = []
    count2 = 0
    for j in ShareOfGames:
        Diff_Probs.append((ShareOfGames[count2] - 100* CHSolveAfrund(deck_names, winrates, 5, alpha, beta, 0, MLE = 1)[count2])**2)
        count2 += 1
    return Diff_Probs
print(f_one(3.39633443e-09, 9.99999929e-01))

initial_guess = [0.5, 0.4]
sol_case1 = optimize.minimize(sum_func1, initial_guess, method='SLSQP', bounds=[(0,None), (0, None)])
sol_case2 = optimize.minimize(sum_func2, initial_guess, method='SLSQP', bounds=[(0,None), (0, None)])
#method='bounded', bounds=[(0, None), (0, None)]
print(sol_case1['x'])
print(sol_case2['x'])
