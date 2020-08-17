''' hs_gto.py



Calculates a game theory optimal deck selection strategy for hearthstone laddering. 

Utilities in the payoff matrix are based on win-rates from the tempostorm website '''

import seaborn as sns

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from scipy.optimize import linprog



decks = ["Mid-range Druid", "Token Druid", "Mid-range Hunter",

         "Freeze Mage", "Mech Mage", "Secret Paladin", 

         "Dragon Priest", "Handlock", "Demon Handlock", 

         "Zoolock", "Control Warrior", "Patron Warrior"]



# winrates for each deck from the tempostorm website

winrates = [[50,50,45,75,55,45,40,65,60,35,70,60],

            [50,50,40,60,55,40,35,55,60,40,75,40],

            [55,60,50,35,40,35,40,50,65,45,55,30],

            [25,40,65,50,30,70,70,70,70,80,10,20],

            [45,45,60,70,50,70,40,60,40,30,35,55],

            [55,60,65,30,30,50,50,45,35,55,60,30],

            [60,65,60,30,60,50,50,20,25,70,40,50],

            [35,45,50,30,40,55,80,50,45,65,60,55],

            [40,40,35,30,60,65,75,55,50,60,60,65],

            [65,60,55,20,70,45,30,35,40,50,60,40],

            [30,25,45,90,65,40,60,40,40,40,50,60],

            [40,60,70,80,45,70,50,45,35,60,40,50]]


def solve(decks, winrates):

    '''find an optimal strategy based on the given deck winrates.

    the number of decks must match the number of rows/columns in winrates'''

    num_decks=len(decks)



    # maximize the new variable z

    c = [0 for i in range(num_decks)]

    c.append(1)



    # calculate the payoff matrix from win percentages

payoffs=[]
for u in j:
    [(j/50.0)-1]
    for j in i:
        for i in winrates:
            payoffs.append(u)

    # append a column of -1s to subtract z from each upper bound constraint 

    for r in payoffs:

        r.append(-1.0)



    # inequality constraint right hand sides

    b_ub = [0 for i in range(num_decks)]



    # setup equality constraint so x forms a probability distribution

    ones = [1 for i in range(num_decks)]

    # leave z out of this formula

    ones.append(0)



    A_eq = [ones]

    # the x add up to 1

    b_eq = [1]



    # x and z must be non-negative

    bounds = [(0,None) for i in range(num_decks+1)]



    solution = linprog(c, A_ub=payoffs, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

    return zip(decks,solution['x'])


if __name__ == '__main__':

    print(list(solve(decks, winrates)))