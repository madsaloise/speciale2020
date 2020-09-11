import seaborn as sns

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from scipy.optimize import linprog


def solvemixednash(decks, winrates):

    num_decks=len(decks)

    # maximize the new variable c

    c = [0 for i in range(num_decks)]

    c.append(1)

    # calculate the payoff matrix from win percentages

    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]

    # append a column of -1s to subtract z from each upper bound constraint 

    for r in payoffs:

        r.append(-1.0)

    # inequality constraint right hand sides

    b_ub = [0 for i in range(num_decks)]

    # setup equality constraint so x forms a probability distribution

    ones = [1 for i in range(num_decks)]

    ones.append(0)

    A_eq = [ones]

    # the x add up to 1

    b_eq = [1]

    # x and z must be non-negative

    bounds = [(0,None) for i in range(num_decks+1)]

    solution = linprog(c, A_ub=payoffs, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

    return zip(decks,solution['x'])

'''if __name__ == '__main__':

    print(list(solvemixednash(decks, winrates)))'''