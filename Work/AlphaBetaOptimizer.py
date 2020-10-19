from scipy import optimize
import numpy as np
from CHModelBetaDist import CHSolveBeta
from CHModelBetaDistAfrund import CHSolveBetaAfrund
import matplotlib.pyplot as plt
import math

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

