# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 20:18:20 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

n = 100 # initializing n=100 for nxn matrix
h = (2*np.pi)/n # dividing the 0 to 2pi interval into 100 evenly spaced segments yields step size h
A = np.zeros([n,n]) # initializes nxn matrix A
for i in range(n):
    A[i][i] = -2 # writes -2 along the diagonal 
    for j in range(n):
        if j == i + 1:
            A[i][j] = 1 # writes 1 along the line directly below the diagonal
            A[j][i] = 1 # writes 1 along the line directly above the diagonal
A[0][n-1] = 1 # adds endpoint for periodic behavior
A[n-1][0] = 1 # adds endpoint for periodic behavior
A = A * (1/h**2) # divide by 1/h^2 term from taylor expansion
         
b = np.zeros([n,1]) # initializes b vector of length n
for i in range(n):
    b[i] = -4*np.pi*np.sin(i*h) # computes -4pirho(xi) for i=0,n-1 and writes to b vector

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

x = np.arange(0,n*h,h) # creates mesh to be plotted over

iterativeSolution = myJacobi(A,b,1,10**(-4)) # computes iterative solution using Jacobi method

analyticalSolution = [] # initializes list for analytical solution
for i in range(n):
    analyticalSolution.append(4*np.pi*np.sin(i*h)) # calculates the found analytical solution for rho(xi) from i=0 to n-1, appends to list

directInverse = np.linalg.inv(A)@b # computes x= Ainv*b as direct inverse solution

plt.plot(x,iterativeSolution[1], label="iterative") # plots iterative solution
plt.plot(x,analyticalSolution, label="analytical") # plots analytical solution
plt.plot(x,directInverse, label="directinv") # plots direct inverse solution
plt.legend() #displays legend
plt.show()

