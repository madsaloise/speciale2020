from scipy import optimize
import numpy as np
from CHModelBetaDist import CHSolveBeta
from CHModelBetaDistAfrund import CHSolveBetaAfrund
from MixedEquilibriumWinrates import solvemixednash
from DataPrep import ImportExcelFile 
from DataPrep import ImportFrekvenser 
from math import factorial
from math import exp
from scipy.stats import beta
from scipy.optimize import linprog

def player_distribution_frievar(alpha, beta, gamma, delta, epsilon):
    dist = [alpha, beta, gamma, delta, epsilon]
    return dist
def player_plays(winrates, level, deckID, indeks_tal):
    if level == 0:
        prob = 1/len(winrates)
        return prob
    elif indeks_tal == deckID and level > 0:
        return 1 
    else:
        return 0
def CHSolveBeta2(decks, winrates, levels, alpha, beta, gamma, delta, epsilon, kommentarer, MLE = 0):
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
                        temp_dist = temp_dist + (1/len(A))*player_distribution_frievar(alpha, beta, gamma, delta, epsilon)[q]
                    else:
                        temp_dist = temp_dist + player_distribution_frievar(alpha, beta, gamma, delta, epsilon)[q] * player_plays(winrates, q, deckID[q-1], count1)
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
            #if kommentarer == 1:
                #print("Level-" + str(p) + "--->")    
                #print("Sandsynligheden for at møde andre decks: " + str(maks_index))
                #print("Payoffs: " + str(payoff_index))
            #Tilføjer deck-indekset til deckID-listen
            deckID.append(payoff_index.index(max(payoff_index)))   
            if p == levels:
                return_prob = maks_index
            else:
                #Nulstiller lister 
                maks_index = []
                payoff_index = []
                deck_prob = []
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
        #print("I en standard CH-model har vi følgende:")
        for i in deckID:
            ilevel_k = counter
            deckIDcounter = deckID[ilevel_k]
            leveliplay = decks[deckIDcounter]
            plays.append("Level-" + str(counter+1) + " spiller: "+ str(leveliplay))
            counter += 1
        return plays


def CHModelFree(deck_names, winrates, alpha, beta, gamma, delta, epsilon, MLE = 1):
    num_decks = len(deck_names)
    CHLVL0 = [1/num_decks for i in deck_names]
    CHLVL1 = []
    CHLVL2 = []
    CHLVL3 = []
    CHLVL4 = []
    count = 0
    for i in deck_names:
        if deck_names[count] == deck_names[deck_names.index(CHSolveBeta2(deck_names, winrates, 1, alpha, beta, gamma, delta, epsilon, 0, MLE = 2))]:
            CHLVL1.append(1)
        else:
            CHLVL1.append(0)
        count += 1
    count = 0
    for i in deck_names:
        if deck_names[count] == deck_names[deck_names.index(CHSolveBeta2(deck_names, winrates, 2, alpha, beta, gamma, delta, epsilon, 0, MLE = 2))]:
            CHLVL2.append(1)
        else:
            CHLVL2.append(0)
        count += 1
    count = 0
    for i in deck_names:
        if deck_names[count] == deck_names[deck_names.index(CHSolveBeta2(deck_names, winrates, 3, alpha, beta, gamma, delta, epsilon, 0, MLE = 2))]:
            CHLVL3.append(1)
        else:
            CHLVL3.append(0)
        count += 1
    count = 0
    for i in deck_names:
        if deck_names[count] == deck_names[deck_names.index(CHSolveBeta2(deck_names, winrates, 4, alpha, beta, gamma, delta, epsilon, 0, MLE = 2))]:
            CHLVL4.append(1)
        else:
            CHLVL4.append(0)
        count += 1
    dist_probs = player_distribution_frievar(alpha, beta, gamma, delta, epsilon)
    #print(dist_probs)
    ListProbs = [CHLVL0, CHLVL1, CHLVL2, CHLVL3, CHLVL4]
    CombinedProbs = []
    count = 0
    for i in range(len(deck_names)):
        temp_sum = 0
        count2 = 0
        for j in ListProbs:
            temp_sum = temp_sum + j[count]*dist_probs[count2]
            count2 += 1
        CombinedProbs.append(temp_sum)
        count += 1
    NormProbs = []
    for i in range(len(CombinedProbs)):
        NormProbs.append(CombinedProbs[i]/sum(CombinedProbs))
    payoff_index = []
    A = list.copy(winrates)
    #Beregner gennemsnitligt payoff
    for i in A:
        temp_sum = []
        count3 = 0
        for j in i:
            temp_sum.append(j * NormProbs[count3])
            count3 += 1
        payoff_index.append(sum(temp_sum))
        temp_sum = []  
    #print("Level-" + str(5) + "--->")    
    #print("Sandsynligheden for at møde andre decks: " + str(NormProbs))
    #print("Payoffs: " + str(payoff_index))
    #Tilføjer deck-indekset til deckID-listen
    if MLE == 1:
        return NormProbs
    elif MLE == 0: 
        Strategi = deck_names[payoff_index.index(max(payoff_index))]
        return Strategi


