#Imports
import numpy as np
import pandas as pd
from scipy.optimize import linprog
from scipy import optimize
import matplotlib.pyplot as plt
import time


t0= time.process_time()


#Importerer DataPrep
from DataPrep import ImportExcelFile 
from DataPrep import ImportFrekvenser 
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

#Dominans, Syntax: ElimineringDomStrat(deck, winrates)
from ElimineringDomineredeStrat import ElimineringDomStrat
ElimineringDomStrat(deck_names, winrates)

#Importerer Nash
#Syntax: solvemixednash(decks, winrates)
from MixedEquilibriumWinrates import solvemixednash
#Printer
print("Optimal sammensætning af deck i et mixed-nash equilibrium er: " + str(solvemixednash(deck_names, winrates, 0)) + ". Andre decks spilles med en sandsynlighed på 0.")

#Optimale tau beregnet ved OptLS_Standard
tau = 0.1407035175879397
tau_afrund = 0.15075376884422112
tau_levelk = 0.1306532663316583
level = 5

###/POISSON###
print("POISSONFORDELING:")
print("LEVEL-K:")
#Syntax: levelksolve(decks, winrates, levels), level 0 antages at spille uniformt. For k spillere skrives levels som k-1.
from LevelKModelTeori import levelksolve
print(list(levelksolve(deck_names, winrates, level-1)))
from LevelKModelPoisson import levelksolvepoisson
print("Deckandele for level-k modellen: ")
print(levelksolvepoisson(deck_names, winrates, level, tau_levelk))

#CH Model, syntax: CHSolve(decks, winrates, levels, kommentarer, tau, decksandsynligheder = 1):, level 0 antages at spille uniformt. 
#"Kommentarer" skal være en, hvis man vil se sandsynligheder og payoffs, 0 ellers.
print("CH-MODEL:")
from CHModelAfrund import CHSolveAfrund
from CHModel import CHSolve
from CHModel import player_distributionpoisson

print("Standard Poisson-CH model: ")
print(CHSolve(deck_names, winrates, level, 0, tau, 0))
print(CHSolve(deck_names, winrates, level, 0, tau, 1))
print("tilhørende levelfordeling: ")
print(player_distributionpoisson(tau, level))
print("Afrundet Poisson-CH model: ")
print(CHSolveAfrund(deck_names, winrates, level, 0, tau, 0))
print(CHSolveAfrund(deck_names, winrates, level, 0, tau, 1))
print("tilhørende levelfordeling: ")
print(player_distributionpoisson(tau_afrund, level))

#Optimerer tau
from LeastSquares import OptLS_Standard
OptLS_Standard(deck_names, winrates, frekvenser, level+1)


###POISSON/###


###/BETA###
print("BETAFORDELING:")
from CHModelBetaDistAfrund import CHSolveBetaAfrund
from CHModelBetaDist import CHSolveBeta
from CHModelBetaDist import player_distribution
from CHModelFreeWeights import CHModelFree
from AlphaBetaOptimizer import f_one
from AlphaBetaOptimizer import f_two
from AlphaBetaOptimizer import f_three
from AlphaBetaOptimizer import f_four
from AlphaBetaOptimizer import f_five
from AlphaBetaOptimizer import f_six
from AlphaBetaOptimizer import f_seven
from BR_Til_Nash_CHMODEL import NashCHModelCH
#from BR_Til_Nash_NashLigevægt import NashCHModelNash
import math

sum_func1 = lambda x: sum(f_one(x[0], x[1], deck_names, winrates, frekvenser, level))
sum_func2 = lambda x: sum(f_two(x[0], x[1], deck_names, winrates, frekvenser, level))
sum_func3 = lambda x: sum(f_four(x[0], x[1], x[2], x[3], x[4], deck_names, winrates, frekvenser))
sum_func4 = lambda x: sum(f_five(x[0], x[1], x[2], x[3], x[4], deck_names, winrates, frekvenser))
sum_func6 = lambda x: sum(f_six(x[0], x[1], deck_names, winrates, frekvenser, level))
sum_func7 = lambda x: sum(f_seven(x[0], x[1], deck_names, winrates, frekvenser, level))

initial_guess = [0.5, 0.5]
initial_guess2 = [0.2, 0.2, 0.2, 0.2, 0.2]

