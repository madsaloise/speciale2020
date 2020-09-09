import seaborn as sns

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from scipy.optimize import linprog

def CHSolve(decks, winrates, levels):
    
    num_decks=len(decks)
    '''/DONE'''
    #Beregner gennemsnitlige payoffs
    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
    avg_payoff=[]
    for i in payoffs:
        avg_pay = sum(i)/num_decks
        avg_payoff.append(avg_pay)
    #Indsætter player 0's valg i en liste
    level_0_maxpayoff = max(avg_payoff)
    level_0_index = avg_payoff.index(level_0_maxpayoff)
    

    #TODO: Lav vægte
    #Uniforme vægte
    
    range_level = []
    #Gør det nemmere at vælge et tilfældigt level som højeste level som del af programmet. For k niveauer angives k-1 niveauer.
    for i in range(levels):
        range_level.append(i)
    
    #TODO: Inkluder vægte
    maks_index = []
    deckID = [level_0_index]
    for p in enumerate(range_level):
        weights = 1/(p+1)
        if p = 0:
            for i in payoffs:
                maks_index.append(payoffs[level_0_index])
            deckID.append(np.argmax(maks_index))
            level_0_index = np.argmax(maks_index)
            maks_index = [] '''DONE/'''
        else: 
            for i in payoffs:
                #Finder payoffs for hvert af decks, som spiller h spiller. level_0_indeks burde nok være en liste efterhånden?    
                for j in enumerate(deckID):
                    maks_index.append(payoffs[level_0_index[j]])
            #TODO: Det her skal vægtes og laves om til best-response funktion
            maxIDlist = np.argmax(maks_index)
            deckID.append(maxIDlist)
            level_0_index = [maxIDlist]
            maks_index = []
    #Danner en liste med forskellige spilleres valg
    counter=0
    plays = []
    print("I et level-k hierarki har vi følgende:")
    for i in deckID:
        ilevel_k = counter
        deckIDcounter = deckID[ilevel_k]
        leveliplay = decks[deckIDcounter]
        plays.append("Level-" + str(counter+1) + " spiller: "+ str(leveliplay) + " med sandsynlighederne" + str(PlayWeights))
        counter += 1
    return plays
