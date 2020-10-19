from scipy import optimize
import numpy as np
from CHModelBetaDist import CHSolve
from CHModelBetaDistAfrund import CHSolveAfrund
from LevelKModelPoisson import levelksolvepoisson
import matplotlib.pyplot as plt
def OptLS_Standard(decks, winrates, Obs_Frequences, levels):
    Afrund_Val = []
    Standard_Val = []
    LevelK_Val = []
    alpha_values = np.linspace(0, 1)
    beta_values = np.linspace(0, 1)
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
        Sum_Each_LevelK = []
        Sum_Each_2 = []
        Sum_Each_Afrund_2 = []
        Sum_Each_LevelK_2 = []
        for i in alpha_values:
            Diff_Probs_2 = []
            Diff_probs_Afrund_2 = []
            Diff_Probs_LevelK = []
            for h in beta_values:
                Diff_Probs = []
                Diff_probs_Afrund = []
                Diff_Probs_LevelK = []
                count2 = 0
                for j in ShareOfGames:
                    Diff_Probs.append((ShareOfGames[count2] - 100* CHSolve(decks, winrates, q+1, i, h, 0, MLE = 1)[count2])**2)
                    Diff_probs_Afrund.append((ShareOfGames[count2] - 100* CHSolveAfrund(decks, winrates, q+1, i, h, 0, MLE = 1)[count2])**2)
                    #Diff_Probs_LevelK.append((ShareOfGames[count2] - 100* levelksolvepoisson(decks, winrates, q+1, i)[count2])**2)
                    count2 += 1
                Sum_Each.append(sum(Diff_Probs))
                Sum_Each_Afrund.append(sum(Diff_probs_Afrund))
                #Sum_Each_LevelK.append(sum(Diff_Probs_LevelK))
            Sum_Each_2.append(Sum_Each)
            Sum_Each_Afrund_2.append(Sum_Each_Afrund)
        Min_Func = Sum_Each_2.index(min(Sum_Each_2))
        Min_Func_Afrund = Sum_Each_Afrund_2.index(min(Sum_Each_Afrund_2))
        #Min_Func_LevelK = Sum_Each_LevelK.index(min(Sum_Each_LevelK))
        print("Level-" + str(q))
        print("Standard:" + str(min(Sum_Each)) +"med tau på: " + str(alpha_values[Sum_Each_2.index(min(Sum_Each_2))]) + ". Afrundet: " + str(min(Sum_Each_Afrund_2))+"med tau på: "+str(beta_values[Sum_Each_Afrund_2.index(min(Sum_Each_Afrund_2))]) )
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.title("Least Squares by tau for level" + str(q))
        plt.scatter(alpha_values, Sum_Each, color='navy', alpha=1, label='Standard')
        plt.scatter(alpha_values, Sum_Each_Afrund, color='red', alpha=1, label='Afrundet')
        #plt.scatter(tau_values, Sum_Each_LevelK, color='yellow', alpha=1, label='LevelK')
        plt.legend()
        Afrund_Val.append(alpha_values[Sum_Each_Afrund.index(min(Sum_Each_Afrund))])
        Standard_Val.append(alpha_values[Sum_Each.index(min(Sum_Each))])
        LevelK_Val.append(alpha_values[Sum_Each_LevelK.index(min(Sum_Each_LevelK))])
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.title("Optimale tau for forskellige levels")
    plt.scatter(range(levels), Standard_Val, color='navy', alpha=1, label='Standard')
    plt.scatter(range(levels), Afrund_Val, color='red', alpha=1, label='Afrundet')
    plt.scatter(range(levels), LevelK_Val, color='yellow', alpha=1, label='LevelK')
    plt.legend()

    return Min_Func
    

