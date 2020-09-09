import nashpy as nash
import numpy as np
A = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
B = np.negative(A)
rps = nash.Game(A, B)
(print(rps))
'''
#If row player only plays scissor and column player only plays paper
sigma_r = [0, 0, 1]
sigma_c = [1, 0, 0]
print(f'If player r plays scissors and player c plays paper, the payoff is: {rps[sigma_r, sigma_c]}')

sigma_c = [1 / 2, 0, 1 / 2]
print(f'If player c mixes between playing rock and paper, the payoff is: {rps[sigma_r, sigma_c]}')


sigma_r = [0, 1 / 2, 1 / 2]
print(f'If player r mixes between playing paper and scissor, whilst player c is still mixing, the payoff is: {rps[sigma_r, sigma_c]}')
'''
eqs = rps.support_enumeration()
print(f'The nash equilibrium is: {list(eqs)}')

