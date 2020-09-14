import numpy as np

def CHSolve(decks, winrates, levels):
    
    num_decks=len(decks)
    '''/DONE'''
    #Beregner gennemsnitlige payoffs
    payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
    avg_payoff=[]
    for i in payoffs:
        avg_pay = sum(i)/num_decks
        avg_payoff.append(avg_pay)
    #Indsætter player 0's valg i en liste
    level_0_maxpayoff = max(avg_payoff)
    level_0_index = avg_payoff.index(level_0_maxpayoff)
    

    #Lister 
    range_level = []
    maxIDlist = []
    #Gør det nemmere at vælge et tilfældigt level som højeste level som del af programmet. For k niveauer angives k-1 niveauer.
    for i in range(levels):
        range_level.append(i)
    
    #TODO: Inkluder vægte
    maks_index = []
    deckID = [level_0_index]
    count = 0
    for p in enumerate(range_level):
        weights = 1/(count+2)
        if count == 0:
            for i in payoffs:
                maks_index.append(payoffs[level_0_index])
            deckID.append(np.argmin(maks_index))
            level_0_index = [np.argmin(maks_index)]
            maks_index = [] 
        else: 
            for i in payoffs:
                #Finder payoffs for hvert af decks, som spiller h spiller. level_0_indeks burde nok være en liste efterhånden?    
                for j in enumerate(deckID):
                    maks_index.append(payoffs[level_0_index.index(j)])
            #TODO: Det her skal vægtes og laves om til best-response funktion
            for q in maks_index:
                maxIDlist.append(np.argmin(maks_index.index(q)))
            deckID.append(maxIDlist)
            level_0_index = maxIDlist
            maxIDlist = []
            maks_index = []
        count += 1
    print(deckID)
    #Danner en liste med forskellige spilleres valg
    counter=0
    plays = []
    print("I CH-model har vi følgende:")
    for i in deckID:
        ilevel_k = counter
        deckIDcounter = deckID[ilevel_k]
        leveliplay = decks[deckIDcounter]
        plays.append("Level-" + str(counter+1) + " spiller: "+ str(leveliplay) + " med sandsynlighederne" '''+ str(PlayWeights)''')
        counter += 1
    return plays
