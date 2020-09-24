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
from scipy.optimize import linprog
from MixedEquilibriumWinrates import solvemixednash
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
print(player_distribution(2, 1))

from DataPrep import ImportExcelFile
PathWin = r'C:\Users\Mads\Desktop\Speciale\Kode\Git\Data\Winrates_Data_2.xlsx'
decks = ImportExcelFile(1,0,0, PathWin)
winrates = ImportExcelFile(0,1,0, PathWin)
data = ImportExcelFile(0,0,1, PathWin)   


 


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
    counter=0
    plays = []
    for i in deckID:
        ilevel_k = counter
        deckIDcounter = deckID[ilevel_k]
        leveliplay = decks[deckIDcounter]
        plays.append("Level-" + str(counter+1) + " spiller: "+ str(leveliplay))
        counter += 1
    ###Level 2 and so on###
    Level0Weights = [[u for u in [((j/50.0)-1)*(1/num_decks) for j in i]] for i in winrates]
    '''A = list.copy(payoffs)
    count = 0
    for i in range(levels): 
        for x in A:
            if count in deckID:
                for y in x:
                    pass
            else:
                for y in x:
                    y = 0
            count += 1
    print(A)
    '''
    
    C = []
        #payoffs_level = [[u  for u in [(j/50.0)-1 if i in deckID else -1000 for j in i]] for i in payoffs]
    for i in range(levels):
        B = []
        count = 0
        temp_list = []
        temp_payoff = 0
        #payoffs_level = [[u  for u in [(j/50.0)-1 if True == any(i in deckID) else -1000 for j in i]] for i in payoffs]
        for j in payoffs:
            A = []
            if count in deckID:
                for q in j:
                    temp_payoff = sum(player_distribution(i, tau))*q  
                    A.append(temp_payoff)
                B.append(A)       
            else:
                for q in j:
                    A.append(-1000)
                B.append(A)   
            count += 1     
        C = list.copy(B)     
        #temp_list.append(solvemixednash(decks, B, 2))
    print(len(B))
    # Maximer c
    '''
    c = [0 for i in range(num_decks)]

    c.append(1)
    for r in B:

        r.append(-1.0)

    # højreside-grænse

    b_ub = [0 for i in range(num_decks)]

    # equality constraint

    ones = [1 for i in range(num_decks)]

    ones.append(0)

    A_eq = [ones]

    # x summerer til 1

    b_eq = [1]

    # x og c must skal være positive

    bounds = [(0,None) for i in range(num_decks+1)]

    solution = linprog(c, A_ub=B, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    if levels == 1:
        return deckID[1]
    if levels > 2:
        return zip(decks,solution['x'])
    
for i in range(5):
    print(CHSolve(decks, winrates, i, 1))
    '''
'''
def CHPrint(decks, winrates, levels, tau):
    Print_Decks = CHSolve(decks, winrates, levels, tau)
    for i in range(levels):
        print("Level-" + str(i) + " spiller" + str(Print_Decks[i])) 
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

'''