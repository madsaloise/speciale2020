import numpy as np


#Lige pt. tjekker den kun på tværs
def ElimineringDomStrat(deck_names, winrates):
    count = 0
    DomineredeStrat = []
    P2Winrates = np.array(winrates)
    for j in range(len(deck_names)-1):
        for i in winrates[:-1]:
            PlusEn = count+1
            if all(P2Winrates[count,:] <= P2Winrates[PlusEn,:]) and any(P2Winrates[count,:] < P2Winrates[PlusEn,:]):
                DomineredeStrat.append(count)
                print("Række" + str(count) + "er svagt domineret af" + str(PlusEn))
            PlusEn += 1
        count += 1
    if not DomineredeStrat:
        print("Ingen svagt dominerede strategier")



