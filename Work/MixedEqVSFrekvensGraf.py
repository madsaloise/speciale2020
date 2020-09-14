import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def format(l):
    return "["+", ".join(["%.2f" % x for x in l])+"]"

def MixedEqGraph(Vores_Nash, frekvenser):
    #Splitter tuple
    MixedEq = list(Vores_Nash)
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
    
    plt.hlines(y = my_range, xmin = dfGraph['Observationer'], xmax = dfGraph['Nash'], color='grey', alpha = 0.4)
    plt.scatter(dfGraph['Observationer'], my_range, color='navy', alpha=1, label='Observationer')
    plt.scatter(dfGraph['Nash'], my_range, color='gold', alpha=1, label='Nash')
    plt.legend()
    '''
    for x,y in zip(ShareOfGames,MixedEq_Winrates):
        label = "{:.2f}".format(y)
        # this method is called for each point
        plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,-1), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
    '''
    #Titel og Akser
    plt.yticks(my_range, dfGraph['Decks'])
    plt.title("Nash VS Frekvens")
    plt.xlabel('Pct. spillet')
    plt.ylabel('Deck')
    plt.show()
    '''
    labels = MixedEq_Decks
    a_values = ShareOfGames
    b_values = MixedEq_Winrates

    # Create the figure
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for i in list(range(len(labels))):
        # Plot the line between dumbbells
        ax.plot([a_values[i], b_values[i]], [i, i], color='black')
        # Plot the dumbbells.
        ax.plot(a_values[i], i, color='red', marker='o', markersize=15)
        ax.plot(b_values[i], i, color='blue', marker='o', markersize=15)
        # Add data label on top of dumbbells
        ax.text(a_values[i], i, a_values[i], horizontalalignment='center', verticalalignment='center', color='white')
        ax.text(b_values[i], i, b_values[i], horizontalalignment='center', verticalalignment='center', color='white')
        # Add the axis label
        ax.text(3, i, labels[i], horizontalalignment='right', verticalalignment='center', fontsize=12)

    # Adjust and show the plot
    fig.subplots_adjust(left=0.3)
    ax.set_axis_off()
    plt.show()
    '''

    
    
    