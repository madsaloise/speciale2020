def RunAll(winratespath, frequenciespath):
    #Imports
    import numpy as np
    import pandas as pd
    from scipy.optimize import linprog
    import matplotlib.pyplot as plt
    #Importerer DataPrep
    from DataPrep import ImportExcelFile 
    from DataPrep import ImportFrekvenser 
    #Syntax:
    # ImportExcelFile(Kolonner, Rækker, dataframe, Path) 
    # ImportFrekvenser(Path)
    # Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0. Stien angives med R'Sti.xlsx'
    # Vælger man flere input med 1 vil den bare returnere kolonnenavnene, just dont 


    #Winrates Data
    PathWin = winratespath
    #Frekvens Data
    PathFrek = frequenciespath

    deck_names = ImportExcelFile(1,0,0, PathWin)
    winrates = ImportExcelFile(0,1,0, PathWin)
    data = ImportExcelFile(0,0,1, PathWin)
    frekvenser = ImportFrekvenser(PathFrek)

    #Dominans, Syntax: ElimineringDomStrat(deck, winrates)
    from ElimineringDomineredeStrat import ElimineringDomStrat
    ElimineringDomStrat(deck_names, winrates)

    #Importerer Nash
    #Syntax: solvemixednash(decks, winrates)
    from MixedEquilibriumWinrates import solvemixednash
    #Printer
    print("Optimal sammensætning af deck i et mixed-nash equilibrium er: " + str(solvemixednash(deck_names, winrates, 0)) + ". Andre decks spilles med en sandsynlighed på 0.")
    #Level-K Model, 

    tau = 0.14285714285714285
    tau_levelk = 0.12244897959183673
    level = 5
    #Syntax: levelksolve(decks, winrates, levels), level 0 antages at spille uniformt. For k spillere skrives levels som k-1.
    from LevelKModelTeori import levelksolve
    print(list(levelksolve(deck_names, winrates, level-1)))
    from LevelKModelPoisson import levelksolvepoisson

    print(levelksolvepoisson(deck_names, winrates, level, tau_levelk))

    #CH Model, syntax: CHSolve(decks, winrates, levels, kommentarer, tau = 0.5):, level 0 antages at spille uniformt. 
    #"Kommentarer" skal være en, hvis man vil se sandsynligheder og payoffs, 0 ellers.
    #from MLEEstimation import MLEPlot
    from CHModelAfrundingTester import CHSolveAfrund
    from CHModel import CHSolve

    #MLEPlot(12, 8)
    print(CHSolve(deck_names, winrates, level, 0, tau, 0))
    print(CHSolveAfrund(deck_names, winrates, level, 0, tau, 0))


    from DumbellPlot import MixedEqGraph
    # Syntax: MixedEqGraph(Vores_Nash, Frekvenser)
    MixedEqGraph(solvemixednash(deck_names, winrates, 1), frekvenser,CHSolve(deck_names, winrates, level+1, 0, tau, 1), CHSolveAfrund(deck_names, winrates, level+1, 0, tau, 1) )

    from LeastSquares import OptLS_Standard

    OptLS_Standard(deck_names, winrates, frekvenser, level+1)

