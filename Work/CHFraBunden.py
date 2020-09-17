import pandas as pd
import numpy as np
import scipy as sp
from scipy.stats import chisquare
import matplotlib.pyplot as plt
from math import factorial
from math import exp
import scipy
import statsmodels
import nashpy as nash

def player_distribution(levels, tau):
    def poisson_distribution(levels, tau):
        distribution = (exp(-tau))*(tau**levels)/(factorial(levels))
        return distribution
    fractions = []
    for i in levels:
        fractions.append(poisson_distribution(tau, i))
    return fractions

        
def CHDistr(decks, winrates, levels, tau):
    n = len(winrates)
    def player_beliefs(levels):
        fractions = player_distribution(levels, tau)
        belief = sum(fractions[0:(levels)])
        return belief
    Deck_combination = []
    Deck_temp =[]
    for o in range(levels):
        for i in range(n):
            temp_dist = 0 
            for j in range(n):
                temp_dist = temp_dist + player_distribution(o, tau)[o-1]/player_beliefs(o)
            temp_dist = np.exp(temp_dist)
            Deck_temp.append(temp_dist)
        for i in range(n):
            temp_prob = Deck_temp[i] / sum(Deck_temp)
            Deck_combination.append(temp_prob)
        Deck_combination = tuple(Deck_combination)
    return Deck_combination


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

