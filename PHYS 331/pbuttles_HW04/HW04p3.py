# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:37:38 2020

@author: pbuttles
"""

################ Part A #################

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

# imports the given csv file as a 41x2 array
data = np.loadtxt("C:/Users/pbuttles/Downloads/HW04p3data.csv", delimiter=",")

################ Part B #################

# initializing lists v and Sv
v = []
Sv = []

# this function stores the first column of imported data into the list v
def importv(x):
    i = 0
    for i in range(41):
        v.append(x[i][0])
    return v

# this function stores the first column of imported data into the list Sv
def importSv(x):
    i = 0
    for i in range(41):
        Sv.append(x[i][1])
    return Sv

v = np.array(importv(data)) # imports and stores the first column of imported data as a numpy array
Sv = np.array(importSv(data)) # imports and stores the second column of imported data as a numpy array

plt.scatter(v,Sv, label="Data")
plt.title("Optical Intensity vs. Wavenumber (collected data)")
plt.legend()
plt.show()

################ Part C #################

# this function is the equation L(v) which takes v, v0, and gamma, and returns the value L
def L(v,v0,gamma):
    L = (1/np.pi) * (((1/2) * gamma) / ((v-v0)**2 + ((1/2) * gamma)**2))
    return L

# this function is the equation S(v) which takes c1, c2, and the inputs for L, and returns the value S
def ModelSpectrum(c1,c2,v01,v02,gamma1,gamma2,v):
    S = c1 * L(v,v01,gamma1) + c2 * L(v,v02,gamma2)
    return S

# plots the given data and the data passed through the model with a set of approximate guesses
plt.scatter(v,Sv, label="Data")
plt.plot(v,ModelSpectrum(50,21,20237,20700,40,50,v), label="ModelSpectrum")
plt.title("Optical Intensity vs. Wavenumber (ModelSpectrum)")
plt.legend()
plt.show()

################ Part D #################

# stores the trial and error guesses from earlier as variables in the numpy array x0
c1 = 50; c2 = 21; v01 = 20237; v02 = 20700; gamma1 = 40; gamma2 = 50
x0 = np.array([c1,c2,v01,v02,gamma1,gamma2])

# this function is essentially ModelSpectrum but indexes values from x0 rather than hard-coding them
def ModelSpectrum2(x,v):
    S = x[0] * L(v,x[2],x[4]) + x[1] * L(v,x[3],x[5])
    return S

# plots the given data and the data passed through ModelSpectrum2, which should be the same as the prior plot
plt.scatter(v,Sv, label="Data")
plt.plot(v,ModelSpectrum2(x0,v), label="ModelSpectrum2")
plt.title("Optical Intensity vs. Wavenumber (ModelSpectrum2)")
plt.legend()
plt.show()

################ Part E #################

# this function calculates the residuals, the difference between actual values and model values
def Residuals(x,v,Sv):
    Resid = Sv - ModelSpectrum2(x,v)
    return np.array(Resid) # stores the residuals in a numpy array

# plots the ModelSpectrum2 model against the plot of the residuals to visually ensure that the residuals are small enough (and hence the guesses are good enough)
plt.plot(v,ModelSpectrum2(x0,v), label="ModelSpectrum2")
plt.plot(v,Residuals(x0,v,Sv), label="Residuals")
plt.scatter(v,Sv, label="Data")
plt.title("Optical Intensity and Residuals vs. Wavenumber")
plt.legend()
plt.show()

################ Part F & G #################

# uses the least squares minimization function from scipy to find the optimized values of the parameters stored in x0
res = scipy.optimize.leastsq(Residuals,x0,args=(v,Sv))
x1 = res[0]

# plots the residuals after scipy least squares optimization
plt.plot(v,Residuals(x1,v,Sv), label="Residuals")
plt.title("Residuals vs. Wavenumber")
plt.legend()
plt.show()

################ Part H #################

# creates a mesh to graph smoothly over, with a range of 20000 to 21000, with mesh size 0.001
vmesh = np.arange(20000,21000,0.001)

# plots the original data against the optimized model, smoothed over vmesh
plt.scatter(v,Sv, label="Data")
plt.plot(vmesh,ModelSpectrum2(x1,vmesh), label="ModelSpectrum2 (Optimized)")
plt.title("Optical Intensity vs. Wavenumber (Optimized)")
plt.legend()
plt.show()
# outputs the best-fit wavenumbers from the optimized parameters stored in x0
print("v01 = " + str(x1[2]))
print("v02 = " + str(x1[3]))
