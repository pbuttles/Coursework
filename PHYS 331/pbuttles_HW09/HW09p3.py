# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:34:49 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

####################################
####### Begin Copy From Book #######
####################################

def RK4Integrate(F,x,y,xStop,h):
    ## module run_kut4
    ''' X,Y = integrate(F,x,y,xStop,h).
    4th-order Runge-Kutta method for solving the
    initial value problem {y}’ = {F(x,{y})}, where
    {y} = {y[0],y[1],...y[n-1]}.
    x,y = initial conditions
    xStop = terminal value of x
    h = increment of x used in integration
    F = user-supplied function that returns the
        array F(x,y) = {y’[0],y’[1],...,y’[n-1]}.'''

    def run_kut4(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
    
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut4(F,x,y,h)
        x=x+h
        X.append(x)
        Y.append(y)
    return np.array(X),np.array(Y)

####################################
######## End Copy From Book ########
####################################

# this function inputs starting x values and y as a vector of y1 and y2 at the starting x, and returns a vector of dy1 and dy2
def Fcoupled(x,y):
    F = np.zeros(2) # initializes the F output vector of dy1 and dy2
    y1 = y[0] # indexes the y1 equation from the yvec
    y2 = y[1] # indexes the y2 equation from the vec
    dy1 = y2 # sets dy1 equal to y2 as a substitution
    dy2 = -(2*x+3)*y2 - 6*x*y1 + x # sets dy2 equal to the expression formed after the dy1=y2 substition
    F = np.array([dy1,dy2]) # forms the output array of dy1 and dy2
    return F

y = np.array([1,1]) # given initial conditions for y and y' (y1 and y2) at x=0,0

rk4h1 = RK4Integrate(Fcoupled,0,y,4,1) # executes the RK4 function for Fcoupled, x, y, and xStop, with h = 1
plt.plot(rk4h1[0],rk4h1[1]) # plots the two pairs of vector outputs of the RK4 as two curves on the same graph, where blue = y1 and orange = y2
plt.title("RK4 for h=1") # titles the plot
plt.show()

rk4h2 = RK4Integrate(Fcoupled,0,y,4,0.1) # executes the RK4 function for Fcoupled, x, y, and xStop, with h = 0.1
plt.plot(rk4h2[0],rk4h2[1]) # plots the two pairs of vector outputs of the RK4 as two curves on the same graph, where blue = y1 and orange = y2
plt.title("RK4 for h=0.1") # titles the plot
plt.show()

rk4h3 = RK4Integrate(Fcoupled,0,y,4,0.01) # executes the RK4 function for Fcoupled, x, y, and xStop, with h = 0.01
plt.plot(rk4h3[0],rk4h3[1]) # plots the two pairs of vector outputs of the RK4 as two curves on the same graph, where blue = y1 and orange = y2
plt.title("RK4 for h=0.01") # titles the plot
plt.show()

rk4h4 = RK4Integrate(Fcoupled,0,y,4,0.001) # executes the RK4 function for Fcoupled, x, y, and xStop, with h = 0.001
plt.plot(rk4h4[0],rk4h4[1]) # plots the two pairs of vector outputs of the RK4 as two curves on the same graph, where blue = y1 and orange = y2
plt.title("RK4 for h=0.001") # titles the plot
plt.show()
    