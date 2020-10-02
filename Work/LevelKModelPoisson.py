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

def levelksolvepoisson(decks, winrates, levels, tau):
    
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
    
    maks_index = []
    deckID = [level_0_index]
    for p in range(levels):
        for i in payoffs:
            maks_index.append(payoffs[level_0_index])
        deckID.append(np.argmin(maks_index))
        level_0_index = np.argmin(maks_index)
        maks_index = []
    #print(deckID)
    #Danner en liste med forskellige spilleres valg
    #print(player_distribution(0.14285714285714285, levels))
    plays = []
    #print("I et level-k hierarki med tau på 0.14 har vi følgende:")
    for j in range(levels):
        counter=0
        for i in decks:
            if j == 0:
                plays.append((1/num_decks) * player_distribution(tau, levels)[0])
            elif counter == deckID[j-1]:
                plays[counter] = plays[counter] + player_distribution(tau, levels)[j]
            else:
                pass
            counter += 1
    prob_plays = []        
    for i in range(len(plays)):
        prob_plays.append(plays[i]/sum(plays))
    return prob_plays
