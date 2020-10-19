import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
from scipy.special import factorial
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import statsmodels.api as sm
from statsmodels.api import Poisson
from scipy import stats
from scipy.stats import norm
from statsmodels.iolib.summary2 import summary_col
def MLEPlot(levels, maks_tau):
    poisson_pmf = lambda level, tau: tau**level / factorial(level) * exp(-tau)
    level_values = range(0, levels)
    tau_range = np.linspace(0,maks_tau, maks_tau+1)
    fig, ax = plt.subplots(figsize=(12, 8))

    for tau in tau_range:
        distribution = []
        for level_i in level_values:
            distribution.append(poisson_pmf(level_i, tau))
        ax.plot(level_values,
                distribution,
                label=f'$\ tau$={tau}',
                alpha=0.5,
                marker='o',
                markersize=8)
    ax.grid()
    ax.set_xlabel('$levels$', fontsize=14)
    ax.set_ylabel('$f(levels \mid \ tau)$', fontsize=14)
    ax.axis(xmin=0, ymin=0)
    ax.legend(fontsize=10)

#Maximum Likelihood:    
from CHModel import CHSolve 
def player_distribution(tau, levels):
    def poisson_distribution(tau, levels):
        distribution = (exp(-tau))*(tau**levels)/(factorial(levels))
        return distribution
    fractions = []
    truncated_fractions = []
    for i in range(levels):
        fractions.append(poisson_distribution(tau, i))
    for i in range(levels):
        truncated_fractions.append(fractions[i]/sum(fractions))
    return truncated_fractions
#print("fordeling")
#print(player_distribution(1, 5))
def player_plays(winrates, level, deckID, indeks_tal):
    if level == 0:
        prob = 1/len(winrates)
        return prob
    elif indeks_tal in deckID and level > 0:
        return 1 
    else:
        return 0
def MLEEstimation(decks, winrates, levels, tau):
    CH_List = CHSolve(decks, winrates, levels, 0, tau, 1)
    print(CH_List)
    Deck_List = []
    for i in decks:
        if i in CH_List:
            Deck_List.append(decks.index(i))
    print(Deck_List)
    probabilities = []
    count = 0
    #Beregner sandsynlighed for at du møder et deck betinget på dit level og beliefs omkring de andres levels.
    for i in winrates:
        temp_dist = 0
        #Summerer ssh for alle levels
        for q in range(levels):
            temp_dist = temp_dist + player_distribution(tau, levels)[q] * player_plays(winrates, q, Deck_List, count)
        probabilities.append(temp_dist)
        count += 1
    print(probabilities)


#Importerer DataPrep
from DataPrep import ImportExcelFile 
from DataPrep import ImportFrekvenser 
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe, Path) 
# ImportFrekvenser(Path)
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0. Stien angives med R'Sti.xlsx'
# Vælger man flere input med 1 vil den bare returnere kolonnenavnene, just dont 

#Winrates Data
PathWin = r'C:\speciale2020\Data\Winrates_Data_2.xlsx'
#Frekvens Data
PathFrek = r'C:\speciale2020\Data\Frekvenser.xlsx'

deck_names = ImportExcelFile(1,0,0, PathWin)
winrates = ImportExcelFile(0,1,0, PathWin)
data = ImportExcelFile(0,0,1, PathWin)
frekvenser = ImportFrekvenser(PathFrek)
MLEEstimation(deck_names, winrates, 5, tau = 0.5)