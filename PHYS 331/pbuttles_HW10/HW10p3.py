# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:24:04 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

def euclidNorm(A):
    norm = 0 # initializes norm count
    for i in range(len(A)):
        norm += A[i]**2 # sums squares of elements
    norm = np.sqrt(norm) # takes sqrt of sum of squares
    return norm

def myJacobi(A,b,w,tol):
    iters = 0 # initializes iteration counter to zero
    n = len(A) # initializes n as length of A
    D = np.zeros([n,n]) # initializes diagonal matrix D
    L = np.zeros([n,n]) # initializes lower triangular matrix L
    U = np.zeros([n,n]) # initializes upper triangular matrix U
    Dinv = np.zeros([n,n]) # initializes inverse diagonal matrix Dinv
    for i in range(n):
        D[i][i] = A[i][i] # creates diagonal matrix
        for j in range(n):
            if i>j:
                L[i][j] = A[i][j] # creates lower triangular matrix
            if i<j:
                U[i][j] = A[i][j] # creates upper triangular matrix
    for i in range(n):
        Dinv[i][i] = 1/D[i][i] # inverse of a diagonal matrix is just inverse of the elements, creates Dinv
    x0 = Dinv@b # establishes starting vector x0 as Dinv*b
    x1 = 0 # intializes x1 as 0 to start the while loop
    xdiff = x0 - x1 # computes difference in old and new vectors
    while euclidNorm(xdiff) > tol: # checks for |x0-x1|<tol break condition
        def g(x): # g(x) iterative method as given
            g = -Dinv@(L+U)@x + Dinv@b
            return g
        x1 = w*g(x0) + (1-w)*x0 # relaxes g(x) iterative method with relaxation factor w
        xdiff = x0 - x1 # recomputes xdiff for looping
        x0 = x1 # resets x0 to the new x for looping
        iters += 1 # increases iteration count
    return iters, x1 # returns the number of iterations and the final x vector

#this function exploits geometric symmetries of a square grid like was given,
#and produces a 2D second order differential operator matrix of arbitrary size nxn
def generateA(n):
    n2 = n**2
    A = np.zeros([n2,n2])
    for i in range(len(A)):
        A[i][i] = -4
        for j in range(len(A)):
            if np.abs(i - j) == n:
                A[i][j] = 1
            if np.abs(i - j) == 1 and (i+j+1) % (2*n) != 0:
                A[i][j] = 1
    return A

A = generateA(3) # generates 2D 2nd order diff operator for 3x3
b = np.array([0,0,-100,0,0,-100,-200,-200,-300]) # given b vector, with negative values adjusted from textbook

iters, j = myJacobi(A,b,1,10**(-4)) # iteratively solves laplace equation by jacobi method
J = []; j1 = []; j2 = []; j3 = [] # initializes lists for mapping
for i in range(3): # partitions values into 3 element lists
    j1.append(j[i])
    j2.append(j[i+3])
    j3.append(j[i+6])
J.append(j1);J.append(j2);J.append(j3) # recombines lists into one list
J = np.array(J) # converts to numpy array for plotting
print(J)
plt.imshow(J,cmap="hot") # plots heatmap of values