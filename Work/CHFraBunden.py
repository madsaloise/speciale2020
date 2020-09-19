import pandas as pd
import numpy as np
import scipy as sp
from scipy.stats import chisquare
import matplotlib.pyplot as plt
from math import factorial
from math import exp
import scipy
import statsmodels
import gamegym
###///DONE###
def player_distribution(levels, tau):
    def poisson_distribution(levels, tau):
        distribution = (exp(-tau))*(tau**levels)/(factorial(levels))
        return distribution
    fractions = []
    for i in range(levels-1):
        fractions.append(poisson_distribution(i, tau))
    fractions.append(1-sum(fractions))
    return fractions
###DONE///###

from DataPrep import ImportExcelFile
PathWin = r'C:\Users\Mads\Desktop\Speciale\Kode\Git\Data\Winrates_Data_2.xlsx'
decks = ImportExcelFile(1,0,0, PathWin)
winrates = ImportExcelFile(0,1,0, PathWin)
data = ImportExcelFile(0,0,1, PathWin)        
def CHDistr(decks, winrates, levels, tau):
    n = len(winrates)
    def player_beliefs(levels, tau):
        fractions = []
        fractions.append(player_distribution(levels, tau))
        belief = sum(fractions[0:(levels)])
        return belief
    Deck_combination = []
    Deck_temp =[]
    for o in range(levels):
        for i in range(n):
            temp_dist = []
            for j in range(n):
                temp_dist = temp_dist + player_distribution(o, tau)
            temp_dist = np.exp(temp_dist)
            Deck_temp.append(temp_dist)
            for i in range(n):
                temp_prob = Deck_temp[i] / sum(Deck_temp)
                Deck_combination.append(temp_prob)
    Deck_combination = tuple(Deck_combination)
    return Deck_combination
print(CHDistr(decks, winrates, 5, 1))

def CHSolve(decks, winrates, levels, tau):
    num_decks=len(decks)
    #Beregner gennemsnitlige payoffs
    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
    avg_payoff=[]
    for i in payoffs:
        avg_pay = sum(i)/num_decks
        avg_payoff.append(avg_pay)

    #Laver normal_form game til højere CH-Levels
    n = len(payoffs)
    ###LEVEL 0###
    level_0_maxpayoff = max(avg_payoff)
    level_0_index = avg_payoff.index(level_0_maxpayoff)

    ###LEVEL 1###
    maks_index = []
    deckID = [level_0_index]
    for i in payoffs:
        maks_index.append(payoffs[level_0_index])
    deckID.append(np.argmin(maks_index))
    level_0_index = np.argmin(maks_index)
    maks_index = []

    ###Level 2###
    A = payoffs
    


    return deckID


def CHPrint(decks, winrates, levels, tau):
    Print_Decks = CHSolve(decks, winrates, levels, tau)
    for i in range(levels):
        print("Level-" + str(i) + " spiller" + str(Print_Decks[i]))

