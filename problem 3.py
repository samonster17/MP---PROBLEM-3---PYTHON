#Ppython program to check if two  
# to get unique values from list 
# using numpy.unique  
import numpy as np 
from numpy import linalg as LA
import warnings    
import pandas as pd

R = int(input("Enter the number of rows:")) 

print("Enter values (Rowwise): ")
a = []
b = []
for i in range(R):
     a = []
     for j in range(2):
         a.append(input())
     b.append(a)
x = np.array(b)
array = x.astype(np.float)
print("The array you entered is: ")
print(array)

xx = array[:, 0]
xi = xx.astype(np.float)
yy = array[:,1]
yi = yy.astype(np.float)

P1 = np.polyfit(xi, yi, 1)
F1 = np.polyval(P1, xi)
E1 = yi - F1
N1 = LA.norm(E1)

P2 = np.polyfit(xi, yi, 2)
F2 = np.polyval(P2, xi)
E2 = yi - F2
N2 = LA.norm(E2)

P3 = np.polyfit(xi, yi, 3)
F3 = np.polyval(P3, xi)
E3 = yi - F3
N3 = LA.norm(E3)

P4 = np.polyfit(xi, yi, 4)
F4 = np.polyval(P4, xi)
E4 = yi - F4
N4 = LA.norm(E4)

P5 = np.polyfit(xi, yi, 5)
F5 = np.polyval(P5, xi)
E5 = yi - F5
N5 = LA.norm(E5)

P6 = np.polyfit(xi, yi, 6)
F6 = np.polyval(P6, xi)
E6 = yi - F6
N6 = LA.norm(E6)

P7 = np.polyfit(xi, yi, 7)
F7 = np.polyval(P7, xi)
E7 = yi - F7
N7 = LA.norm(E7)

P8 = np.polyfit(xi, yi, 8)
F8 = np.polyval(P8, xi)
E8 = yi - F8
N8 = LA.norm(E8)

P9 = np.polyfit(xi, yi, 9)
F9 = np.polyval(P9, xi)
E9 = yi - F9
N9 = LA.norm(E9)

P10 = np.polyfit(xi, yi, 10)
F10 = np.polyval(P10, xi)
E10 = yi - F10
N10 = LA.norm(E10)

LNEVector = [N1, N2, N3, N4, N5, N6, N7, N8, N9, N10]
LeastNorm1 = np.sort(LNEVector)
LeastNorm = np.min(LeastNorm1)

if LeastNorm == N1:
    print('The Coefficients of the Polynomial Function are: ')
    print(P1)
elif LeastNorm == N2:
    print('The Coefficients of the Polynomial Function are: ')
    print(P2)
elif LeastNorm == N3:
    print('The Coefficients of the Polynomial Function are: ')
    print(P3)
elif LeastNorm == N4:
    print('The Coefficients of the Polynomial Function are: ')
    print(P4)
elif LeastNorm == N5:
    print('The Coefficients of the Polynomial Function are: ')
    print(P5)
elif LeastNorm == N6:
    print('The Coefficients of the Polynomial Function are: ')
    print(P6)
elif LeastNorm == N7:
    print('The Coefficients of the Polynomial Function are: ')
    print(P7)
elif LeastNorm == N8:
    print('The Coefficients of the Polynomial Function are: ')
    print(P8)
elif LeastNorm == N9:
    print('The Coefficients of the Polynomial Function are: ')
    print(P9)
else:
    print('The Coefficients of the Polynomial Function are: ')
    print(P10)