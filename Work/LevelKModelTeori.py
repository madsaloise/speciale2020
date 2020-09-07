import seaborn as sns

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from scipy.optimize import linprog

def levelksolve(decks, winrates):
    
    num_decks=len(decks)
    

    #Beregner gennemsnitlige payoffs
    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
    avg_payoff=[]
    for i in payoffs:
        avg_pay = sum(i)/num_decks
        avg_payoff.append(avg_pay)
    #Indsætter player 0's valg i en liste
    level_0_maxpayoff = max(avg_payoff)

    level_k = []
    level_k.append(level_0_maxpayoff)
    level_0_index = avg_payoff.index(level_0_maxpayoff)

    maks_index = []
    deckID = [level_0_index]
    for p in range(4):
        for i in payoffs:
            maks_index.append(payoffs[level_0_index])
        level_k.append(max(maks_index))
        maxIDlist = np.argmax(maks_index)
        deckID.append(maxIDlist)
        level_0_index = maxIDlist
        maks_index = []
        
    print(deckID)
    print(level_k)
    #Danner en liste med forskellige spilleres valg
    counter=0
    plays = []
    print("I et level-k hierarki har vi følgende:")
    for i in level_k:
        ilevel_k = counter
        val_level_k = level_k[ilevel_k]
        deckIDcounter = deckID[ilevel_k]
        leveliplay = decks[deckIDcounter]
        plays.append("Level-" + str(counter+1) + " spiller: "+ str(leveliplay))
        counter += 1
    return plays

