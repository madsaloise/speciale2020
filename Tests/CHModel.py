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

    def level_k_payoff_p1(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2,lk_probabilities_p):
        n=len(normal_form_game_player)
        player_probabilities = lk_probabilities_p
        level_0_probabilities = lk_probabilities_0
        level_1_probabilities = lk_probabilities_1
        level_2_probabilities = lk_probabilities_2
        player_distributionvar = player_distribution(tau, levels)
        payoff = 0
        for i in range(n):
            for j in range(n):
                #Checked
                payoff = payoff + player_probabilities[i] * normal_form_game_player[i][j][0] * (
                            level_0_probabilities[j] * player_distributionvar[0] + level_1_probabilities[j] *
                            player_distributionvar[1] + level_2_probabilities[j] * player_distributionvar[2])
        return payoff
    def level_k_payoff_p2(lk_probabilities_0,lk_probabilities_1,lk_probabilities_2, lk_probabilities_p):
        n=len(normal_form_game_player)
        player_probabilities = lk_probabilities_p
        level_0_probabilities = lk_probabilities_0
        level_1_probabilities = lk_probabilities_1
        level_2_probabilities = lk_probabilities_2
        player_distributionvar = player_distribution(tau, levels)
        payoff = 0
        for i in range(n):
            for j in range(n):
                payoff = payoff + player_probabilities[j] * normal_form_game_player[i][j][1] * (
                            level_0_probabilities[i] * player_distributionvar[0] + level_1_probabilities[i] *
                            player_distributionvar[1] + level_2_probabilities[i] * player_distributionvar[2])
        return payoff
    def game_play(tau):
        n = len(normal_form_game_player)
        lk_probabilities_0p1 = level_k_probabilities_1(0, 0)
        lk_probabilities_1p1 = level_k_probabilities_1(1, 0,tau)
        lk_probabilities_2p1 = level_k_probabilities_2(2, 0,tau, tau)
        lk_probabilities_0p2 = level_k_probabilities_1(0, 1)
        lk_probabilities_1p2 = level_k_probabilities_1(1, 1, tau)
        lk_probabilities_2p2 = level_k_probabilities_2(2, 1, tau, tau)
        print ('\n\n')
        print ('Game')
        print ('\n')
        print ('Player 1')
        print ('Level-0 -->', list(zip(decks, lk_probabilities_0p1)))
        print ('Level-1 -->', list(zip(decks,lk_probabilities_1p1)))
        print ('Level-2 -->',list(zip(decks,lk_probabilities_2p1)))
        payoff_10 = level_k_payoff_p1(lk_probabilities_0p2, lk_probabilities_1p2, lk_probabilities_2p2, lk_probabilities_0p1)
        payoff_11 = level_k_payoff_p1(lk_probabilities_0p2, lk_probabilities_1p2, lk_probabilities_2p2, lk_probabilities_1p1)
        payoff_12 = level_k_payoff_p1(lk_probabilities_0p2, lk_probabilities_1p2, lk_probabilities_2p2, lk_probabilities_2p1)
        payoff_1 = [payoff_10, payoff_11, payoff_12]
        print ('Avg. Payoff -->',payoff_1)
        print ('Player 2')
        print ('Level-0 -->', list(zip(decks,lk_probabilities_0p2)))
        print ('Level-1 -->', list(zip(decks,lk_probabilities_1p2)))
        print ('Level-2 -->', list(zip(decks,lk_probabilities_2p2)))
        payoff_20 = level_k_payoff_p2(lk_probabilities_0p1, lk_probabilities_1p1, lk_probabilities_2p1, lk_probabilities_0p2)
        payoff_21 = level_k_payoff_p2(lk_probabilities_0p1, lk_probabilities_1p1, lk_probabilities_2p1, lk_probabilities_1p2)
        payoff_22 = level_k_payoff_p2(lk_probabilities_0p1, lk_probabilities_1p1, lk_probabilities_2p1, lk_probabilities_2p2)
        payoff_2 = [payoff_20, payoff_21, payoff_22]
        print ('Avg. Payoff -->',payoff_2)
        return payoff_1, payoff_2
    return game_play(tau)
