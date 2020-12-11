from scipy import optimize
import numpy as np
from CHModelBetaDist import CHSolveBeta
from CHModelBetaDistAfrund import CHSolveBetaAfrund
import matplotlib.pyplot as plt
import math
from MixedEquilibriumWinrates import solvemixednash
from BR_Til_Nash_CHMODEL import NashCHModelCH
from BR_Til_Nash_NashLigevægt import NashCHModelNash
from CHModelFreeWeights import CHModelFree
def f_one(alpha, beta, deck_names, winrates, frekvenser, levels):
    NumberOfGames = []
    count = 0
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    Diff_Probs = []
    count2 = 0
    for j in ShareOfGames:
        Diff_Probs.append((ShareOfGames[count2] - 100* CHSolveBeta(deck_names, winrates, levels, alpha, beta, 0, MLE = 1)[count2])**2)
        count2 += 1
    return Diff_Probs

def f_two(alpha, beta, deck_names, winrates, frekvenser, levels):
    NumberOfGames = []
    count = 0
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    Diff_Probs = []
    count2 = 0
    for j in ShareOfGames:
        Diff_Probs.append((ShareOfGames[count2] - 100* CHSolveBetaAfrund(deck_names, winrates, levels, alpha, beta, 0, MLE = 1)[count2])**2)
        count2 += 1
    return Diff_Probs
#Nash-CH model, hvor man løser Nash-ligevægten
def f_three(alpha, beta, deck_names, winrates, frekvenser, levels):
    NumberOfGames = []
    count = 0
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    Diff_Probs = []
    count2 = 0
    for j in ShareOfGames:
        Diff_Probs.append((ShareOfGames[count2] - 100* NashCHModelNash(solvemixednash(deck_names, winrates, 1), deck_names, winrates, alpha, beta, 0)[count2])**2)
        count2 += 1
    return Diff_Probs
#Nash
def f_four(alpha, beta, gamma, delta, epsilon, deck_names, winrates, frekvenser):
    NumberOfGames = []
    count = 0
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    Diff_Probs = []
    count2 = 0
    for j in ShareOfGames:
        Diff_Probs.append((ShareOfGames[count2] - 100* NashCHModelCH(solvemixednash(deck_names, winrates, 1), deck_names, winrates, alpha, beta, gamma, delta, epsilon, MLE = 1)[count2])**2)
        count2 += 1
    return Diff_Probs

#Frievægte normal CH
def f_five(alpha, beta, gamma, delta, epsilon, deck_names, winrates, frekvenser):
    NumberOfGames = []
    count = 0
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    Diff_Probs = []
    count2 = 0
    for j in ShareOfGames:
        Diff_Probs.append((ShareOfGames[count2] - 100* CHModelFree(deck_names, winrates, alpha, beta, gamma, delta, epsilon, MLE = 1)[count2])**2)
        count2 += 1
    return Diff_Probs

#Skaleret med frekvenser
def f_six(alpha, beta, deck_names, winrates, frekvenser, levels):
    NumberOfGames = []
    count = 0
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    Diff_Probs = []
    count2 = 0
    for j in ShareOfGames:
        Diff_Probs.append(((ShareOfGames[count2] - 100* CHSolveBeta(deck_names, winrates, levels, alpha, beta, 0, MLE = 1)[count2])**2)*ShareOfGames[count2])
        count2 += 1
    return Diff_Probs


#Skaleret med levelk (10% på levels >0, 20% på 0)
def f_seven(alpha, beta, deck_names, winrates, frekvenser, levels):
    NumberOfGames = []
    count = 0
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    Diff_Probs = []
    count2 = 0
    for j in ShareOfGames:
        Diff_Probs.append((ShareOfGames[count2] - 100* CHSolveBeta(deck_names, winrates, levels, alpha, beta, 0, MLE = 1)[count2])**2)
        count2 += 1
    return Diff_Probs