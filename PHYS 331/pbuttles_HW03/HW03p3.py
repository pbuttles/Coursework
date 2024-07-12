# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:14:42 2020

@author: pbuttles
"""

# Template File for Homework 3, Problem 3
# PHYS 331
# Amy Oldenburg
#----------------------------------------------   
# DO NOT MODIFY BETWEEN THIS LINE AND ONE BELOW
## module newtonRaphson
''' root = newtonRaphson(f,df,a,b,tol,maxiter).
    Finds a root of f(x) = 0 by combining the Newton-Raphson
    method with bisection. The root must be bracketed in (a,b).
    Calls user-supplied functions f(x) and its derivative df(x).   
    tol is the tolerance, and maxiter is the maximum number of iterations..
''' 
def newtonRaphson(f,df,a,b,tol,maxiter): 
    from numpy import sign
    
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): 
        print('Root is not bracketed')
        return []
    x = 0.5*(a + b)                    
    for i in range(maxiter):
        fx = f(x)
        if fx == 0.0: return x
      # Tighten the brackets on the root 
        if sign(fa) != sign(fx): b = x  
        else: a = x
      # Try a Newton-Raphson step    
        dfx = df(x)
      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx
      # If the result is outside the brackets, use bisection  
        if (b - x)*(x - a) < 0.0:  
            dx = 0.5*(b - a)                      
            x = a + dx
      # Check for convergence     
        if abs(dx) < tol*max(abs(b),1.0): return x
    print('Too many iterations in Newton-Raphson')
## ADD your code below this line
#----------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

#importing values given from the problem, doing some menial calculations
L = 0.9 #m
W = 25*10**(-3) #m
H = 2.5*10**(-3) #m
D = 7850 #kg/m^3
V = L*W*H #m^3
m = D*V #kg
I = (W*(H**3))/12 #m^4
E = 200*10**9 #Pa

#for efficiency/sanity's sake, all the constants from the B^4 function are multiplied out here
#this way, plugging B (the fourth root has been taken) into f(B) is much simpler
#plus, taking the derivative is not so bad
a = (2*np.pi)**(1/2)*m**(1/4)*L**(3/4)*(E*I)**(-1/4)

#B = a(fi)^(1/2) plugged into f = cosh(B)cos(B)+1
def f(fi):
    f = np.cosh(a*fi**(1/2))*np.cos(a*fi**(1/2))+1
    return f

#taking the derivative of f
def df(fi):
    df = (a*(1/2)/(fi**(1/2))) * (np.sinh(a*fi**(1/2))*np.cos(a*fi**(1/2))-np.cosh(a*fi**(1/2))*np.sin(a*fi**(1/2)))
    return df

#plotting the frequency function to visually estimate ranges on roots
x = np.arange(0,20,0.01)
plt.plot(x,f(x))
plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
    
#using bounds [0,5] for frequency 1 and [10,20] for frequency 2
print("frequency 1 = " + str(newtonRaphson(f,df,0,5,10**(-4),100)))
print("frequency 2 = " + str(newtonRaphson(f,df,10,20,10**(-4),100)))
