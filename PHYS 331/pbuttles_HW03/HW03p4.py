# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:13:52 2020

@author: pbuttles
"""

# Template File for Homework 3, Problem 4
# PHYS 331
# Amy Oldenburg

## module newtonRaphson

# has been modified to strip bisection aspects of the code
# is generally UNSAFE, but can be used for specific case of Problem 4

import numpy as np
import matplotlib.pyplot as plt

def newtonRaphsonMOD(f,df,a,b): # YES YOU MAY MODIFY!
    from numpy import sign
    
    #create empty lists for error diagnostics
    error = [] #error diagnostics, has differences between iterations
    
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): 
        print('Root is not bracketed')
        return []
    x = 0.5*(a + b)                    
    for i in range(30):
        fx = f(x)
      # Try a Newton-Raphson step    
        dfx = df(x)
      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x1 = x + dx #the new x is set to x1 to hold to the value temporarily
        err = np.abs(x1-x) #error is computed between the old x (x) and new x (x1)
        x = x1 #with error calculated, x is set to the new value so it is ready to be looped
        error.append(err) #adds error value into error list
    np.array(error) #converts error list into numpy array
    return error

#this is the function given to us
def f(x):
    f = (x+10)*(x-25)*(x**2+45)
    return f

#analytically determined derivative of the given function
def df(x):
    df = (x-25)*(x**2+45)+(x+10)*(x**2+45)+(x+10)*(x-25)*2*x
    return df

def error_ratio(m,error):
    ratios = [] #creates empty list for storing ratios between errors at different iterations
    nonzeros = 0 #initializing counter to determine the number of nonzero error values
    for j in error: #loop runs through every error value in the error array and counts for each nonzero value
        if j != 0.0:
            nonzeros += 1
    for k in range(nonzeros-1): #uses the number of nonzero values to determine the range of this for loop
        r = error[k+1] / (error[k]**m) #calculates the ratio of one error against the previous iteration error
        ratios.append(r) #adds each ratio to the ratio list
    return ratios

#executes newtonRaphsonMOD function over the range [-50,0], returns value
error = newtonRaphsonMOD(f,df,-50,0)
print("error = " + str(error))

#plotting e_n+1 / e_n = c for m=1,1.5,2
x = np.arange(0,7,1)
plt.plot(x,error_ratio(1,error))
plt.plot(x,error_ratio(1.5,error))
plt.plot(x,error_ratio(2,error))
plt.legend(["m=1","m=1.5","m=2"])
