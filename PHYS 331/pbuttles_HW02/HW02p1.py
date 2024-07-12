# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:11:41 2020

@author: pbuttles
"""

import numpy as np

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
    iters = 0 #initializing iteration counter
    while np.abs(upper-lower) > tolerance and iters < maxiters: #continues loop until tolerance or max iterations is reached
        iters += 1 #iteration counter
        mid = (lower + upper)/2 #determines midpoint
        flower = function(lower) #assigns f(lower) once per iteration for efficiency
        fupper = function(upper) #assigns f(upper) once per iteration for efficiency
        fmid = function(mid) #assigns f(mid) once per iteration for efficiency
        if fmid == 0: #checks for exact roots 
            root = mid #assigns output root value when exact value is reached
            return (root,iters)
        if fmid*flower > 0 and fmid*fupper < 0: #checks for sign difference on the upper half
            lower = mid
        if fmid*flower < 0 and fmid*fupper > 0: #checks for sign difference on the lower half
            upper = mid
        if fmid*flower > 0 and fmid*fupper > 0: #checks for no sign difference (no root or multiple roots in range)
            print("0 or 2+ roots detected for " + str(function))
            return
        if fmid*flower < 0 and fmid*fupper < 0: #checks for sign differences in both halves (multiple roots in range)
            print("2+ roots detected for " + str(function))
            return
    root = mid #assigns output root value after while loop terminates
    if iters == maxiters: #checks if max iterations were reached rather than tolerance reached
        print("WARNING: Max Iterations Reached for " + str(function))
    return (root,iters)

print(rf_bisect(f1,-1,1,10**(-3),1000))
print(rf_bisect(f1,-1,1,10**(-6),1000))
print(rf_bisect(f1,-1,1,10**(-12),1000))
print(rf_bisect(f2,-1,1,10**(-3),1000))
print(rf_bisect(f2,-1,1,10**(-6),1000))
print(rf_bisect(f2,-1,1,10**(-12),1000))
print(rf_bisect(f3,-1,1,10**(-3),1000))
print(rf_bisect(f3,-1,1,10**(-6),1000))
print(rf_bisect(f3,-1,1,10**(-12),1000))
print(rf_bisect(f4,-1,1,10**(-3),1000))
print(rf_bisect(f4,-1,1,10**(-6),1000))
print(rf_bisect(f4,-1,1,10**(-12),1000))
