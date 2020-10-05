import matplotlib.pyplot as plt
from RunAll import RunAll


winratespath = r'C:\speciale2020\Data\Winrates_Data_2_169.xlsx'
frequenciespath = r'C:\speciale2020\Data\Frekvenser_169_UnderPlatinium.xlsx'
RunAll(winratespath, frequenciespath)

plt.show()


#For legend er tau 0.17
#Under legen er tau 0.055