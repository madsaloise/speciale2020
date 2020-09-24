import numpy as np
import matplotlib.pyplot as plt
import math
import collections
import functools
from math import factorial
from math import exp

def CHSolve(winrates, decks, tau, levels = 2):
    normal_form_game = [[u for u in [[j, 100-j] for j in i]] for i in winrates]
    normal_form_game_player=normal_form_game

    def level_k_probabilities_2(k,player,lamda=0.56, lamda2 = 0.05):
        n=len(normal_form_game_player)
        if k == 0:
            probs=[]
            for i in range(n):
                probs.append((1.0/n))
            probs=tuple(probs)
            return probs
        if player == 0:
            sum_action=[]
            for i in range(n):
                temp_sum = 0
                for j in range(n):
                    temp_sum = temp_sum + level_k_probabilities_1(k-1, (player+1) % 2,lamda2)[j] * normal_form_game_player[i][j][0]
                temp_sum = np.exp(lamda * temp_sum)
                sum_action.append(temp_sum)
            probs=[]
            for i in range(n):
                temp_prob = sum_action[i]/sum(sum_action)
                probs.append(temp_prob)
            probs=tuple(probs)
            return probs
        else:
            sum_action = []
            for i in range(n):
                temp_sum = 0
                for j in range(n):
                    temp_sum = temp_sum + level_k_probabilities_1(k - 1, (player + 1) % 2,lamda2)[j] * \
                            normal_form_game_player[j][i][1]
                temp_sum = np.exp(lamda * temp_sum)
                sum_action.append(temp_sum)
            probs = []
            for i in range(n):
                temp_prob = sum_action[i] / sum(sum_action)
                probs.append(temp_prob)
            probs = tuple(probs)
            return probs
    def level_k_probabilities_1(k,player,lamda=0.36):
        n=len(normal_form_game_player)
        if k == 0:
            probs=[]
            for i in range(n):
                probs.append((1.0/n))
            probs=tuple(probs)
            return probs
        if player == 0:
            sum_action=[]
            for i in range(n):
                temp_sum = 0
                for j in range(n):
                    temp_sum = temp_sum + level_k_probabilities_1(k-1, (player+1) % 2)[j] * normal_form_game_player[i][j][0]
                temp_sum = np.exp(lamda * temp_sum)
                sum_action.append(temp_sum)
            probs=[]
            for i in range(n):
                temp_prob = sum_action[i]/sum(sum_action)
                probs.append(temp_prob)
            probs=tuple(probs)
            return probs
        else:
            sum_action = []
            for i in range(n):
                temp_sum = 0
                for j in range(n):
                    temp_sum = temp_sum + level_k_probabilities_1(k - 1, (player + 1) % 2)[j] * normal_form_game_player[j][i][1]
                temp_sum = np.exp(lamda * temp_sum)
                sum_action.append(temp_sum)
            probs = []
            for i in range(n):
                temp_prob = sum_action[i] / sum(sum_action)
                probs.append(temp_prob)
            probs = tuple(probs)
            return probs
    def player_distribution(tau, levels):
        def poisson_distribution(tau, levels):
            distribution = (exp(-tau))*(tau**levels)/(factorial(levels))
            return distribution
        fractions = []
        for i in range(levels+1):
            fractions.append(poisson_distribution(tau, i))
        return fractions

    def game_play(tau):
        n = len(normal_form_game_player)
        j11 = level_k_probabilities_1(1, 0,tau).index(max(level_k_probabilities_1(1, 0,tau)))
        j21 = level_k_probabilities_2(2, 0,tau, tau).index(max(level_k_probabilities_2(2, 0,tau, tau)))
        j12 = level_k_probabilities_1(1, 1,tau).index(max(level_k_probabilities_1(1, 1,tau)))
        j22 = level_k_probabilities_2(2, 1,tau, tau).index(max(level_k_probabilities_2(2, 1,tau, tau)))

        lk_probabilities_0p1 = level_k_probabilities_1(0, 0)
        lk_probabilities_1p1 = max(level_k_probabilities_1(1, 0,tau))
        lk_probabilities_2p1 = max(level_k_probabilities_2(2, 0,tau, tau))
        lk_probabilities_0p2 = level_k_probabilities_1(0, 1)
        lk_probabilities_1p2 = max(level_k_probabilities_1(1, 1, tau))
        lk_probabilities_2p2 = max(level_k_probabilities_2(2, 1, tau, tau))
        print ('\n\n')
        print ('Game')
        print ('\n')
        print ('Player 1')
        print ('Level-0 -->', list(zip(decks, lk_probabilities_0p1)))
        print ('Level-1 -->', decks[j11],lk_probabilities_1p1)
        print ('Level-2 -->',decks[j21],lk_probabilities_2p1)

        print ('Player 2')
        print ('Level-0 -->', list(zip(decks,lk_probabilities_0p2)))
        print ('Level-1 -->', decks[j12],lk_probabilities_1p2)
        print ('Level-2 -->', decks[j22],lk_probabilities_2p2)

        
    return game_play(tau)

from DataPrep import ImportExcelFile 
from DataPrep import ImportFrekvenser 
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe, Path) 
# ImportFrekvenser(Path)
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0. Stien angives med R'Sti.xlsx'
# Vælger man flere input med 1 vil den bare returnere kolonnenavnene, just dont 

#Winrates Data
PathWin = r'C:\Users\Mads\Desktop\Speciale\Kode\Git\Data\Winrates_Data_2.xlsx'
#Frekvens Data
PathFrek = r'C:\Users\Mads\Desktop\Speciale\Kode\Git\Data\Frekvenser.xlsx'

deck_names = ImportExcelFile(1,0,0, PathWin)
winrates = ImportExcelFile(0,1,0, PathWin)
data = ImportExcelFile(0,0,1, PathWin)
frekvenser = ImportFrekvenser(PathFrek)
print(CHSolve(winrates, deck_names, 1))