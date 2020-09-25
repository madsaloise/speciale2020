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

from DataPrep import ImportExcelFile 
from DataPrep import ImportFrekvenser 
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe, Path) 
# ImportFrekvenser(Path)
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0. Stien angives med R'Sti.xlsx'
# Vælger man flere input med 1 vil den bare returnere kolonnenavnene, just dont 

#Winrates Data
PathWin = r'C:\Users\vodst\OneDrive\Bærbar\Polit\Kandidat\KU\E20 - Speciale\Github\speciale2020\Data\Winrates_Data_2.xlsx'
#Frekvens Data
PathFrek = r'C:\Users\vodst\OneDrive\Bærbar\Polit\Kandidat\KU\E20 - Speciale\Github\speciale2020\Data\Frekvenser.xlsx'

deck_names = ImportExcelFile(1,0,0, PathWin)
winrates = ImportExcelFile(0,1,0, PathWin)
data = ImportExcelFile(0,0,1, PathWin)
frekvenser = ImportFrekvenser(PathFrek)
from MixedEquilibriumWinrates import solvemixednash
MixedEqGraph(solvemixednash(deck_names, winrates, 1), frekvenser)   
    
    