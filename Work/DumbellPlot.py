import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def format(l):
    return "["+", ".join(["%.2f" % x for x in l])+"]"

def MixedEqGraph(Our_Nash, frekvenser, CHInput, CHRoundedInput):
    #Splitter tuple
    MixedEq = list(Our_Nash)
    MixedEq_Decks = []
    MixedEq_Winrates = []
    for a, b in MixedEq:
        MixedEq_Decks.append(a)
        MixedEq_Winrates.append(b*100)
    Standard_CH = [i*100 for i in CHInput]
    CH_rounded = [i*100 for i in CHRoundedInput]
    #Omdanner frekvensdata til andele
    NumberOfGames = []
    count = 0
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    CombinedList = []
    for i in range(len(MixedEq_Decks)):
        CombinedList.append([MixedEq_Decks[i], ShareOfGames[i], MixedEq_Winrates[i], Standard_CH[i], CH_rounded[i]])
    dfGraph = pd.DataFrame(CombinedList, columns = ["Decks","Observationer", "Nash", "Standard_CH", "Rounded_CH"])
    dfGraph.to_excel("nash-ligevægt_output.xlsx") 
    my_range = range(1, len(dfGraph.index)+1)
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.hlines(y = my_range, xmin = dfGraph['Observationer'], xmax = dfGraph['Nash'], color='grey', alpha = 0.4)
    plt.scatter(dfGraph['Observationer'], my_range, color='navy', alpha=1, label='Observationer')
    plt.scatter(dfGraph['Nash'], my_range, color='gold', alpha=1, label='Nash')
    plt.scatter(dfGraph['Standard_CH'], my_range, color='red', alpha=1, label='CH_Standard')
    plt.scatter(dfGraph['Rounded_CH'], my_range, color='green', alpha=1, label='CH_Rounded')
    plt.legend()
    textcordy = 7
    textcordx = 0
    for i, txt in enumerate(ShareOfGames):
        if abs(ShareOfGames[i] - MixedEq_Winrates[i]) < 1:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    for i, txt in enumerate(MixedEq_Winrates):
        if abs(MixedEq_Winrates[i] - ShareOfGames[i]) < 1:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (MixedEq_Winrates[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    #Titel og Akser
    plt.yticks(my_range, dfGraph['Decks'])
    plt.title("Nash VS Frekvens")
    plt.xlabel('Pct. spillet')
    plt.ylabel('Deck')