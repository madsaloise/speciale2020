
#Importerer DataPrep
from DataPrep import ImportExcelFile 
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe) 
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0
# Vælger man flere med et vil den bare returnere kolonnenavnene 

column_names = ImportExcelFile(1,0,0)
row_names = ImportExcelFile(0,1,0)
data = ImportExcelFile(0,0,1)
print(column_names)
print(row_names)