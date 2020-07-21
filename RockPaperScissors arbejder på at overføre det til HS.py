import nashpy as nash
import numpy as np
Awinrates = [[50,50,45,75,55,45,40,65,60,35,70,60],

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
            
B = np.negative(A)
rps = nash.Game(A, B)
(print(rps))

#If row player only plays scissor and column player only plays paper
sigma_r = [0, 0, 1]
sigma_c = [1, 0, 0]
print(f'If player r plays scissors and player c plays paper, the payoff is: {rps[sigma_r, sigma_c]}')

sigma_c = [1 / 2, 0, 1 / 2]
print(f'If player c mixes between playing rock and paper, the payoff is: {rps[sigma_r, sigma_c]}')


sigma_r = [0, 1 / 2, 1 / 2]
print(f'If player r mixes between playing paper and scissor, whilst player c is still mixing, the payoff is: {rps[sigma_r, sigma_c]}')

eqs = rps.support_enumeration()
print(f'The nash equilibrium is: {list(eqs)}')

