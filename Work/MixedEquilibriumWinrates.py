import numpy as np
from scipy.optimize import linprog

def solvemixednash(decks, winrates, GrafData):

    num_decks=len(decks)

    # Maximer c

    c = [0 for i in range(num_decks)]

    c.append(1)

    # Beregn payoff

    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
    # append -1 til brug for øvre grænse
    
    for r in payoffs:

        r.append(-1.0)

    # højreside-grænse

    b_ub = [0 for i in range(num_decks)]

    # equality constraint

    ones = [1 for i in range(num_decks)]

    ones.append(0)

    A_eq = [ones]

    # x summerer til 1

    b_eq = [1]

    # x og c must skal være positive

    bounds = [(0,None) for i in range(num_decks+1)]

    solution = linprog(c, A_ub=payoffs, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

    if GrafData == 0:
        MixedStrat = [(i,j) for i,j in zip(decks,solution['x']) if j != 0]
        return MixedStrat
    else:
        return zip(decks,solution['x'])
    

