import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def format(l):
    return "["+", ".join(["%.2f" % x for x in l])+"]"

def MixedEqGraphNash(Our_Nash, frekvenser):
    #Splitter tuple
    MixedEq = list(Our_Nash)
    MixedEq_Decks = []
    MixedEq_Winrates = []
    for a, b in MixedEq:
        MixedEq_Decks.append(a)
        MixedEq_Winrates.append(b*100)
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
        CombinedList.append([MixedEq_Decks[i], ShareOfGames[i], MixedEq_Winrates[i]])
    dfGraph = pd.DataFrame(CombinedList, columns = ["Decks","Observationer", "Nash"])
    my_range = range(1, len(dfGraph.index)+1)
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.scatter(dfGraph['Observationer'], my_range, color='deepskyblue', alpha=1, label='Observationer')
    plt.scatter(dfGraph['Nash'], my_range, color='khaki', alpha=1, label='Nash')
    plt.hlines(y = my_range, xmin = dfGraph['Observationer'], xmax = dfGraph['Nash'], color='peru', alpha = 0.4)
    plt.legend()
    textcordy = 7
    textcordx = 0
    for i, txt in enumerate(ShareOfGames):
        if 0 < ShareOfGames[i] - MixedEq_Winrates[i] < 1:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        elif -1 < ShareOfGames[i] - MixedEq_Winrates[i] < 0:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    for i, txt in enumerate(MixedEq_Winrates):
        if 0 < MixedEq_Winrates[i] - ShareOfGames[i] < 1:
            ax.annotate("{:.1f}".format(txt), (MixedEq_Winrates[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        elif -1 < MixedEq_Winrates[i] - ShareOfGames[i] < 0:
            ax.annotate("{:.1f}".format(txt), (MixedEq_Winrates[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (MixedEq_Winrates[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    #Titel og Akser
    plt.yticks(my_range, dfGraph['Decks'])
    plt.xlabel('Pct. spillet')
    plt.ylabel('Deck')

def MixedEqGraphCHPoissonStandard(MixedEq_Decks, CHInput, frekvenser):

    Standard_CH = [i*100 for i in CHInput]
    count = 0
    NumberOfGames = []
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    CombinedList = []
    for i in range(len(MixedEq_Decks)):
        CombinedList.append([MixedEq_Decks[i], ShareOfGames[i], Standard_CH[i]])
    dfGraph = pd.DataFrame(CombinedList, columns = ["Decks","Observationer", "CH-model"])
    my_range = range(1, len(dfGraph.index)+1)
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.hlines(y = my_range, xmin = dfGraph['Observationer'], xmax = dfGraph['CH-model'], color='peru', alpha = 0.4)
    plt.scatter(dfGraph['Observationer'], my_range, color='deepskyblue', alpha=1, label='Observationer')
    plt.scatter(dfGraph['CH-model'], my_range, color='khaki', alpha=1, label='Poisson-CH Model (1)')
    plt.legend()
    textcordy = 7
    textcordx = 0
    for i, txt in enumerate(ShareOfGames):
        if 0 < ShareOfGames[i] - Standard_CH[i] < 1:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        elif -1 < ShareOfGames[i] - Standard_CH[i] < 0:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    for i, txt in enumerate(Standard_CH):
        if 0 < Standard_CH[i] - ShareOfGames[i] < 1:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        elif -1 < Standard_CH[i] - ShareOfGames[i] < 0:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    #Titel og Akser
    plt.yticks(my_range, dfGraph['Decks'])
    plt.xlabel('Pct. spillet')
    plt.ylabel('Deck')

def MixedEqGraphCHPoissonAfrundet(MixedEq_Decks, CHInput, frekvenser):

    Standard_CH = [i*100 for i in CHInput]
    count = 0
    NumberOfGames = []
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    CombinedList = []
    for i in range(len(MixedEq_Decks)):
        CombinedList.append([MixedEq_Decks[i], ShareOfGames[i], Standard_CH[i]])
    dfGraph = pd.DataFrame(CombinedList, columns = ["Decks","Observationer", "CH-model"])
    my_range = range(1, len(dfGraph.index)+1)
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.hlines(y = my_range, xmin = dfGraph['Observationer'], xmax = dfGraph['CH-model'], color='peru', alpha = 0.4)
    plt.scatter(dfGraph['Observationer'], my_range, color='deepskyblue', alpha=1, label='Observationer')
    plt.scatter(dfGraph['CH-model'], my_range, color='khaki', alpha=1, label='Poisson-CH model (2)')
    plt.legend()
    textcordy = 7
    textcordx = 0
    for i, txt in enumerate(ShareOfGames):
        if 0 < ShareOfGames[i] - Standard_CH[i] < 1:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        elif -1 < ShareOfGames[i] - Standard_CH[i] < 0:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    for i, txt in enumerate(Standard_CH):
        if 0 < Standard_CH[i] - ShareOfGames[i] < 1:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        elif -1 < Standard_CH[i] - ShareOfGames[i] < 0:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    #Titel og Akser
    plt.yticks(my_range, dfGraph['Decks'])
    plt.xlabel('Pct. spillet')
    plt.ylabel('Deck')

def MixedEqGraphCHBetaAfrundet(MixedEq_Decks, CHInput, frekvenser):

    Standard_CH = [i*100 for i in CHInput]
    count = 0
    NumberOfGames = []
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    CombinedList = []
    for i in range(len(MixedEq_Decks)):
        CombinedList.append([MixedEq_Decks[i], ShareOfGames[i], Standard_CH[i]])
    dfGraph = pd.DataFrame(CombinedList, columns = ["Decks","Observationer", "CH-model"])
    my_range = range(1, len(dfGraph.index)+1)
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.hlines(y = my_range, xmin = dfGraph['Observationer'], xmax = dfGraph['CH-model'], color='peru', alpha = 0.4)
    plt.scatter(dfGraph['Observationer'], my_range, color='deepskyblue', alpha=1, label='Observationer')
    plt.scatter(dfGraph['CH-model'], my_range, color='khaki', alpha=1, label='Beta-CH Model (1)')
    plt.legend()
    textcordy = 7
    textcordx = 0
    for i, txt in enumerate(ShareOfGames):
        if 0 < ShareOfGames[i] - Standard_CH[i] < 1:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        elif -1 < ShareOfGames[i] - Standard_CH[i] < 0:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    for i, txt in enumerate(Standard_CH):
        if 0 < Standard_CH[i] - ShareOfGames[i] < 1:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        elif -1 < Standard_CH[i] - ShareOfGames[i] < 0:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    #Titel og Akser
    plt.yticks(my_range, dfGraph['Decks'])
    plt.xlabel('Pct. spillet')
    plt.ylabel('Deck')

def MixedEqGraphCHBetaStandard(MixedEq_Decks, CHInput, frekvenser):

    Standard_CH = [i*100 for i in CHInput]
    count = 0
    NumberOfGames = []
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    CombinedList = []
    for i in range(len(MixedEq_Decks)):
        CombinedList.append([MixedEq_Decks[i], ShareOfGames[i], Standard_CH[i]])
    dfGraph = pd.DataFrame(CombinedList, columns = ["Decks","Observationer", "CH-model"])
    my_range = range(1, len(dfGraph.index)+1)
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.hlines(y = my_range, xmin = dfGraph['Observationer'], xmax = dfGraph['CH-model'], color='peru', alpha = 0.4)
    plt.scatter(dfGraph['Observationer'], my_range, color='deepskyblue', alpha=1, label='Observationer')
    plt.scatter(dfGraph['CH-model'], my_range, color='khaki', alpha=1, label='Beta-CH Model (2)')
    plt.legend()
    textcordy = 7
    textcordx = 0
    for i, txt in enumerate(ShareOfGames):
        if 0 < ShareOfGames[i] - Standard_CH[i] < 1:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        elif -1 < ShareOfGames[i] - Standard_CH[i] < 0:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    for i, txt in enumerate(Standard_CH):
        if 0 < Standard_CH[i] - ShareOfGames[i] < 1:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        elif -1 < Standard_CH[i] - ShareOfGames[i] < 0:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    #Titel og Akser
    plt.yticks(my_range, dfGraph['Decks'])
    plt.xlabel('Pct. spillet')
    plt.ylabel('Deck')

def MixedEqLevelK(MixedEq_Decks, CHInput, frekvenser):

    Standard_CH = [i*100 for i in CHInput]
    count = 0
    NumberOfGames = []
    for i in frekvenser:
        NumberOfGames.append(sum(i)+i[count])
        count += 1 
    ShareOfGames = []
    for i in NumberOfGames:
        ShareOfGames.append(100 * i / sum(NumberOfGames))
    CombinedList = []
    for i in range(len(MixedEq_Decks)):
        CombinedList.append([MixedEq_Decks[i], ShareOfGames[i], Standard_CH[i]])
    dfGraph = pd.DataFrame(CombinedList, columns = ["Decks","Observationer", "Level-K"])
    my_range = range(1, len(dfGraph.index)+1)
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.hlines(y = my_range, xmin = dfGraph['Observationer'], xmax = dfGraph['Level-K'], color='peru', alpha = 0.4)
    plt.scatter(dfGraph['Observationer'], my_range, color='deepskyblue', alpha=1, label='Observationer')
    plt.scatter(dfGraph['Level-K'], my_range, color='khaki', alpha=1, label='Level-K Model')
    plt.legend()
    textcordy = 7
    textcordx = 0
    for i, txt in enumerate(ShareOfGames):
        if 0 < ShareOfGames[i] - Standard_CH[i] < 1:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        elif -1 < ShareOfGames[i] - Standard_CH[i] < 0:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (ShareOfGames[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    for i, txt in enumerate(Standard_CH):
        if 0 < Standard_CH[i] - ShareOfGames[i] < 1:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx+8,textcordy),ha='center',fontsize=8)
        elif -1 < Standard_CH[i] - ShareOfGames[i] < 0:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx-8,textcordy),ha='center',fontsize=8)
        else:
            ax.annotate("{:.1f}".format(txt), (Standard_CH[i], my_range[i]),textcoords='offset points',xytext=(textcordx,textcordy),ha='center',fontsize=8)
    #Titel og Akser
    plt.yticks(my_range, dfGraph['Decks'])
    plt.xlabel('Pct. spillet')
    plt.ylabel('Deck')