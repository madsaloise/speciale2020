import numpy as np
from math import factorial
from math import exp
from scipy.stats import beta
import matplotlib.pyplot as plt
def player_distribution(levels, alpha_val, beta_val):
    def beta_distribution(mean, alpha_val, beta_val):
        distribution = beta.cdf(mean, alpha_val, beta_val)
        return distribution
    fractions = []
    fractions_temp = []
    truncated_fractions = []
    for i in range(levels+1):
        fractions_temp.append(beta_distribution((1+i)/levels, alpha_val, beta_val))
    for i in range(len(fractions_temp)-1):
        if i == 0: 
            fractions.append(fractions_temp[i])
        elif i > 0:
            fractions.append(fractions_temp[i]-fractions_temp[i-1])
    for i in range(levels):
        truncated_fractions.append(fractions[i]/sum(fractions))
    return truncated_fractions
print(player_distribution(5, 0.09316826, 2.65226339))
print(sum(player_distribution(5,  0.17872715,1.78459794)[2:]))
print(player_distribution(5, 0.15303938 , 1.09506258))
print(sum(player_distribution(5,  0.15303938 , 1.09506258)[2:]))
#print(player_distribution(5, 0.0899432,  0.79928276))
#SSH på 1/antallet af decks, hvis det kun er lvl 0. 1 ellers
def player_plays(winrates, level, deckID, indeks_tal):
    if level == 0:
        prob = 1/len(winrates)
        return prob
    elif indeks_tal == deckID and level > 0:
        return 1 
    else:
        return 0
def CHSolveBeta(decks, winrates, levels, alpha_val, beta_val, kommentarer, MLE = 0):
    #print(player_distribution(tau, levels))
    num_decks=len(decks)
    #Beregner gennemsnitlige payoffs
    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
    avg_payoff=[]
    for i in payoffs:
        avg_pay = sum(i)/num_decks
        avg_payoff.append(avg_pay)
    
    #Lvl1 og op
    deckID = []
    maks_index = []
    payoff_index = []
    deck_prob = []
    for p in range(levels+1):
        if p > 0:
            #print("LEVEL :" + str(p))
            #print(player_distribution(p, alpha_val, beta_val))
            #Kopierer liste
            A = list.copy(winrates)
            i_list = []
            count1 = 0
            #Beregner sandsynlighed for at du møder et deck betinget på dit level og beliefs omkring de andres levels.
            for i in A:
                temp_dist = 0
                #Summerer ssh for alle levels
                for q in range(p):
                    if q == 0:
                        temp_dist = temp_dist + (1/len(A))*player_distribution(p, alpha_val, beta_val)[q]
                        #print("Level 0 --->")
                        #print(player_distribution(levels+1, alpha_val, beta_val)[q])
                    else:
                        temp_dist = temp_dist + player_distribution(p, alpha_val, beta_val)[q] * player_plays(winrates, q, deckID[q-1], count1)
                        #print("Level " +str(p) +" --->")
                        #print(player_distribution(levels+1, alpha_val, beta_val)[q])
                        #print(player_plays(winrates, q, deckID[q-1], count1))
                    #print(player_plays(winrates, q, deckID, count1))
                i_list.append(temp_dist)
                count1 += 1
            count2 = 0
            #normaliserer
            for i in i_list:
                deck_prob.append(i_list[count2]/sum(i_list))
                count2 += 1
            maks_index = list.copy(deck_prob)
            #Beregner gennemsnitligt payoff
            for i in A:
                temp_sum = []
                count3 = 0
                for j in i:
                    temp_sum.append(j * maks_index[count3])
                    count3 += 1
                payoff_index.append(sum(temp_sum))
                temp_sum = []  
            if kommentarer == 1:
                print("Level-" + str(p) + "--->")    
                print("Sandsynligheden for at møde andre decks: " + str(maks_index))
                print("Payoffs: " + str(payoff_index))
            #Tilføjer deck-indekset til deckID-listen
            deckID.append(payoff_index.index(max(payoff_index)))   
            if p == levels:
                return_prob = maks_index
            else:
                #Nulstiller lister 
                maks_index = []
                payoff_index = []
                deck_prob = []
    #deckID = list.copy(deckID[1:])
    if MLE == 1:
        return return_prob
    elif MLE == 2:
        counter=0
        plays = []
        #print("I en CH-model har vi følgende:")
        for i in deckID:
            ilevel_k = counter
            deckIDcounter = deckID[ilevel_k]
            leveliplay = decks[deckIDcounter]
            counter += 1
        return leveliplay
    else:
        #Danner en liste med forskellige spilleres valg
        counter=0
        plays = []
        print("I en standard CH-model har vi følgende:")
        for i in deckID:
            ilevel_k = counter
            deckIDcounter = deckID[ilevel_k]
            leveliplay = decks[deckIDcounter]
            plays.append("Level-" + str(counter+1) + " spiller: "+ str(leveliplay))
            counter += 1
        return plays
'''
tau_range = [0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 100]
for i in tau_range:
    print("Fordeling for tau på: " + str(i))
    print(player_distribution(i, 10)) 
'''