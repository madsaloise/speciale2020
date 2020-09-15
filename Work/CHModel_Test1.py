import numpy as np
import matplotlib.pyplot as plt
import math
import CHFramework
def CHSolve(decks, winrates, levels):
    #Parametre og lister    
    normal_form_game = [[u for u in [[j, 100-j] for j in i]] for i in winrates]
    n=len(decks)
    k = []
    for i in range(levels):
        k.append(i)
    lamda1 = 0.56
    lamda2 = 0.05
    '''
    #Beregner sandsynligheder
    probs = []
    for i in k:
        if k == 0:
            probs.append((1.0/n))
        probs=tuple(probs)
    if player == 0:
        sum_action = []
        for i in range(n):
            temp_sum = 0
            for j in range(j):
                temp_sum = temp_sum + 
    '''
    


        
