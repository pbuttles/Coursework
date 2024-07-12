# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:35:28 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

V = np.array([[1,0,0,0,0,0,0,0],[1,1,1,1,0,0,0,0],[0,0,0,0,1,1,1,1],[0,0,0,0,1,2,4,8],[0,1,2,3,0,-1,-2,-3],[0,0,2,6,0,0,-2,-6],[0,0,2,0,0,0,0,0],[0,0,0,0,0,0,2,12]])

y = np.array([2,5,5,6,0,0,0,0])

a = np.linalg.inv(V)@y

print(a)

def f1(x,a,b,c,d):
    f = a + b*x + c*x**2 + d*x**3
    return f

def f2(x,a,b,c,d):
    f = a + b*x + c*x**2 + d*x**3
    return f

xs = [0,1,2]
ys = [2,5,6]

x = np.arange(0,2,0.01)
x1 = np.arange(0,1,0.01)
x2 = np.arange(1,2,0.01)

# plots interpolations to check if it makes sense (it does)
plt.scatter(xs,ys)
plt.plot(x1,f1(x1,a[0],a[1],a[2],a[3]))
plt.plot(x2,f2(x2,a[4],a[5],a[6],a[7]))
plt.show()