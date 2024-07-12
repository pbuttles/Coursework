# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:04:49 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

#initializing given values Q, g, b, h0, and H
Q = 1.2
g = 9.81
b = 1.8
h0 = 0.6
H = 0.075

#purely numerical terms are calculated once for efficiency and assigned to a,b
a = Q**2/(2*g*b**2*h0**2)+h0-H
b = Q**2/(2*g*b**2)

def bernoulli(h): #defines bernoulli equation rewritten equal to 0, multiplied by x^2 to get rid of potential division by 0 errors
    bernoulli = -h**3+a*h**2-b
    return bernoulli

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
            return (root,iters) #because the exact value is found, the loop terminates
        if fmid*flower > 0 and fmid*fupper < 0: #checks for sign difference on the upper half
            lower = mid
        if fmid*flower < 0 and fmid*fupper > 0: #checks for sign difference on the lower half
            upper = mid
        if fmid*flower > 0 and fmid*fupper > 0: #checks for no sign difference (no root or multiple roots in range)
            print("0 or 2+ roots detected")
            return
        if fmid*flower < 0 and fmid*fupper < 0: #checks for sign differences in both halves (multiple roots in range)
            print("2+ roots detected")
            return
    root = mid #assigns output root value after while loop terminates
    if iters == maxiters: #checks if max iterations were reached rather than tolerance reached
        print("WARNING: Max Iterations Reached")
    return (root,iters)

h = np.arange(0,1,0.0001) #graphs from 0 to 1 with mesh size of 0.0001
plt.plot(h,bernoulli(h)) #plot the bernoulli equation over the mesh x
plt.axhline(y=0) #y-axis for reference
plt.axvline(x=0) #x-axis for reference
plt.xlim(0,0.7) #adjusted for easier viewing
plt.ylim(-0.03,0.03) #adjusted for easier viewing
plt.title('Roots for Bernoulli Equation')

h1 = rf_bisect(bernoulli,0.1,0.4,10**(-3),1000)[0] #assign output to h1
h2 = rf_bisect(bernoulli,0.4,0.6,10**(-3),1000)[0] #assign output to h2
print("roots found = " + str(h1) + ", " +str(h2)) #returns both roots from rf_bisect

h1 = round(h1,3) #rounds roots to 3 sigfigs
h2 = round(h2,3) #rounds roots to 3 sigfigs
plt.scatter((h1,h2),(0,0)) #plots rounded roots on graph for easier viewing
print("h = " + str(h1) + ", " +str(h2)) #returns rounded roots