sol_case1 = optimize.minimize(sum_func1, initial_guess, method='SLSQP', bounds=[(0,None), (0, None)])
sol_case2 = optimize.minimize(sum_func2, initial_guess, method='SLSQP', bounds=[(0,None), (0, None)])
sol_case3 = optimize.minimize(sum_func3, initial_guess2, method='SLSQP', bounds=[(0,None), (0, None),(0,None), (0, None), (0,None)])
sol_case4 = optimize.minimize(sum_func4, initial_guess2, method='SLSQP', bounds=[(0,None), (0, None),(0,None), (0, None), (0,None)])
sol_case6 = optimize.minimize(sum_func6, initial_guess, method='SLSQP', bounds=[(0,None), (0, None)])
sol_case7 = optimize.minimize(sum_func7, initial_guess, method='SLSQP', bounds=[(0,None), (0, None)])

print("Alpha,Beta for Standard CH: ")
print(sol_case1['x'])
print("Alpha,Beta for Afrundet CH: " )
print(sol_case2['x'])

NormSolDist1 = []
count = 0
for i in sol_case3['x']:
    NormSolDist1.append(sol_case3['x'][count]/sum(sol_case3['x']))
    count += 1
print("Vægte for Nash-CH model: " )
print(NormSolDist1)

NormSolDist2 = []
count = 0
for i in sol_case4['x']:
    NormSolDist2.append(sol_case4['x'][count]/sum(sol_case4['x']))
    count += 1
print("Vægte for Standard CH model med frie vægte: ")
print(NormSolDist2)

print("Alpha, Beta for CH model skaleret med frekvenser: ")
print(sol_case6['x'])

print("Alpha, Beta for CH model vægtet med 1 på level-k modellens prediktioner og 20/12 på resterende decks")
print(sol_case7['x'])


#Optimale alpha og beta bruges til at beregne CH-modellerne
print("Deck andele")
print("Beta Standard")
print(CHSolveBeta(deck_names, winrates, level,sol_case1['x'][0], sol_case1['x'][1], 0, MLE = 1))
print("tilhørende levelfordeling: ")
print(player_distribution(level,sol_case1['x'][0], sol_case1['x'][1]))
print("Beta Afrundet")
print(CHSolveBetaAfrund(deck_names, winrates, level, sol_case2['x'][0], sol_case2['x'][1], 0, MLE = 1))
print("tilhørende levelfordeling: ")
print(player_distribution(level,sol_case2['x'][0], sol_case2['x'][1]))
print("Nash-CH")
print(NashCHModelCH(solvemixednash(deck_names, winrates, 1), deck_names, winrates, sol_case3['x'][0], sol_case3['x'][1], sol_case3['x'][2], sol_case3['x'][3], sol_case3['x'][4], MLE = 1))
print("tilhørende levelfordeling: ")
print(NormSolDist1)
print("Standard CH med frie parametre")
print(CHModelFree(deck_names, winrates, sol_case4['x'][0], sol_case4['x'][1], sol_case4['x'][2], sol_case4['x'][3], sol_case4['x'][4], MLE = 1))
print("tilhørende levelfordeling: ")
print(NormSolDist2)
print("Standard CH vægtet med frekvenser")
print(CHSolveBeta(deck_names, winrates, level,sol_case6['x'][0], sol_case6['x'][1], 0, MLE = 1))
print("tilhørende levelfordeling: ")
print(player_distribution(level,sol_case6['x'][0], sol_case6['x'][1]))
print("Standard CH vægtet med 1 på level-k modellens prediktioner og 20/12 på resterende decks")
print(CHSolveBeta(deck_names, winrates, level,sol_case7['x'][0], sol_case7['x'][1], 0, MLE = 1))
print("tilhørende levelfordeling: ")
print(player_distribution(level,sol_case7['x'][0], sol_case7['x'][1]))
###BETA/###

###DUMBELL PLOTS###
from DumbellPlotEnkelte import MixedEqGraphNash
from DumbellPlotEnkelte import MixedEqGraphCHPoissonStandard
from DumbellPlotEnkelte import MixedEqGraphCHPoissonAfrundet
from DumbellPlotEnkelte import MixedEqGraphCHBetaAfrundet
from DumbellPlotEnkelte import MixedEqGraphCHBetaStandard
from DumbellPlotEnkelte import MixedEqLevelK
from DumbellPlotEnkelte import NashCH

