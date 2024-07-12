# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:37:09 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

# defines f(x) as given in the problem
def f(x):
    fx = np.exp(-x)
    return fx

# defines the range and mesh to be plotted over
x = np.arange(-1,1,0.02)

second = np.polyfit(x,f(x),2) # outputs a2, a1, a0 for 2nd order polynomial fit
third = np.polyfit(x,f(x),3) # outputs a3, a2, a1, a0 for 3rd order polynomial fit
fourth = np.polyfit(x,f(x),4) # outputs a4, a3, a2, a1, a0 for fourth order polynomial fit

plt.plot(x,second[2]+x*second[1]+x**2*second[0]) # plots second order polyfit
plt.plot(x,third[3]+x*third[2]+x**2*third[1]+x**3*third[0]) # plots third order polyfit
plt.plot(x,fourth[4]+x*fourth[3]+x**2*fourth[2]+x**3*fourth[1]+x**4*fourth[0]) # plots fourth order polyfit
plt.plot(x,f(x)) # plots f(x) for reference
plt.show()

plt.plot(x,second[2]+x*second[1]+x**2*second[0]-f(x)) # plots difference of second order polyfit and f(x)
plt.plot(x,third[3]+x*third[2]+x**2*third[1]+x**3*third[0]-f(x)) # plots difference of third order polyfit and f(x)
plt.plot(x,fourth[4]+x*fourth[3]+x**2*fourth[2]+x**3*fourth[1]+x**4*fourth[0]-f(x)) # plots difference of fourth order polyfit and f(x)
plt.show()

print(second)
print(third)
print(fourth)