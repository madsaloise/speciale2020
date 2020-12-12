from scipy import optimize
import numpy as np
from CHModel import CHSolve
from CHModelAfrund import CHSolveAfrund
from LevelKModelPoisson import levelksolvepoisson
import matplotlib.pyplot as plt
import numpy as np
def OptLS_Standard(decks, winrates, Obs_Frequences, levels):
    Afrund_Val = []
    Standard_Val = []
    LevelK_Val = []
    vægtetLevelL_Val = []
    #LevelKDecks = [20/12, 10, 20/12, 10, 10, 20/12, 20/12, 10, 10, 20/12, 10, 10, 20/12, 20/12, 20/12, 20/12, 20/12, 20/12, 20/12, 10]
    testlist = []
    count = 0
    '''
    for i in LevelKDecks:
        if count == 4:
            testlist.append(1)
        else:
            testlist.append(0)
        count += 1
    print(testlist)
    '''
    tau_values = np.linspace(0, 2, 200)
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
        #Sum_Each_vægtet_levelk = []
        for i in tau_values:
            Diff_Probs = []
            Diff_probs_Afrund = []
            Diff_Probs_LevelK = []
            #Diff_Probs_vægtet_levelk = []
            count2 = 0
            for j in ShareOfGames:
                Diff_Probs.append((ShareOfGames[count2] - 100* CHSolve(decks, winrates, q+1, 0, i, 1)[count2])**2)
                Diff_probs_Afrund.append((ShareOfGames[count2] - 100* CHSolveAfrund(decks, winrates, q+1, 0, i, 1)[count2])**2)
                Diff_Probs_LevelK.append((ShareOfGames[count2] - 100* levelksolvepoisson(decks, winrates, q+1, i)[count2])**2)
                #Diff_Probs_vægtet_levelk.append(((ShareOfGames[count2] - 100* CHSolve(decks, winrates, q+1, 0, i, 1)[count2])**2)*LevelKDecks[count2])
                count2 += 1
            Sum_Each.append(sum(Diff_Probs))
            Sum_Each_Afrund.append(sum(Diff_probs_Afrund))
            Sum_Each_LevelK.append(sum(Diff_Probs_LevelK))
            #Sum_Each_vægtet_levelk.append(sum(Diff_Probs_vægtet_levelk))
        Min_Func = Sum_Each.index(min(Sum_Each))
        Min_Func_Afrund = Sum_Each_Afrund.index(min(Sum_Each_Afrund))
        Min_Func_LevelK = Sum_Each_LevelK.index(min(Sum_Each_LevelK))
        #Min_Func_vægtet_levelk = Sum_Each_vægtet_levelk.index(min(Sum_Each_vægtet_levelk))
        print("Level-" + str(q))
        print("Standard:" + str(min(Sum_Each)) +"med tau på: " + str(tau_values[Sum_Each.index(min(Sum_Each))]) + ". Afrundet: " + str(min(Sum_Each_Afrund))+"med tau på: "+str(tau_values[Sum_Each_Afrund.index(min(Sum_Each_Afrund))]) + "og LevelK: " + str(min(Sum_Each_LevelK)) + "med en tau værdi på: " + str(tau_values[Sum_Each_LevelK.index(min(Sum_Each_LevelK))]))
        #print("CH model vægtet med levelK strategier:" + str(tau_values[Sum_Each_vægtet_levelk.index(min(Sum_Each_vægtet_levelk))]))
        #nplevelkdecks = Sum_Each_vægtet_levelk/sum(np.array(LevelKDecks))
        #VægtSum =  Sum_Each_vægtet_levelk/sum(LevelKDecks)
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.title("Least Squares by tau for level" + str(q))
        plt.scatter(tau_values, Sum_Each, color='navy', alpha=1, label='Standard')
        plt.scatter(tau_values, Sum_Each_Afrund, color='red', alpha=1, label='Afrundet')
        plt.scatter(tau_values, Sum_Each_LevelK, color='yellow', alpha=1, label='LevelK')
        #plt.scatter(tau_values, nplevelkdecks, color='brown', alpha=1, label='Vægtet med lvlk')
        plt.legend()
        Afrund_Val.append(tau_values[Sum_Each_Afrund.index(min(Sum_Each_Afrund))])
        Standard_Val.append(tau_values[Sum_Each.index(min(Sum_Each))])
        LevelK_Val.append(tau_values[Sum_Each_LevelK.index(min(Sum_Each_LevelK))])
        #vægtetLevelL_Val.append(tau_values[Sum_Each_vægtet_levelk.index(min(Sum_Each_vægtet_levelk))])
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.title("Optimale tau for forskellige levels")
    plt.scatter(range(levels), Standard_Val, color='navy', alpha=1, label='Standard')
    plt.scatter(range(levels), Afrund_Val, color='red', alpha=1, label='Afrundet')
    plt.scatter(range(levels), LevelK_Val, color='yellow', alpha=1, label='LevelK')
    #plt.scatter(range(levels), vægtetLevelL_Val, color='brown', alpha=1, label='Vægtet med lvlk')
    plt.legend()

    return Min_Func
    

