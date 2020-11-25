#Imports
import numpy as np
import pandas as pd
from scipy.optimize import linprog
from scipy import optimize
import matplotlib.pyplot as plt
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
'''
#Printer
print("Optimal sammensætning af deck i et mixed-nash equilibrium er: " + str(solvemixednash(deck_names, winrates, 0)) + ". Andre decks spilles med en sandsynlighed på 0.")
#Level-K Model, 
'''
tau = 0.1407035175879397
tau_afrund = 0.15075376884422112
tau_levelk = 0.1306532663316583
level = 5
'''
###/POISSON###
print("POISSONFORDELING:")
#Syntax: levelksolve(decks, winrates, levels), level 0 antages at spille uniformt. For k spillere skrives levels som k-1.
from LevelKModelTeori import levelksolve
print(list(levelksolve(deck_names, winrates, level-1)))
from LevelKModelPoisson import levelksolvepoisson

print(levelksolvepoisson(deck_names, winrates, level, tau_levelk))

#CH Model, syntax: CHSolve(decks, winrates, levels, kommentarer, tau = 0.5):, level 0 antages at spille uniformt. 
#"Kommentarer" skal være en, hvis man vil se sandsynligheder og payoffs, 0 ellers.
#from MLEEstimation import MLEPlot
from CHModelAfrund import CHSolveAfrund
from CHModel import CHSolve
print("standard")
print(CHSolve(deck_names, winrates, level, 0, tau, 0))
print(CHSolve(deck_names, winrates, level, 0, tau, 1))
print("Afrund")
print(CHSolveAfrund(deck_names, winrates, level, 0, tau, 0))
print(CHSolveAfrund(deck_names, winrates, level, 0, tau, 1))
'''
#from MLEEstimation import MLEPlot
#MLEPlot(level, tau)
from CHModel import CHSolve
'''
print("tau= 0.1")
print(CHSolve(deck_names, winrates, level, 0, 0.1, 0))
print("tau= 1.1")
print(CHSolve(deck_names, winrates, level, 0, 1.1, 0))
print("tau= 1")
print(CHSolve(deck_names, winrates, level, 0, 1, 0))
print(CHSolve(deck_names, winrates, level, 0, 2.9, 0))
'''
from DumbellPlot import MixedEqGraph
#Syntax: MixedEqGraph(Vores_Nash, Frekvenser)
#MixedEqGraph(solvemixednash(deck_names, winrates, 1), frekvenser,CHSolve(deck_names, winrates, level+1, 0, tau, 1), CHSolveAfrund(deck_names, winrates, level+1, 0, tau, 1) )
'''
from LeastSquares import OptLS_Standard
OptLS_Standard(deck_names, winrates, frekvenser, level+1)
'''
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
from BR_Til_Nash_CHMODEL import NashCHModelCH
from BR_Til_Nash_NashLigevægt import NashCHModelNash
import math
initial_guess1 = [0.5, 0.5]
initial_guess2 = [0.2, 0.2, 0.2, 0.2, 0.2]
'''

sum_func1 = lambda x: sum(f_one(x[0], x[1], deck_names, winrates, frekvenser, level))
sum_func2 = lambda x: sum(f_two(x[0], x[1], deck_names, winrates, frekvenser, level))
sol_case1 = optimize.minimize(sum_func1, initial_guess, method='SLSQP', bounds=[(0,None), (0, None)])
sol_case2 = optimize.minimize(sum_func2, initial_guess, method='SLSQP', bounds=[(0,None), (0, None)])
'''
'''
sum_func3 = lambda x: sum(f_four(x[0], x[1], x[2], x[3], x[4], deck_names, winrates, frekvenser))
sol_case3 = optimize.minimize(sum_func3, initial_guess2, method='SLSQP', bounds=[(0,None), (0, None),(0,None), (0, None), (0,None)])
'''
sum_func4 = lambda x: sum(f_five(x[0], x[1], x[2], x[3], x[4], deck_names, winrates, frekvenser))
sol_case4 = optimize.minimize(sum_func4, initial_guess2, method='SLSQP', bounds=[(0,None), (0, None),(0,None), (0, None), (0,None)])
print(sol_case4['x'])
NormSolDist = []
count = 0
for i in sol_case4['x']:
    NormSolDist.append(sol_case4['x'][count]/sum(sol_case4['x']))
    count += 1
