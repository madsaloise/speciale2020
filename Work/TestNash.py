import numpy as np
import pandas as pd
import string
from sympy import symbols, Eq, solve
from DataPrep import ImportExcelFile 
#Syntax:
# ImportExcelFile(Kolonner, Rækker, dataframe) 
# Det, som man gerne vil gemme fra funktionen angives som 1, de andre som 0
# Vælger man flere med et vil den bare returnere kolonnenavnene 

deck_names = ImportExcelFile(1,0,0)
winrates = ImportExcelFile(0,1,0)
data = ImportExcelFile(0,0,1)
payoffs = [[u for u in [(j/50.0)-1 for j in i]] for i in winrates]
print(len(deck_names))
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o = symbols('a, b, c, d, e, f, g, h, i, j, k, l, m, n, o')
eq1 = sm.Eq(50*a + 56.5*b + 54.4*c + 51.6*d + 38.9*e + 49.4*f + 57.1*g + 61*h + 49.1*i + 60.2*j + 58.6*k + 51.8*l + 56.6*m + 56.3*n + 45.1*o)
eq2 = sm.Eq(43.5*a + 50*b + 50.8*c + 46.7*d + 48.2*e + 51.7*f + 56.3*g + 42.4*h + 50*i + 65.7*j + 42.3*k + 56.1*l + 44.6*m + 55.7*n + 55.3*o)
eq3 = sm.Eq(45.6*a + 49.2*b + 50*c + 51.8*d + 49.1*e + 53.5*f + 53.4*g + 50.2*h + 43.8*i + 51.3*j + 49.9*k + 55.2*l + 43.6*m + 50.8*n + 53*o)
eq4 = sm.Eq(48.4*a + 53.3*b + 48.2*c + 50*d + 42.4*e + 46.4*f + 54.5*g + 32.6*h + 56.2*i + 62.5*j + 43*k + 49.3*l + 48.3*m + 50.4*n + 47.2*o)
eq5 = sm.Eq(61.1*a + 51.8*b + 50.9*c + 57.6*d + 50*e + 54.5*f + 51.9*g + 68.6*h + 64.9*i + 43.2*j + 70.1*k + 52.5*l + 56.7*m + 52.6*n + 48.2*o)
eq6 = sm.Eq(50.6*a + 48.3*b + 46.5*c + 53.6*d + 45.5*e + 50*f + 49.4*g + 50.3*h + 47.6*i + 43.6*j + 48.2*k + 51.3*l + 54.3*m + 49.7*n + 52.5*o)
eq7 = sm.Eq(42.9*a + 43.7*b + 46.6*c + 45.5*d + 48.1*e + 50.6*f + 50*g + 47.5*h + 43.9*i + 47.6*j + 49.5*k + 53.1*l + 38.5*m + 44.8*n + 52.2*o)
eq8 = sm.Eq(39*a + 57.6*b + 49.8*c + 67.4*d + 31.4*e + 49.7*f + 52.5*g + 50*h + 65.6*i + 44.7*j + 52.2*k + 48.1*l + 55.1*m + 46.5*n + 37.5*o)
eq9 = sm.Eq(50.9*a + 50*b + 56.2*c + 43.8*d + 35.1*e + 52.4*f + 56.1*g + 34.4*h + 50*i + 65.6*j + 36.4*k + 53.8*l + 53.8*m + 62.5*n + 39.8*o)
eq10 = sm.Eq(39.8*a + 34.3*b + 48.7*c + 37.5*d + 56.8*e + 56.4*f + 52.4*g + 55.3*h + 34.4*i + 50*j + 54.9*k + 55.8*l + 54.6*m + 56.3*n + 55.6*o)
eq11 = sm.Eq(41.4*a + 57.7*b + 50.1*c + 57*d + 29.9*e + 51.8*f + 50.5*g + 47.8*h + 63.6*i + 45.1*j + 50*k + 57*l + 47.8*m + 61.3*n + 39.5*o)
eq12 = sm.Eq(48.2*a + 43.9*b + 44.8*c + 50.7*d + 47.5*e + 48.7*f + 46.9*g + 51.9*h + 46.2*i + 44.2*j + 43*k + 50*l + 42.2*m + 48.2*n + 52.2*o)
eq13 = sm.Eq(43.4*a + 55.4*b + 56.4*c + 51.7*d + 43.3*e + 45.7*f + 61.5*g + 44.9*h + 46.2*i + 45.4*j + 52.2*k + 57.8*l + 50*m + 50.7*n + 43.2*o)
eq14 = sm.Eq(43.7*a + 44.3*b + 49.2*c + 49.6*d + 47.4*e + 50.3*f + 55.2*g + 53.5*h + 37.5*i + 43.7*j + 38.7*k + 51.8*l + 49.3*m + 50*n + 51.6*o)
eq15 = sm.Eq(54.9*a + 44.7*b + 47*c + 52.8*d + 51.8*e + 47.5*f + 47.8*g + 62.5*h + 60.2*i + 44.4*j + 60.5*k + 47.8*l + 56.8*m + 48.4*n + 50*o)
