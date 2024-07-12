# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:32:31 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

C = np.array([[-998.0,-1998.0],[999.0,1999.0]]) # matrix from set of equations, all times -1

# computes exact solution from equations we analytically solved in class
def ExactSol(xvec):
    u = 2*np.exp(-xvec) - np.exp(-1000*xvec)
    v = -np.exp(-xvec) + np.exp(-1000*xvec)
    return u,v

# computes explicit integration as I - hC
def ExplicitIntegrate(xstart, xstop, h, ystart):
    xvec = np.arange(xstart,xstop+h,h)
    n = len(xvec)
    yvec = np.zeros([n,2])
    M = np.identity(len(C)) - h*C
    yvec[0] = ystart
    for i in range(1,n):
        yvec[i] = M@yvec[i-1]
    return xvec, yvec

# mimics the above function but for inv(I + hC)
def ImplicitIntegrate(xstart, xstop, h, ystart):
    xvec = np.arange(xstart,xstop+h,h)
    n = len(xvec)
    yvec = np.zeros([n,2])
    M = np.linalg.inv(np.identity(len(C)) + h*C)
    yvec[0] = ystart
    for i in range(1,n):
        yvec[i] = M@yvec[i-1]
    return xvec, yvec 

ystart = np.array([1,0])
h=0.001

# plots exact solution on its own
x = np.arange(0,4,h)
u,v = ExactSol(x)
plt.plot(x,u, label="Exact u")
plt.plot(x,v, label="Exact v")
plt.xscale("log")
plt.title("Exact Solution")
plt.legend()
plt.show()

# plots exact solution vs. explicit integration solution
xvec, yvec = ExplicitIntegrate(0,4,h,ystart)
plt.plot(x,u)
plt.plot(x,v)
plt.plot(xvec,yvec)
plt.xscale("log")
plt.title("Exact Solution vs. Explicit Solution")
plt.legend(["Exact u","Exact v","Explicit u","Explicit v"])
plt.show()

# plots exact solution vs. implicit integration solution
xvec, yvec = ImplicitIntegrate(0,4,h,ystart)
plt.plot(x,u)
plt.plot(x,v)
plt.plot(xvec,yvec)
plt.xscale("log")
plt.title("Exact Solution vs. Implicit Solution")
plt.legend(["Exact u","Exact v","Implicit u","Implicit v"])
plt.show()