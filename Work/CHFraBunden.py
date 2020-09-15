import numpy as np

def CHSolve(decks, winrates, levels):
    num_decks=len(decks)
    #Beregner gennemsnitlige payoffs
    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
    avg_payoff=[]
    for i in payoffs:
        avg_pay = sum(i)/num_decks
        avg_payoff.append(avg_pay)

    #Laver normal_form game til højere CH-Levels
    normal_form_game = [[u for u in [[j, 100-j] for j in i]] for i in payoffs]

    ###LEVEL 0###
    level_0_maxpayoff = max(avg_payoff)
    level_0_index = avg_payoff.index(level_0_maxpayoff)

    ###LEVEL 1###
    maks_index = []
    deckID = [level_0_index]
    for i in payoffs:
        maks_index.append(payoffs[level_0_index])
    deckID.append(np.argmin(maks_index))
    level_0_index = np.argmin(maks_index)
    maks_index = []
    return deckID

