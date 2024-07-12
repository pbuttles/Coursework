# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 20:30:55 2020

@author: pbuttles
"""

# HW6 Problem 2 template file -- replace with your name here

#--Do not modify below this line--#
import numpy as np

# this function inputs an nxn matrix "Ainput" and an nx1 column matrix "binput"
# inputs should be floating-point type
# it performs Gaussian elimination and outputs the eliminated new matrices A and b
# where "A" is nxn upper triangular, and "b" is an nx1 column matrix
def LUdecomp(Ainput):
    n=len(Ainput[0]) # finds the dimension of the nxn matrix
    L = np.zeros((n,n)) # creates an nxn matrix of zeros to initialize the L matrix
    for k in range(n): # puts 1's along the diagonal of the L matrix
        L[k][k] = 1
    U = Ainput.copy() # make copies so as not to write over originals
    # loop over pivot rows from row 1 to row n-1 (i to n-2)
    for i in range(0,n-1):
        # loop over row to be zero'ed from row j+1 to n (j+1 to n-1)
        for j in range(i+1,n):
            c = U[j,i]/U[i,i] # multiplicative factor to zero point
            U[j,i] = 0.0 # we know this element goes to zero
            U[j,i+1:n]=U[j,i+1:n]-c*U[i,i+1:n] # do subtraction of two rows
            L[j][i] = c # stores the computed value of c in its respective spot, fully generating L
    return (L,U)  # return modified A and b

#---Do not modify above this line--#

A1 = np.array([[4,-2,1],[-3,-1,4],[1,-1,3]], dtype=float) # given in problem 2
A2 = np.array([[2,4,3,3],[2,2,3,2],[6,-1,3,3],[6,1,-6,-5]],dtype=float) #given in problem 2

[L,U] = LUdecomp(A1) # passes A1 into LUdecomp, stores L and U
res = A1 - np.dot(L,U) # calculates the residual of A1 and L*U
print(res)

[L,U] = LUdecomp(A2) # passes A2 into LUdecomp, stores L and U
res = A2 - np.dot(L,U) # calculates the residual of A2 and L*U
print(res)