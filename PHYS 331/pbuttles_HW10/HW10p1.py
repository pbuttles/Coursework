# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 18:40:53 2020

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

# giant block of code just passing different matrices and vectors and printing to console
A1 = np.array([[1.01, 0.99],[0.99,1.01]])
b1 = np.array([2.0,2.0])
print("A1 iterations = " + str(myJacobi(A1,b1,1,10**(-4))[0]))
print("A1 jacobi = " + str(myJacobi(A1,b1,1,10**(-4))[1]))
print("A1 exact = " + str(np.linalg.inv(A1)@b1))
A2 = np.array([[1.5,0.5],[0.5,1.5]])
b2 = np.array([2.0,2.0])
print("A2 iterations = " + str(myJacobi(A2,b2,1,10**(-4))[0]))
print("A2 jacobi = " + str(myJacobi(A2,b2,1,10**(-4))[1]))
print("A2 exact = " + str(np.linalg.inv(A2)@b2))
A3 = np.array([[9,10,2],[1,6,3],[10,-1,2]])
b3 = np.array([7,8,1])
print("A3 iterations = " + str(myJacobi(A3,b3,0.34,10**(-4))[0]))
print("A3 jacobi = " + str(myJacobi(A3,b3,0.34,10**(-4))[1]))
print("A3 exact = " + str(np.linalg.inv(A3)@b3))

x = np.linalg.inv(A3)@b3 # computes the "true" solution
xjacobi = [] # initializes list of x vectors for each w
itercount = [] # initializes list of iteration counts for each w
for i in range(1,35):
    i = i*0.01
    jacobi = myJacobi(A3,b3,i,10**(-4)) # computes jacobi method solution at each mesh point
    itercount.append(jacobi[0]) # appends iteration count for solution at each mesh point to a list
    xjacobi.append(jacobi[1]) # appends xjacobi at each mesh point to a list

true_error = np.zeros([len(xjacobi)]) # initializes a numpy array for true error
for i in range(len(true_error)):
    true_error[i] = euclidNorm((x - xjacobi)[i]) # computes true error as |x-xjacobi| and indexes to array

w = np.arange(0.01,0.35,0.01) # creates mesh to be plotted over
plt.plot(w,true_error, label="true error") # creates plot of true error vs w
plt.hlines(10**(-4),0.01,0.35, label="tolerance=0.0001") # creates tol = 0.0001 reference line
plt.title("True Error vs. w") # titles plot
plt.legend() # creates legend
plt.show()
plt.plot(w,itercount) # creates plot of iteration count vs w
plt.title("Iterations vs. w") # titles plot
plt.show()