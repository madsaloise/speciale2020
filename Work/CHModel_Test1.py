import numpy as np
import matplotlib.pyplot as plt
import math
def level_k_probabilities_2(k,player, n, lamda=0.56, lamda2 = 0.05):
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
                temp_sum = temp_sum + level_k_probabilities_1(k-1, (player+1) % 2, n ,lamda2)[j] * normal_form_game_player[i][j][0]
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
                temp_sum = temp_sum + level_k_probabilities_1(k - 1, (player + 1) % 2, n ,lamda2)[j] * \
                           normal_form_game_player[j][i][1]
            temp_sum = np.exp(lamda * temp_sum)
            sum_action.append(temp_sum)
        probs = []
        for i in range(n):
            temp_prob = sum_action[i] / sum(sum_action)
            probs.append(temp_prob)
        probs = tuple(probs)
        return probs
def level_k_probabilities_1(k,player, n, lamda=0.36):
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
                temp_sum = temp_sum + level_k_probabilities_1(k-1, (player+1) % 2, n)[j] * normal_form_game_player[i][j][0]
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
                temp_sum = temp_sum + level_k_probabilities_1(k - 1, (player + 1) % 2, n)[j] * \
                           normal_form_game_player[j][i][1]
            temp_sum = np.exp(lamda * temp_sum)
            sum_action.append(temp_sum)
        probs = []
        for i in range(n):
            temp_prob = sum_action[i] / sum(sum_action)
            probs.append(temp_prob)
        probs = tuple(probs)
        return probs

#Parametre og lister  
from DataPrep import ImportExcelFile   
PathWin = r'C:\Users\Mads\Desktop\Speciale\Kode\Git\Data\Winrates_Data_2.xlsx'
deck_names = ImportExcelFile(1,0,0, PathWin)
winrates = ImportExcelFile(0,1,0, PathWin)
normal_form_game = [[u for u in [[j, 100-j] for j in i]] for i in winrates]
normal_form_game_player = normal_form_game
levels = 2
player = 0
n=len(deck_names)
k = []
for i in range(levels):
    k.append(i)
lamda1 = 0.56
lamda2 = 0.05
weights = []
for i in range(len(k)):
    weights.append(level_k_probabilities_2(k, player, n))