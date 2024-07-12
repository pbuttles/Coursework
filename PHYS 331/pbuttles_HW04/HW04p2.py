# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:00:11 2020

@author: pbuttles
"""

# Homework 4, Problem 2 Template
# Amy Oldenburg

import numpy as np
import math
import sys

## module error
''' err(string).
    Prints 'string' and terminates program.
'''    
def err(string):
    print(string)
    input('Press return to exit')
    sys.exit(0)

## module swap
''' swapRows(v,i,j).
    Swaps rows i and j of a vector or matrix [v].

    swapCols(v,i,j).
    Swaps columns of matrix [v].
'''
def swapRows(v,i,j):
    if len(v.shape) == 1:
        v[i],v[j] = v[j],v[i]
    else:
        v[[i,j],:] = v[[j,i],:]
        
def swapCols(v,i,j):
    v[:,[i,j]] = v[:,[j,i]]
    
## module gaussPivot
''' x = gaussPivot(a,b,tol=1.0e-12).
    Solves [a]{x} = {b} by Gauss elimination with
    scaled row pivoting
'''    
def gaussPivot(a,b,tol=1.0e-12):
    n = len(b)
    
  # Set up scale factors
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(a[i,:]))
            
    for k in range(0,n-1):
        
      # Row interchange, if needed
        p = np.argmax(np.abs(a[k:n,k])/s[k:n]) + k
        if abs(a[p,k]) < tol: err('Matrix is singular')
        if p != k:
            swapRows(b,k,p)
            swapRows(s,k,p)
            swapRows(a,k,p)
            
      # Elimination
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    if abs(a[n-1,n-1]) < tol: err('Matrix is singular')
                   
  # Back substitution
    b[n-1] = b[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

## module newtonRaphson2
''' soln = newtonRaphson2(f,x,tol=1.0e-9).
    Solves the simultaneous equations f(x) = 0 by
    the Newton-Raphson method using {x} as the initial
    guess. Note that {f} and {x} are vectors.
'''
def newtonRaphson2(f,x,tol=1.0e-9):
    
    def jacobian(f,x):
        h = 1.0e-4
        n = len(x)
        jac = np.zeros((n,n))
        f0 = f(x)
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = f(x)
            x[i] = temp
            jac[:,i] = (f1 - f0)/h
        return jac,f0
    
    for i in range(30):
        jac,f0 = jacobian(f,x)
        if math.sqrt(np.dot(f0,f0)/len(x)) < tol:
            return x
        dx = gaussPivot(jac,-f0)
        x = x + dx
        if math.sqrt(np.dot(dx,dx)) < tol*max(max(abs(x)),1.0): return x
    print('Too many iterations')

### EDIT BELOW HERE ###

x = [400,10,np.pi/4] # initializing an array of the form [C,e,alpha] with a set of initial guesses

# R = C / (1 + e sin(theta + alpha)) becomes R + R e sin(theta + alpha) - C = 0

# defining the first function from the first values of R and theta
def f1(x):
    f1 = 6870 + 6870*x[1]*np.sin(np.radians(-30) + x[2]) - x[0]
    return f1

# defining the second function from the second values of R and theta
def f2(x):
    f2 = 6728 + 6728*x[1]*np.sin(np.radians(0) + x[2]) - x[0]
    return f2
        
# defining the third function from the third values of R and theta
def f3(x):
    f3 = 6615 + 6615*x[1]*np.sin(np.radians(30) + x[2]) - x[0]
    return f3

# defining the system of equations F(x), consisting of f1(x), f2(x), and f3(x)
def F(x):
    F = np.array([f1(x),f2(x),f3(x)])
    return F

NR2 = newtonRaphson2(F,x) # plugging the system of equations F and the initial value guesses x into the given function newtonRaphson2
C = NR2[0] # indexing C from NR2
e = NR2[1] # indexing e from NR2
alpha = np.degrees(NR2[2]) # indexing alpha from NR2 and converting from radians to degrees
#print("C = " + str(C) + ", e = " + str(e) + ", alpha = " + str(alpha))

# R is minimized when the denominator is maximized. The denominator is maximized when sine is maximized. Sine is maximized at 90 degrees
mintheta = 90 - alpha # R is minimized when theta + alpha = 90
print("minimum theta = " + str(mintheta))
minR = C / (1 + e*np.sin(mintheta + alpha)) # plugging mintheta back into the original equation to find minR
print("minimum trajectory distance = " + str(minR))
