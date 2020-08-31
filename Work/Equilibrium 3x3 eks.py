
import seaborn as sns

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from scipy.optimize import linprog



decks = ["Highlander Mage", "Mech Paladin","Ressurect Priest"]


# winrates for each deck from the tempostorm website

winrates = [[50,46,56],

            [54,50,40],

            [44,60,50]]


def solve(decks, winrates):


    num_decks=len(decks)



    
    c = [0 for i in range(num_decks)]

    c.append(1)



    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]



    for r in payoffs:

        r.append(-1.0)

    print(payoffs)

    

    b_ub = [0 for i in range(num_decks)]



    

    ones = [1 for i in range(num_decks)]

    

    ones.append(0)

    A_eq = [ones]

    

    b_eq = [1]

    

    bounds = [(0,None) for i in range(num_decks+1)]

    solution = linprog(c, A_ub=payoffs, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

    return zip(decks,solution['x'])


if __name__ == '__main__':

    print(list(solve(decks, winrates)))