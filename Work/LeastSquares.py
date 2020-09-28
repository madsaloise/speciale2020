from scipy import optimize
import numpy as np
from CHModel import CHSolve
from CHModelAfrundingTester import CHSolveAfrund
import matplotlib.pyplot as plt
def OptLS_Standard(decks, winrates, Obs_Frequences, levels):
    Afrund_Val = []
    Standard_Val = []
    tau_values = np.linspace(0, 1)
    for q in range(levels):
        NumberOfGames = []
        count = 0
        for i in Obs_Frequences:
            NumberOfGames.append(sum(i)+i[count])
            count += 1 
        ShareOfGames = []
        for i in NumberOfGames:
            ShareOfGames.append(100 * i / sum(NumberOfGames))
        Sum_Each = []
        Sum_Each_Afrund = []
        for i in tau_values:
            Diff_Probs = []
            Diff_probs_Afrund = []
            count2 = 0
            for j in ShareOfGames:
                Diff_Probs.append((ShareOfGames[count2] - 100* CHSolve(decks, winrates, q+1, 0, i, 1)[count2])**2)
                Diff_probs_Afrund.append((ShareOfGames[count2] - 100* CHSolveAfrund(decks, winrates, q+1, 0, i, 1)[count2])**2)
                count2 += 1
            Sum_Each.append(sum(Diff_Probs))
            Sum_Each_Afrund.append(sum(Diff_probs_Afrund))
        Min_Func = Sum_Each.index(min(Sum_Each))
        Min_Func_Afrund = Sum_Each_Afrund.index(min(Sum_Each_Afrund))
        print("Standard:" + str(min(Sum_Each)) +"med tau på: " + str(tau_values[Sum_Each.index(min(Sum_Each))]) + ". Afrundet: " + str(min(Sum_Each_Afrund))+"med tau på: "+str(tau_values[Sum_Each_Afrund.index(min(Sum_Each_Afrund))]))
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.title("Least Squares by tau for level" + str(q))
        plt.scatter(tau_values, Sum_Each, color='navy', alpha=1, label='Standard')
        plt.scatter(tau_values, Sum_Each_Afrund, color='red', alpha=1, label='Afrundet')
        plt.legend()
        Afrund_Val.append(tau_values[Sum_Each_Afrund.index(min(Sum_Each_Afrund))])
        Standard_Val.append(tau_values[Sum_Each.index(min(Sum_Each))])
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.title("Optimale tau for forskellige levels")
    plt.scatter(range(levels), Standard_Val, color='navy', alpha=1, label='Standard')
    plt.scatter(range(levels), Afrund_Val, color='red', alpha=1, label='Afrundet')
    plt.legend()

    return Min_Func
    
'''
    
def OptLS_Afrund(decks, winrates, Obs_Frequences, levels):
    NumberOfGames = []
    count = 0
    for i in Obs_Frequences:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    Sum_Each = []
    tau_values = np.linspace(0, 1)
    for i in tau_values:
        Diff_Probs = []
        count2 = 0
        for j in ShareOfGames:
            Diff_Probs.append((ShareOfGames[count2] - 100* CHSolveAfrund(decks, winrates, levels, 0, i, 1)[count2])**2)
            count2 += 1
        Sum_Each.append(sum(Diff_Probs))
    Min_Func = Sum_Each.index(min(Sum_Each))
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.scatter(tau_values, Sum_Each, color='navy', alpha=1, label='Observationer')
    return Min_Func

'''
