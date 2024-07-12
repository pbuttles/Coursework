# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:29:32 2020

@author: pbuttles
"""
# importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# defining the function being analyzed
def func(x):
    func = x**5-3*x**3+15*x**2+27*x+9
    return func

#graphing the function func over the mesh x, with x and y axes, fitted for viewing
x = np.arange(-3,1,0.01)
plt.plot(x,func(x))
plt.axhline(y=0, color="black") #x-axis for reference
plt.axvline(x=0, color="black") #y-axis for reference
plt.ylim(-15,15)

#defining the newton-raphson g(x) = x - f(x)/f'(x)
def NR(x):
    y = x - (x**5-3*x**3+15*x**2+27*x+9)/(5*x**4-9*x**2+30*x+27)
    return y

#defining the Newt function that iterates over NR from an xstart until a tolerance is reached
def Newt(xstart,tol):
    x = xstart
    err = tol + 1 #initializing the error counter as more than the tolerance
    while err > tol: #looping until the error reaches the tolerance
        x1 = NR(x) #iterates over the NR function
        err = np.abs(x1-x) #calculates error between iterations
        x = x1 #resets x to the new x value for the next iteration
    return x

#executes the Newt function, passing the starting point x, at a fixed tolerance 10^-14
def test(x):
    x = Newt(x,10**(-14))
    return x

#prints the calculated roots
print("root 1 = " + str(test(-2.3)))
print("root 2 = " + str(test(-1.1)))
print("root 3 = " + str(test(-0.5)))
