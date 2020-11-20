#Imports
import numpy as np
import pandas as pd
from scipy.optimize import linprog
from scipy import optimize
import matplotlib.pyplot as plt
#Importerer DataPrep
from DataPrep import ImportExcelFile 
from DataPrep import ImportFrekvenser 
import math
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe, Path) 
# ImportFrekvenser(Path)
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0. Stien angives med R'Sti.xlsx'
# Vælger man flere input med 1 vil den bare returnere kolonnenavnene, just dont 

WinrateListe = [r'C:\speciale2020\Data\Winrates_Data_168.xlsx', r'C:\speciale2020\Data\Winrates_Data_167.xlsx', r'C:\speciale2020\Data\Winrates_Data_166.xlsx']
FrekvensLister = [r'C:\speciale2020\Data\Frekvenser_168.xlsx', r'C:\speciale2020\Data\Frekvenser_167.xlsx', r'C:\speciale2020\Data\Frekvenser_166.xlsx']
count = 0
tau_168,tau_168_afrundet = 0.16080402010050251, 0.1708542713567839
tau_167, tau_167_afrundet = 0.05025125628140704, 0.05025125628140704
tau_166, tau_166_afrundet = 0.1708542713567839, 0.2613065326633166
alpha_168,beta_168 = 0.25908484, 2.77460386
alpha_167,beta_167 = 0.2899148,6.54266467
alpha_166,beta_166 = 0.17872715,1.78459794
alpha_168_afrund, beta_168_afrund = 1.20023133, 9.87212161
alpha_167_afrund, beta_167_afrund  = 0.38608988, 7.78001212
alpha_166_afrund, beta_166_afrund = 0.15303938 , 1.09506258

print("Tau")
print((tau_168+tau_167+tau_166)/3)
print("Tau afrundet")
print((tau_168_afrundet+tau_167_afrundet+tau_166_afrundet)/3)
print("Alpha")
print((alpha_168+alpha_167+alpha_166)/3)
print("Alpha afrundet")
print((alpha_168_afrund+alpha_167_afrund+alpha_166_afrund)/3)
print("Beta")
print((beta_168+beta_167+beta_166)/3)
print("Beta afrundet")
print((beta_168_afrund+beta_167_afrund+beta_166_afrund)/3)

'''
for i in range(len(WinrateListe)):
    #Winrates Data
    PathWin = WinrateListe[count]
    #Frekvens Data
    PathFrek = FrekvensLister[count]

    deck_names = ImportExcelFile(1,0,0, PathWin)
    winrates = ImportExcelFile(0,1,0, PathWin)
    data = ImportExcelFile(0,0,1, PathWin)
    frekvenser = ImportFrekvenser(PathFrek)

    #Dominans, Syntax: ElimineringDomStrat(deck, winrates)
    from ElimineringDomineredeStrat import ElimineringDomStrat
    ElimineringDomStrat(deck_names, winrates)
    level = 5
    #from MLEEstimation import MLEPlot
    #MLEPlot(level, tau)
    from CHModel import CHSolve

    from DumbellPlot import MixedEqGraph
    #Syntax: MixedEqGraph(Vores_Nash, Frekvenser)
    #MixedEqGraph(solvemixednash(deck_names, winrates, 1), frekvenser,CHSolve(deck_names, winrates, level+1, 0, tau, 1), CHSolveAfrund(deck_names, winrates, level+1, 0, tau, 1) )

    from LeastSquares import OptLS_Standard
    OptLS_Standard(deck_names, winrates, frekvenser, level+1)
    ###POISSON/###


    ###/BETA###
    print("BETAFORDELING:")
    from CHModelBetaDistAfrund import CHSolveBetaAfrund
    from CHModelBetaDist import CHSolveBeta
    from CHModelBetaDist import player_distribution
    from AlphaBetaOptimizer import f_one
    from AlphaBetaOptimizer import f_two
    import math

    sum_func1 = lambda x: sum(f_one(x[0], x[1], deck_names, winrates, frekvenser, level))
    sum_func2 = lambda x: sum(f_two(x[0], x[1], deck_names, winrates, frekvenser, level))

    initial_guess = [0.5, 0.5]
    sol_case1 = optimize.minimize(sum_func1, initial_guess, method='SLSQP', bounds=[(0,None), (0, None)])
    sol_case2 = optimize.minimize(sum_func2, initial_guess, method='SLSQP', bounds=[(0,None), (0, None)])

    print("Alpha, Beta")
    print(sol_case1['x'])
    print(sol_case2['x'])

    #Optimale alpha og beta bruges til at beregne CH-modellerne
    print(CHSolveBeta(deck_names, winrates, level,sol_case1['x'][0], sol_case1['x'][1], 0, MLE = 0))
    print("Afrundet")
    print(CHSolveBetaAfrund(deck_names, winrates, level, sol_case2['x'][0], sol_case2['x'][1], 0, MLE = 0))
    count += 1
'''