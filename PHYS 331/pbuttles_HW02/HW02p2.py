# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 19:28:14 2020

@author: pbuttles
"""

#import relevant libraries
import numpy as np
import matplotlib.pyplot as plt

def f1(x): #defines the given function f1(x)
    f1 = 3*x+2*np.sin(x)-np.exp(x)
    return f1
    
def f2(x): #defines the given function f2(x)
    f2 = x**3-0.125
    return f2
    
def f3(x): #defines the given function f3(x)
    f3 = np.sin(1/(x+0.01))
    return f3
    
def f4(x): #defines the given function f4(x)
    f4 = 1/(x-1/2)
    return f4

def rf_bisect(function,lower,upper,tolerance,maxiters): #defines bisection function
    xmids = [] #creates an empty array for storing xmid values
    fmids = [] #creates an empty array for storing fmid values
    iters = 0 #initializes iteration counter
    while np.abs(upper-lower) > tolerance and iters < maxiters:  #continues loop until tolerance or max iterations is reached
        iters += 1 #iteration counter
        mid = (lower + upper)/2 #determines midpoint
        flower = function(lower) #assigns f(lower) once per iteration for efficiency
        fupper = function(upper) #assigns f(upper) once per iteration for efficiency
        fmid = function(mid) #assigns f(mid) once per iteration for efficiency
        if fmid == 0: #checks for exact values
            xmids.append(mid) #writes mid value to xmids
            fmids.append(fmid) #writes fmid value to fmid
            np.array(xmids) #converts python array to numpy array
            np.array(fmids) #converts python array to numpy array
            tolerance = np.abs(upper-lower) #establishes that the tolerance has been reached so the loop may terminate
        if fmid*flower > 0 and fmid*fupper < 0: #checks for sign difference on the upper half
            lower = mid #shifts lower point to create new bracket
            xmids.append(mid) #write this iteration xmid to xmids
            fmids.append(fmid) #write this iteration fmid to fmids
        if fmid*flower < 0 and fmid*fupper > 0: #checks for sign difference on the lower half
            upper = mid #shifts upper point to create new bracket
            xmids.append(mid) #write this iteration xmid to xmids
            fmids.append(fmid) #write this iteration fmid to fmids
        if fmid*flower > 0 and fmid*fupper > 0: #checks for no sign difference (no root or multiple roots in range)
            print("0 or 2+ roots detected for " + str(function))
            return
        if fmid*flower < 0 and fmid*fupper < 0: #checks for sign differences in both halves (multiple roots in range)
            print("2+ roots detected for " + str(function))
            return
    if iters == maxiters: #checks if max iterations were reached rather than tolerance reached
        print("WARNING: Max Iterations Reached for " + str(function))
    np.array(xmids) #converts python array to numpy array
    np.array(fmids) #converts python array to numpy array
    
    #graphs iterations for part c
    plt.scatter(xmids,fmids) #creates a scatter plot of iterations
    x = np.arange(-1,1,0.01) #creates mesh from -1 to 1 with mesh size 0.01
    plt.plot(x,function(x)) #plots the given function over the mesh x
    plt.title('Root approximations for ' + str(function))
    plt.axhline(y=0) #y-axis for reference
    plt.axvline(x=0) #x-axis for reference
    plt.xlim(-1,1)
    plt.show()
    
    #error vs iteration plotting:
    truevalue = xmids[iters-1] #assigns the found root as the true value of the root
    error = np.subtract(xmids,truevalue) #finds error by subtracting the true value of the root from all previous iterations
    plt.scatter(np.arange(iters)+1,error) #plots the error against the number of iterations
    plt.title('Error vs. iterations for ' + str(function)) #titles the graph
    plt.axhline(y=0) #y-axis for reference
    plt.axvline(x=0) #x-axis for reference
    plt.show()
    return (xmids,fmids)

print("f1 xmids and fmids: " + str(rf_bisect(f1,-1,1,10**(-10),1000)))
print("f2 xmids and fmids: " + str(rf_bisect(f2,-1,1,10**(-10),1000)))
print("f3 xmids and fmids: " + str(rf_bisect(f3,-1,1,10**(-10),1000)))