MixedEqGraphNash(solvemixednash(deck_names, winrates, 1), frekvenser)
MixedEqGraphCHPoissonStandard(deck_names, CHSolve(deck_names, winrates, level, 0, tau, 1), frekvenser)
MixedEqGraphCHPoissonAfrundet(deck_names, CHSolveAfrund(deck_names, winrates, level, 0, tau_afrund, 1), frekvenser)
MixedEqGraphCHBetaStandard(deck_names, CHSolveBeta(deck_names, winrates, level, sol_case1['x'][0], sol_case1['x'][1], 0, MLE = 1), frekvenser)
MixedEqGraphCHBetaAfrundet(deck_names, CHSolveBetaAfrund(deck_names, winrates, level, 0.0899432,  0.79928276, 0, MLE = 1), frekvenser)
MixedEqLevelK(deck_names, levelksolvepoisson(deck_names, winrates, level, tau_levelk), frekvenser)
NashCH(deck_names, NashCHModelCH(solvemixednash(deck_names, winrates, 1), deck_names, winrates, 0.8638375736535256, 0.09599785625939583, 0.03119252040390985, 0.00813884245046459, 0.0008332072327040807, MLE = 1), frekvenser)

#Tests af andre uger
WinratesList = [r'C:\speciale2020\Data\Winrates_Data_166.xlsx', r'C:\speciale2020\Data\Winrates_Data_167.xlsx', r'C:\speciale2020\Data\Winrates_Data_168.xlsx']
FrekvenserList = [r'C:\speciale2020\Data\Frekvenser_166.xlsx', r'C:\speciale2020\Data\Frekvenser_167.xlsx', r'C:\speciale2020\Data\Frekvenser_168.xlsx']
WeekList = [166, 167, 168]
count = 0
initial_guess1 = [0.5, 0.5]
for i in WeekList:
    print(WeekList[count])
    deck_names = ImportExcelFile(1,0,0, WinratesList[count])
    winrates = ImportExcelFile(0,1,0, WinratesList[count])
    frekvenser = ImportFrekvenser(FrekvenserList[count])
    OptLS_Standard(deck_names, winrates, frekvenser, level+1)
    sum_func1 = lambda x: sum(f_one(x[0], x[1], deck_names, winrates, frekvenser, level))
    sol_case1 = optimize.minimize(sum_func1, initial_guess1, method='SLSQP', bounds=[(0,None), (0, None)])
    print("alpha, beta")
    print(sol_case1['x'])
    print(CHSolveBeta(deck_names, winrates, level,sol_case1['x'][0], sol_case1['x'][1], 0, MLE = 1))
    count += 1

#Tests af highability og lowability
WinratesList = [r'C:\speciale2020\Data\Winrates_Data_2_169.xlsx', r'C:\speciale2020\Data\Winrates_Data_2_169.xlsx']
FrekvenserList = [r'C:\speciale2020\Data\Frekvenser_169_PlatToLegend.xlsx', r'C:\speciale2020\Data\Frekvenser_169_UnderPlatinium.xlsx']
RankingList = ["Highability", "Lowability"]
count = 0
initial_guess1 = [0.5, 0.5]
for i in WeekList:
    print(RankingList[count])
    deck_names = ImportExcelFile(1,0,0, WinratesList[count])
    winrates = ImportExcelFile(0,1,0, WinratesList[count])
    frekvenser = ImportFrekvenser(FrekvenserList[count])
    OptLS_Standard(deck_names, winrates, frekvenser, level+1)
    sum_func1 = lambda x: sum(f_one(x[0], x[1], deck_names, winrates, frekvenser, level))
    sol_case1 = optimize.minimize(sum_func1, initial_guess1, method='SLSQP', bounds=[(0,None), (0, None)])
    print("alpha, beta")
    print(sol_case1['x'])
    print(CHSolveBeta(deck_names, winrates, level,sol_case1['x'][0], sol_case1['x'][1], 0, MLE = 1))
    count += 1

#Skal være til sidst
t1 = time.process_time() - t0
print("Tid, der er brugt på at køre koden: ", t1) # CPU seconds elapsed (floating point)
print("R^2 og l^2 er beregnet i excel og fremgår derfor ikke af dette program.")
plt.show()
