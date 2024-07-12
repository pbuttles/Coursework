# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 23:12:58 2023

@author: pbuttles
"""

import numpy as np

N = {'-45':{'-22.5':70*10,'22.5':47*10,'67.5':5*10,'112.5':43.8*10},
        '0':{'-22.5':115*10,'22.5':7.1*10,'67.5':1.89*10,'112.5':73.63*10},
        '45':{'-22.5':45.2*10,'22.5':2.8*10,'67.5':13*10,'112.5':29.1*10},
        '90':{'-22.5':5.7*10,'22.5':7.6*10,'67.5':33.6*10,'112.5':11.2*10}}
print("Sandro data")

'''
N = {'-45':{'-22.5':842,'22.5':212,'67.5':302,'112.5':836},
        '0':{'-22.5':891,'22.5':869,'67.5':173,'112.5':261},
        '45':{'-22.5':255,'22.5':830,'67.5':814,'112.5':221},
        '90':{'-22.5':170,'22.5':259,'67.5':969,'112.5':846}}
print("Paper data")
'''

a = -45
aprime = 0
b = -22.5
bprime = 22.5

global sigmaS
sigmaS = 0

def E(a,b):
    global sigmaS
    ap = a+90
    bp = b+90
    print("a = " + str(a) + ", b = " + str(b))
    #print(N[str(a)][str(b)])
    #print(N[str(ap)][str(bp)])
    #print(N[str(a)][str(bp)])
    #print(N[str(ap)][str(b)])
    num = N[str(a)][str(b)]+N[str(ap)][str(bp)]-N[str(a)][str(bp)]-N[str(ap)][str(b)]
    denom = N[str(a)][str(b)]+N[str(ap)][str(bp)]+N[str(a)][str(bp)]+N[str(ap)][str(b)]
    Eab = num/denom
    dSdN1 = (1)/(denom) - (num)/(denom**2)
    dSdN2 = (-1)/(denom) - (num)/(denom**2)
    dSdN3 = (-1)/(denom) - (num)/(denom**2)
    dSdN4 = (1)/(denom) - (num)/(denom**2)
    sigmaS += (N[str(a)][str(b)]*dSdN1**2 + N[str(a)][str(bp)]*dSdN2**2 + N[str(ap)][str(b)]*dSdN3**2 + N[str(ap)][str(bp)]*dSdN4**2)
    print("E(a,b) = " + str(Eab))
    print("")
    return Eab

S = E(a,b) + E(a,bprime) + E(aprime,b) - E(aprime,bprime)
print("S:")
print(S)

sigmaS = np.sqrt(sigmaS)
print(sigmaS)

    
    
    
    
    
    
    
    
    