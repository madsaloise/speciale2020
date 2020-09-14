import matplotlib as plt
import numpy as np

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


    
    
    