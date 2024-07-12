# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:56:30 2020

@author: pbuttles
"""
import numpy as np
import matplotlib.pyplot as plt

#this is the f(x) function given to us
def f(x):
    fx = (x**5)-(3*x**3)+(15*x**2)+(27*x)+9
    return fx

#adding x to each side of f(x) yields this g(x)
def g1(x):
    g1 = (x**5)-(3*x**3)+(15*x**2)+(28*x)+9
    return g1

#adding x^2 to each side of f(x), then taking the square root, yields this g(x)
def g2(x):
    g2 = ((x**5)-(3*x**3)+(16*x**2)+(27*x)+9)**(1/2)
    return g2

#adding x^3 to each side of f(x), then taking the cube root, yields this g(x)
def g3(x):
    g3 = ((x**5)-(2*x**3)+(15*x**2)+(27*x)+9)**(1/3)
    return g3

#this is the analytic derivative of g1(x)
def dg1(x):
    dg1 = (5*x**4)-(9*x**2)+(30*x)+28
    return dg1

#this is the analytic derivative of g2(x)
def dg2(x):
    dg2 = (1/2)*((x**5)-(3*x**3)+(17*x**2)+(27*x)+9)**(-1/2)*((5*x**4)-(9*x**2)+(32*x)+27)
    return dg2

#this is the analytic derivative of g3(x)
def dg3(x):
    dg3 = (1/3)*((x**5)-(2*x**3)+(15*x**2)+(27*x)+9)**(-2/3)*((5*x**4)-(6*x**2)+(30*x)+27)
    return dg3

#this is y=x, used for graphing later
def yx(x):
    y = x
    return y

#g1(x), |dg1(x)|, y=0, and y=x all graphed over the mesh x, fit for viewing
x = np.arange(-3,3,0.001)
plt.plot(x,g1(x), color="blue", label="g1(x)")
plt.plot(x,np.abs(dg1(x)), color="orange", label="dg1(x)")
plt.axhline(y=0, color="black")
plt.plot(x,yx(x), color="green")
plt.ylim(-5,20)
plt.legend()
plt.show()

#g2(x), |dg2(x)|, y=0, and y=x all graphed over the mesh x, fit for viewing
x = np.arange(-3,3,0.001)
plt.plot(x,g2(x), color="blue", label="g2(x)")
plt.plot(x,np.abs(dg2(x)), color="orange", label="dg2(x)")
plt.axhline(y=0, color="black")
plt.plot(x,yx(x), color="green")
plt.ylim(-5,20)
plt.legend()
plt.show()

#g3(x), |dg3(x)|, y=0, and y=x all graphed over the mesh x, fit for viewing
x = np.arange(-3,3,0.001)
plt.plot(x,g3(x), color="blue", label="g3(x)")
plt.plot(x,np.abs(dg3(x)), color="orange", label="dg3(x)")
plt.axhline(y=0, color="black")
plt.plot(x,yx(x), color="green")
plt.ylim(-5,20)
plt.legend()
plt.show()

#this is the fixed point iteration function, which takes the function g, at some starting xstart, and iterates until it reaches some tolerance or max number of iterations
def fixed_pt(g,xstart,tol,nmax):
    err = tol + 1 #initializes the error as greater than the tolerance
    iters = 0 #initializes the iteration counter
    x1 = xstart #initializes the x1 value as the xstart value
    while err > tol and iters < nmax: #iterates until error is less than tolerance or the max number of iterations is reached
        gx1 = g(x1) #passes x1 into g and assigns this to a new variable gx1
        x2 = gx1 #assigns this "y value" to a new x value, x2, like translating to the y=x line
        x3 = g(x2) # takes the new x value on the y=x line and passes it into the g function, translating back onto g
        err = np.abs(x3-x1) #calculates error between the x component of the new point on g and the x component of the old point on g
        x1 = x3 #resets x1 to be the new value, for continued iterations
        iters += 1 #increases the iteration counter by one
    return x1

#print(fixed_pt(g1,-1.84,10**(-15),2))
#print(fixed_pt(g1,-0.8,10**(-15),2))
#print(fixed_pt(g1,-1.1,10**(-15),3))
#print(fixed_pt(g1,-2.3,10**(-15),2))
#print(fixed_pt(g1,-0.5,10**(-15),3))

#print(fixed_pt(g2,-1.9,10**(-15),3))
#print(fixed_pt(g2,-1.1,10**(-15),3))
#print(fixed_pt(g2,-2.3,10**(-15),3))
#print(fixed_pt(g2,-0.5,10**(-15),4))

#print(fixed_pt(g3,-1.7,10**(-15),5))
#print(fixed_pt(g3,-0.8,10**(-15),6))
#print(fixed_pt(g3,-1.1,10**(-15),6))
#print(fixed_pt(g3,-2.3,10**(-15),5))
#print(fixed_pt(g3,-0.5,10**(-15),6))
