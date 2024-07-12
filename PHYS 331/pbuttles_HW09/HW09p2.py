# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:54:48 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

def CreateSystem(kvec,mvec):
    n = len(mvec) # initializes n, the number of masses
    x = np.zeros([n,n]) # initializes the nxn x matrix
    x[0][0] = (-1*kvec[0]-kvec[1])/mvec[0] # computes x11 endpoint
    x[0][1] = kvec[1]/mvec[0] # computes x12 endpoint
    x[n-1][n-1] = (-1*kvec[n]-kvec[n-1])/mvec[n-1] # computes xnn endpoint
    x[n-1][n-2] = 1*kvec[n-1]/mvec[n-1] # computes xn(n-1) endpoint
    for i in range(1,n-1): # runs the general form for masses 2 through n-1
        x[i][i] = (-1*kvec[i]-kvec[i+1])/mvec[i] # computes the xii element from the spring diagram
        x[i][i-1] = kvec[i]/mvec[i] # computes the xi(i-1)th element from the spring diagram
        x[i][i+1] = kvec[i+1]/mvec[i] # computes the xi(i+1)th element  from the spring diagram
    return x

kvec = np.array([1,1,1]) # k1=k2=k3=1 as given
mvec = np.array([1,1]) # m1=m2=1 as given
print(np.linalg.eig(CreateSystem(kvec,mvec))) # computes eigenvalues and eigenvectors of 2 mass system

kvec = np.array([1,1,1,1]) # k1=k2=k3=k4=1 as given
mvec = np.array([1,1,1]) # m1=m2=m3=1 as given
print(np.linalg.eig(CreateSystem(kvec,mvec))) # computes eigenvalues and eigenvectors of 3 mass system

klattice = np.ones(1001) # creates kvec for 1001 spring constants where k=1
mlattice = np.zeros(1000) # initializes mvec for 1000 masses 
for i in range(len(mlattice)):
    if i % 2 == 0:
        mlattice[i] = 1 # for odd masses, m=1
    if i % 2 == 1:
        mlattice[i] = 1.5 # for even masses, m=1.5

bins = 50 # bin size of 50 chosen
LatticeEigenvalues = np.linalg.eig(CreateSystem(klattice,mlattice))[0] # indexes eigenvalues of the even m=1.5 lattice
plt.hist(LatticeEigenvalues,bins) # plots histogram of eigenvalues with bin size 50
plt.title("Histogram of Lattice Eigenvalues, even m = 1.5, bins = 50") # titles plot
plt.show()

klattice = np.ones(1001) # creates kvec for 1001 spring constants where k=1
mlattice = np.zeros(1000) # initializes mvec for 1000 masses 
for i in range(len(mlattice)):
    if i % 2 == 0:
        mlattice[i] = 1 # for odd masses, m=1
    if i % 2 == 1:
        mlattice[i] = 1.2 # for even masses, m=1.2

LatticeEigenvalues = np.linalg.eig(CreateSystem(klattice,mlattice))[0] # indexes eigenvalues of the even m=1.2 lattice
plt.hist(LatticeEigenvalues,bins) # plots histogram of eigenvalues with bin size 50
plt.title("Histogram of Lattice Eigenvalues, even m = 1.2, bins = 50") # titles plot
plt.show()