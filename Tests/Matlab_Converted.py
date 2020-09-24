import pandas as pd
import numpy as np
import scipy as sp
from scipy.stats import chisquare
import matplotlib.pyplot as plt
from math import factorial
from math import exp
import scipy
import statsmodels   
#import torch as tc

def CogHierSol(winrates,tau,levels):
    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
    numactions = []
    for i in range(levels):
        numactions.append(len(payoffs))

    # Determine number of players in the game
    numplayers=np.size(payoffs,1)
    # Determine number of actions avail to each player
    for player in np.arange(1,numplayers).reshape(-1):
        numactions[player]=np.size(payoffs,player + 1)
    
    #Build Index array for the normal form game
    Indexarray=np.array(1,np.ndim(payoffs))
    numpayoffcells=tc.numel(payoffs)
    # Determine true probability of a player being step k
    fk = []
    for k in np.arange(0,levels).reshape(-1):
        if k < levels:
            fk.append((np.dot(exp(- tau),tau ** k)) / factorial(k))
        else:
            fk.append(1 - sum(fk))
    
# Build strategy matrix for each player using k steps. Each row represents
# a k level of thought (row 1 corresponds to 0 steps, row n with n-1 steps)
# and each column value is an action. Thus, each row sums to 1.
    # Calculate player strategies when using each step k (0 to levels)

    for k in np.arange(0,levels).reshape(-1):
        for player in np.arange(1,numplayers).reshape(-1):
            #Initialize for random level 0 thinkers
            if k == 0:
                for q in np.arange(1,numactions).reshape(-1):
                    strategy[player][k + 1,q]= 1 / sum(numplayers)
            # Determine exp value of playing each strategy under k-level of thought
            if k > 0:
                #Zero out exp payoff for actions
                exppayoffperaction=zeros(1,numactions(player))
                for opplvl in np.arange(1,k).reshape(-1):
                    denom=sum(fk(np.arange(1,k)))
                    opponents=np.arange(1,numplayers)
                    opponents[player]=[]
                    #payoff occurs
                    for cellnum in np.arange(1,numpayoffcells).reshape(-1):
                        #Determine actions of all players for cell index
                        Indexarray[np.arange()]=ind2sub(size(payoffs),cellnum)
                        cellindex=cell2mat(Indexarray)
                        if cellindex(1) == player:
                            #Probability of each player action in the Indexarray
                            probidx=1
                            for otherplayer in opponents.reshape(-1):
                                probabilityplay[probidx]=strategy[otherplayer](opplvl,cellindex(otherplayer + 1))
                                probidx=probidx + 1
                            #Probability payoff occurs given other player's strats
                            probofcell=np.dot((fk(opplvl) / denom),prod(probabilityplay))
                            exppayoffperaction[cellindex(player + 1)]=exppayoffperaction(cellindex(player + 1)) + np.dot(probofcell,payoffs(cellnum))
                # Find best strategy to play
                maxval=max(exppayoffperaction)
                idx=find(exppayoffperaction == maxval)
                for q in np.arange(1,numactions(player)).reshape(-1):
                    if ismember(q,idx) == 1:
                        strategy[player][k + 1,q]=1 / length(idx)
                    else:
                        strategy[player][k + 1,q]=0
            clear('exppayoffperaction','probofcell','probabilityplay')
            #Translate to probs of playing via Poisson rate
            rateofplay[player][k + 1,np.arange()]=np.dot(fk(k + 1),strategy[player](k + 1,np.arange()))
    
    #Record final CH values of play
    
    for player in np.arange(1,numplayers).reshape(-1):
        for action in np.arange(1,numactions(player)).reshape(-1):
            accumulator=0
            for levelthought in np.arange(1,levels + 1).reshape(-1):
                accumulator=accumulator + rateofplay[player](levelthought,action)
            CHsolution[player][action]=accumulator
    
    return CHsolution
    
if __name__ == '__main__':
    pass
    