# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:39:26 2020

@author: pbuttles
"""

import numpy as np # imported for arrays and mathematical functions
import matplotlib.pyplot as plt # imported for plotting
import time # imported for time.time() function

# computes discrete fourier transform of random array of length N
def myDFT(N):
    H = np.zeros(N) # initializing array for fourier transformation H
    h = np.random.rand(N) # creates randomized array of length N to be fourier transformed
    for n in range(N): #computes each H_n
        Hval = 0 # initializes the H_n value to be calculated
        for k in range(N):
            Hval += h[k]*np.exp(-2j*np.pi*k*n/N) # calculates H_n as a sum from k = 0 to N-1 as given in the problem
        H[n] = Hval # stores each H_n in its respective spot in the array H
    return H # returns array of fourier transformed values

# calculates runtime of myDFT for random array of length N
def dftruntime(N):
    starttime = time.time() # records starting time
    myDFT(N) # runs myDFT for random array of length N
    duration = time.time() - starttime # takes difference of end time and start time to find duration
    return duration # returns duration of myDFT runtime

# calcuates runtime of np.fft.fft for random array of length N
def fftruntime(N):
    starttime = time.time() # records starting time
    h = np.random.rand(N) # creates random array of length N
    np.fft.fft(h) # computes fast fourier transform of random array h
    duration = time.time() - starttime # takes difference of end time and start time to find duration
    return duration # returns duration of fft runtime

x = np.array([10,100,1000]) # array of x values to be plotted over
ydft = np.array([dftruntime(10),dftruntime(100),dftruntime(1000)]) # computes the runtime of myDFT at the given x values
plt.plot(np.log(x),np.log(ydft)) # plots the log-log of the runtime of myDFT vs array size
plt.title("log(myDFT runtime) vs. log(array length)") # titles plot
plt.xlabel("log(array length N)") # labels x-axis
plt.ylabel("log(myDFT runtime) (sec)") # labels y-axis
plt.show()

x = np.array([10**5,10**6,10**7]) # array of x values to be plotted over
yfft = np.array([fftruntime(10**5),fftruntime(10**6),fftruntime(10**7)]) # computes the runtime of np.fft.fft at the given x values
plt.plot(np.log(x),np.log(yfft)) # plots the log-log of the runtime of np.fft.fft vs array size
plt.title("log(fft runtime) vs. log(array length)") # titles plot
plt.xlabel("log(array length N)") # labels x-axis
plt.ylabel("log(fft runtime) (sec)") # labels y-axis
plt.show()
