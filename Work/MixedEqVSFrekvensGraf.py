import matplotlib as plt
import numpy as np

def MixedEqGraph(Vores_Nash, frekvenser):
    MixedEq = list(Vores_Nash)
    MixedEq_Decks = []
    MixedEq_Winrates = []
    for a, b in MixedEq:
        MixedEq_Decks.append(a)
        MixedEq_Winrates.append(b)

    
    
    