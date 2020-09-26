import numpy as np
from math import factorial
from math import exp

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
#SSH på 1/antallet af decks, hvis det kun er lvl 0. 1 ellers
def player_plays(winrates, level, deckID, indeks_tal):
    if level == 0:
        prob = 1/len(winrates)
        return prob
    elif indeks_tal == deckID and level > 0:
        return 1 
    else:
        return 0

def CHSolve(decks, winrates, levels, kommentarer, tau = 0.5, MLE = 0):
    print(player_distribution(tau, levels))
    num_decks=len(decks)
    #Beregner gennemsnitlige payoffs
    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
    avg_payoff=[]
    for i in payoffs:
        avg_pay = sum(i)/num_decks
        avg_payoff.append(avg_pay)
    
    #Indsætter player 1's valg i en liste
    level_0_maxpayoff = max(avg_payoff)
    level_0_index = avg_payoff.index(level_0_maxpayoff)
    deckID = [level_0_index]
    print(deckID)
    #Lvl1 og op
    maks_index = []
    payoff_index = []
    deck_prob = []
    for p in range(levels):
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
                        temp_dist = 1/len(A)
                    else:
                        temp_dist = temp_dist + player_distribution(tau, p)[q] * player_plays(winrates, q, deckID[q-1], count1)
                    #print(player_plays(winrates, q, deckID, count))
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
            #Nulstiller lister 
            maks_index = []
            payoff_index = []
            deck_prob = []
    #deckID = list.copy(deckID[1:])
    if MLE == 1:
        #Danner en liste med forskellige spilleres valg
        counter=0
        plays = []
        for i in deckID:
            ilevel_k = counter
            deckIDcounter = deckID[ilevel_k]
            leveliplay = decks[deckIDcounter]
            plays.append(leveliplay)
            counter += 1
        return plays
    else:
        #Danner en liste med forskellige spilleres valg
        counter=0
        plays = []
        print("I en CH-model har vi følgende:")
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
