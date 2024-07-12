# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 01:02:12 2020

@author: pbuttles
"""

# HW6 Problem 2 template file -- replace with your name here

#--Do not modify below this line--#
import numpy as np

# this function inputs an nxn matrix "Ainput" and an nx1 column matrix "binput"
# inputs should be floating-point type
# it performs Gaussian elimination and outputs the eliminated new matrices A and b
# where "A" is nxn upper triangular, and "b" is an nx1 column matrix
def GaussElimin(Ainput,binput):
    n=len(binput)
    A = Ainput.copy() # make copies so as not to write over originals
    b = binput.copy()
    # loop over pivot rows from row 1 to row n-1 (i to n-2)
    for i in range(0,n-1):
        # loop over row to be zero'ed from row j+1 to n (j+1 to n-1)
        for j in range(i+1,n):
            c = A[j,i]/A[i,i] # multiplicative factor to zero point
            A[j,i] = 0.0 # we know this element goes to zero
            A[j,i+1:n]=A[j,i+1:n]-c*A[i,i+1:n] # do subtraction of two rows
            b[j] = b[j]-c*b[i] # do substraction of b's as well
    return (A,b)  # return modified A and b

#---Do not modify above this line--#

A1 = np.array([[4,-2,1],[-3,-1,4],[1,-1,3]], dtype=float) # given A1
b1 = np.array([15,8,13], dtype=float) # given b1

GaussElimin1 = GaussElimin(A1,b1) # passes A1 and b1 into GaussElimin
A1out = GaussElimin1[0] # stores the A1 output
b1out = GaussElimin1[1] # stores the b1 output
print("A1out = " + str(A1out));print("b1out = " + str(b1out))


x1_out = np.linalg.solve(A1out,b1out) # solves for the x1 from the A1 output and b1 output
res = np.dot(A1out,x1_out)-b1out # calculates the residual of the b1 output and A1 output * x1 output
print("residual = " + str(res))

A2 = np.array([[0,2,0,1],[2,2,3,2],[4,-3,0,1],[6,1,-6,-5]],dtype=float) # given A2
b2 = np.array([0,-2,-7,6],dtype=float) # given b2
A2 = np.array([[2,4,3,3],[2,2,3,2],[6,-1,3,3],[6,1,-6,-5]],dtype=float) # modified A2 to get rid of diagonal zeros (row operations)
b2 = np.array([-2,-2,-9,6],dtype=float) # modified b2 as a result of modifying A2 (row operations)
GaussElimin2 = GaussElimin(A2,b2) # passes modified A2 and modified b2 into GaussElimin
A2out = GaussElimin2[0] # stores the modified A2 output
b2out = GaussElimin2[1] # stores the modified b2 output
print("A2out = " + str(A2out));print("b2out = " + str(b2out))

x2_out = np.linalg.solve(A2out,b2out) # solves for the x2 from the modified A2 output and modified b2 output
res = np.dot(A2out,x2_out)-b2out # calculates the residual of the modified b2 output and modified A2 output * x2 output
print("residuals = " + str(res))