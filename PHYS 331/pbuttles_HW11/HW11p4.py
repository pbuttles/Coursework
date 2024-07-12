# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:52:05 2020

@author: pbuttles
"""

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# given function being investigated
def f(x):
    f = np.abs(np.sin(x))
    return f

sample = np.arange(-10,10+0.1,0.1) # samples support points over this range
supports = f(sample) # computes support points along sampling range

# plots support points with y=0 refline to give general shape of the function
plt.scatter(sample,supports,label="support points")
plt.hlines(0,-10,10,label="y=0")
plt.title("Support Points of |sin(x)|")
plt.legend()
plt.show()

x = np.arange(-10,10+0.0001,0.0001) # this is the fine mesh all fits and functions will be plotted over

# computes 4 different interpolations from support point data
nearestinterp = interpolate.interp1d(sample,f(sample),'nearest')
linearinterp = interpolate.interp1d(sample,supports,'linear')
quadraticinterp = interpolate.interp1d(sample,supports,'quadratic')
cubicinterp = interpolate.interp1d(sample,supports,'cubic')

# plotting nearest neighbor interpolation
plt.scatter(sample,supports,label="support points")
plt.plot(x,f(x),label="true function")
plt.plot(x,nearestinterp(x),label="nearest neighbor interpolation")
plt.xlim(-0.5,0.5)
plt.ylim(-0.1,0.6)
plt.title("True function vs. nearest neighbor interpolation of |sin(x)|")
plt.legend()
plt.show()

# plotting linear interpolation
plt.scatter(sample,supports,label="support points")
plt.plot(x,f(x),label="true function")
plt.plot(x,linearinterp(x),label="linear interpolation")
plt.xlim(-0.5,0.5)
plt.ylim(-0.1,0.6)
plt.title("True function vs. linear interpolation of |sin(x)|")
plt.legend()
plt.show()

# plotting quadratic interpolation
plt.scatter(sample,supports,label="support points")
plt.plot(x,f(x),label="true function")
plt.plot(x,quadraticinterp(x),label="quadratic interpolation")
plt.xlim(-0.5,0.5)
plt.ylim(-0.1,0.6)
plt.title("True function vs. quadratic interpolation of |sin(x)|")
plt.legend()
plt.show()

# plotting cubic interpolation
plt.scatter(sample,supports,label="support points")
plt.plot(x,f(x),label="true function")
plt.plot(x,cubicinterp(x),label="cubic interpolation")
plt.xlim(-0.5,0.5)
plt.ylim(-0.1,0.6)
plt.title("True function vs. cubic interpolation of |sin(x)|")
plt.legend()
plt.show()

# plotting linear vs cubic at specific interval
plt.scatter(sample,supports,label="support points")
plt.plot(x,f(x),label="true function")
plt.plot(x,linearinterp(x),label="linear interpolation")
plt.plot(x,cubicinterp(x),label="cubic interpolation")
plt.xlim(1.4,1.75)
plt.ylim(0.994,1.001)
plt.title("True function vs. linear vs cubic interpolation of |sin(x)|")
plt.legend()
plt.show()