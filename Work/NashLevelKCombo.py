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
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe, Path) 
# ImportFrekvenser(Path)
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0. Stien angives med R'Sti.xlsx'
# Vælger man flere input med 1 vil den bare returnere kolonnenavnene, just dont 


#Winrates Data
PathWin = r'C:\speciale2020\Data\Winrates_Data_2_169.xlsx'
#Frekvens Data
PathFrek = r'C:\speciale2020\Data\Frekvenser_169.xlsx'

deck_names = ImportExcelFile(1,0,0, PathWin)
winrates = ImportExcelFile(0,1,0, PathWin)
data = ImportExcelFile(0,0,1, PathWin)
frekvenser = ImportFrekvenser(PathFrek)


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

def NashCHModel(Our_Nash, deck_names, winrates, alpha, beta):
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
    print(CHLVL0)
    print(CHLVL1)
    print(NashProbs)
    dist_probs = player_distribution(3, alpha, beta)
    print(dist_probs)
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

    print(deck_names)
    print(NormProbs)
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

    return zip(deck_names,NashCH_Solution['x'])

print(list(NashCHModel(solvemixednash(deck_names, winrates, 1), deck_names, winrates, 0.5, 0.5)))
