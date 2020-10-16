import matplotlib.pyplot as plt
from RunAll import RunAll
from CHModelBetaDistAfrund import CHSolveAfrund
from CHModelBetaDist import CHSolve
from MixedEquilibriumWinrates import solvemixednash
from DataPrep import ImportExcelFile 
from DataPrep import ImportFrekvenser 
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe, Path) 
# ImportFrekvenser(Path)
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0. Stien angives med R'Sti.xlsx'
# Vælger man flere input med 1 vil den bare returnere kolonnenavnene, just dont 


#Winrates Data
PathWin = r'C:\speciale2020\Data\Winrates_Data_2_169.xlsx'
#Frekvens Data
PathFrek = r'C:\speciale2020\Data\Frekvenser_169.xlsx'

deck_names = ImportExcelFile(1,0,0, PathWin)
winrates = ImportExcelFile(0,1,0, PathWin)
data = ImportExcelFile(0,0,1, PathWin)
frekvenser = ImportFrekvenser(PathFrek)

print(CHSolve(deck_names, winrates, 2, 0.15025539, 0.86047883, 1, MLE = 0))
#print(CHSolve(deck_names, winrates, 5, 0.5, 0.5, 1, MLE = 0))
'''
from DumbellPlot import MixedEqGraph
# Syntax: MixedEqGraph(Vores_Nash, Frekvenser)
from LeastSquares_Beta import OptLS_Standard
OptLS_Standard(deck_names, winrates, frekvenser, 6)

MixedEqGraph(solvemixednash(deck_names, winrates, 1), frekvenser,CHSolve(deck_names, winrates, 10, 0.2, 0.5, 0, MLE = 1), CHSolveAfrund(deck_names, winrates, 10, 0.2, 0.5, 0, MLE = 1) )
plt.show()

winratespath = r'C:\speciale2020\Data\Winrates_Data_2_169.xlsx'
frequenciespath = r'C:\speciale2020\Data\Frekvenser_169.xlsx'


RunAll(winratespath, frequenciespath)

plt.show()


#For legend er tau 0.17
#Under legen er tau 0.055
'''