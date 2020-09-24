import numpy as np
from math import factorial
from math import exp

def player_distribution(tau, levels):
    def poisson_distribution(tau, levels):
        distribution = (exp(-tau))*(tau**levels)/(factorial(levels))
        return distribution
    fractions = []
    truncated_fractions = []
    for i in range(levels+1):
        fractions.append(poisson_distribution(tau, i))
    for i in range(levels+1):
        truncated_fractions.append(fractions[i]/sum(fractions))
    return truncated_fractions

def player_plays(winrates, level, deckID, indeks_tal):
    if level == 0:
        prob = 1/len(winrates)
        return prob
    elif indeks_tal in deckID:
        return 1
    else:
        return 0

def CHSolve(decks, winrates, levels, tau = 0.5):
    for i in range(levels):
        print(player_distribution(tau, i))
    num_decks=len(decks)
    #Beregner gennemsnitlige payoffs
    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
    avg_payoff=[]
    for i in payoffs:
        avg_pay = sum(i)/num_decks
        avg_payoff.append(avg_pay)
    
    #Indsætter player 0's valg i en liste
    level_0_maxpayoff = max(avg_payoff)
    level_0_index = avg_payoff.index(level_0_maxpayoff)
    deckID = [level_0_index]

    #Lvl1
    maks_index = []
    maks_index.append(payoffs[level_0_index])
    deckID.append(np.argmin(maks_index))
    level_0_index = np.argmin(maks_index)
    maks_index = []
    print(deckID)
    #Level 2 og op
    for p in range(levels-1):
        if p > 1:
            A = list.copy(winrates)
            for i in A:
                j_list = []
                count = 0
                for j in i:
                    temp_dist = []
                    for q in range(p):
                        temp_dist.append(j * player_distribution(tau, p)[q] * player_plays(winrates, q, deckID, count))
                        #print(player_plays(winrates, q, deckID, count))
                    j_list.append(sum(temp_dist))
                    count += 1
                print("Level-" + str(p) + "--->")
                print(j_list)
                maks_index.append(sum(j_list))
            #print("Level-" + str(p) + "--->")    
            #print(maks_index)
            deckID.append(maks_index.index(max(maks_index)))    
            maks_index = []
    print(deckID)
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
