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

def NashCHModelNash(Our_Nash, deck_names, winrates, alpha, beta, MLE =1):
    num_decks = len(deck_names)
    CHLVL0 = [1/num_decks for i in deck_names]
    CHLVL1 = []
    count = 0
    for i in deck_names:
        if deck_names[count] == deck_names[deck_names.index(CHSolveBeta(deck_names, winrates, 1, alpha, beta, 0, MLE = 2))]:
            CHLVL1.append(1)
        else:
            CHLVL1.append(0)
        count += 1
    MixedEq = list(Our_Nash)
    MixedEq_Decks = []
    NashProbs = []
    for a, b in MixedEq:
        MixedEq_Decks.append(a)
        NashProbs.append(b)
    dist_probs = player_distribution(3, alpha, beta)
    ListProbs = [CHLVL0, CHLVL1, NashProbs]
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
    c = [0 for i in range(num_decks)]
    c.append(1)
    A = list.copy(winrates)
    for i in A:
        count = 0
        for j in i:
            i[count] = NormProbs[count]* i[count]
            count += 1
    #print(len(A))
    # Lav C
    c = [0 for i in range(num_decks)]
    c.append(1)

    # append -1 til brug for øvre grænse
    for r in A:
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
    
    NashCH_Solution = linprog(c, A_ub=A, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    if MLE == 1:
        return zip(deck_names,NashCH_Solution['x'])
    elif MLE == 0:
        MixedStrat = [j for i,j in zip(deck_names,NashCH_Solution['x'])] 
        return MixedStrat