print(NormSolDist)
'''
print("Alpha, Beta")

print(sol_case1['x'])
print(sol_case2['x'])

print(sol_case3['x'])


for i in sol_case3['x']:
    NormSolDist.append(sol_case3['x'][count]/sum(sol_case3['x']))
    count += 1
print(NormSolDist)
print(NashCHModelCH(solvemixednash(deck_names, winrates, 1), deck_names, winrates, sol_case3['x'][0], sol_case3['x'][1], sol_case3['x'][2], sol_case3['x'][3], sol_case3['x'][4], MLE = 1))
print(NashCHModelCH(solvemixednash(deck_names, winrates, 1), deck_names, winrates, NormSolDist[0], NormSolDist[1], NormSolDist[2], NormSolDist[3], NormSolDist[4], MLE = 1))
print(NashCHModelCH(solvemixednash(deck_names, winrates, 1), deck_names, winrates, NormSolDist[0], NormSolDist[1], NormSolDist[2], NormSolDist[3], NormSolDist[4], MLE = 0))
#Resultater fra optimiser, bare disregard
alpha_standard, beta_standard = 0.20628184, 2.41621851
alpha_afrund, beta_afrund = 0.28102937, 3.21491841
alpha_standard_plat, beta_standard_plat = 0.24720334, 2.4701282 
alpha_afrund_plat, beta_afrund_plat = 0.45068354, 4.27547875
alpha_standard_underplat, beta_standard_underplat = 0.09316826, 2.65226339 
alpha_afrund_underplat, beta_afrund_underplat = 0.10634961, 2.63627197
'''
'''
#Optimale alpha og beta bruges til at beregne CH-modellerne
print(CHSolveBeta(deck_names, winrates, level,alpha_standard, beta_standard, 0, MLE = 1))
print("Afrundet")
print(CHSolveBetaAfrund(deck_names, winrates, level, alpha_afrund, beta_afrund, 0, MLE = 1))


print("Standard")
print(player_distribution(5, alpha_standard_underplat, beta_standard_underplat))
print("Afrundet")
print(player_distribution(5, alpha_afrund_underplat, beta_afrund_underplat))

#Tests
print(CHSolveBeta(deck_names, winrates, level,alpha_standard_plat, beta_standard_plat, 0, MLE = 1))
print(CHSolveBetaAfrund(deck_names, winrates, level,alpha_afrund_plat, beta_afrund_plat, 0, MLE = 1))
print("Standard")
print(player_distribution(5, alpha_standard_plat, beta_standard_plat))
print("Afrundet")
print(player_distribution(5, alpha_afrund_plat, beta_afrund_plat))
'''

###BETA/###
'''
###DUMBELL PLOTS###
from DumbellPlotEnkelte import MixedEqGraphNash
from DumbellPlotEnkelte import MixedEqGraphCHPoissonStandard
from DumbellPlotEnkelte import MixedEqGraphCHPoissonAfrundet
from DumbellPlotEnkelte import MixedEqGraphCHBetaAfrundet
from DumbellPlotEnkelte import MixedEqGraphCHBetaStandard
from DumbellPlotEnkelte import MixedEqLevelK
'''
'''
MixedEqGraphNash(solvemixednash(deck_names, winrates, 1), frekvenser)
MixedEqGraphCHPoissonStandard(deck_names, CHSolve(deck_names, winrates, level, 0, tau, 1), frekvenser)
MixedEqGraphCHPoissonAfrundet(deck_names, CHSolveAfrund(deck_names, winrates, level, 0, tau_afrund, 1), frekvenser)
MixedEqGraphCHBetaStandard(deck_names, CHSolveBeta(deck_names, winrates, level, 0.24688993, 2.46672905, 0, MLE = 1), frekvenser)
MixedEqGraphCHBetaAfrundet(deck_names, CHSolveBetaAfrund(deck_names, winrates, level, 0.0899432,  0.79928276, 0, MLE = 1), frekvenser)
MixedEqLevelK(deck_names, levelksolvepoisson(deck_names, winrates, level, tau_levelk), frekvenser)
#Skal være til sidst


from BR_Til_Nash_NashLigevægt import NashCHModelNash
print(list(NashCHModelNash(solvemixednash(deck_names, winrates, 1), deck_names, winrates, sol_case1['x'][0], sol_case1['x'][1])))
plt.show()
'''