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

#SSH på 1/antallet af decks, hvis det kun er lvl 0. 1 ellers
def player_plays(winrates, level, deckID, indeks_tal):
    if level == 0:
        prob = 1/len(winrates)
        return prob
    elif indeks_tal == deckID and level > 0:
        return 1 
    else:
        return 0
def CHSolveBetaAfrund(decks, winrates, levels, alpha_val, beta_val, kommentarer, MLE = 0):
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
                    elif not isinstance(deckID[q-1], list):
                        temp_dist = temp_dist + player_distribution(p, alpha_val, beta_val)[q] * player_plays(winrates, q, deckID[q-1], count1)
                    else: 
                        count4 = 0
                        for i in deckID[q-1]:
                            temp_dist = temp_dist + player_distribution(p, alpha_val, beta_val)[q] * player_plays(winrates, q, deckID[q-1][count4], count1) / len(deckID[q-1])
                            count4 += 1
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
            max_payoff = round(max(payoff_index))
            multiple_max = [round(i) for i, j in enumerate(payoff_index) if round(j) == max_payoff]
            if len(multiple_max) == 1:
                deckID.append(payoff_index.index(max(payoff_index)))   
            else:
                deckID.append(multiple_max) 
            if p == levels:
                return_prob = maks_index
            else:
                #Nulstiller lister 
                maks_index = []
                payoff_index = []
                deck_prob = []
    if MLE == 1:
        return return_prob
    else:
        #Danner en liste med forskellige spilleres valg
        counter=0
        plays = []
        #print("I en afrundet CH-model har vi følgende:")
        for i in deckID:
            ilevel_k = counter
            deckIDcounter = deckID[ilevel_k]
            if isinstance(deckIDcounter, list):
                counter1 = 0
                temp_list = []
                for j in deckIDcounter:
                    temp_list.append(decks[deckIDcounter[counter1]])
                    counter1 += 1
                plays.append("Level-" + str(counter+1) + " spiller er mix af: " + str(temp_list))
            else:
                leveliplay = decks[deckIDcounter]
                plays.append("Level-" + str(counter+1) + " spiller: "+ str(leveliplay))
            counter += 1
        return plays