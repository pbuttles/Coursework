# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:03:42 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("HW08bridge.csv", delimiter=",") # imports given bridge data as array
fourier = np.fft.fft(data) # computes fast fourier transform of data

N = len(data) # initializes the number of samples, or the length of the data set, as N
dt = 20*10**(-3) # given even sampling intervals (delta t) of 20ms
nyquist = 1/(2*dt) # calculates the nyquist frequency corresponding to 1/(2dt)
df = 1/(dt*N) # calculates the minimum frequency as 1/N*dt, to be used as the stepsize for the frequency domain
freqdomain = np.arange(0,len(data)*df,df) # creates the frequency domain starting at f = 0, stepping in df through all N elements, ending at df*N

a = np.abs(np.fft.fft(data)) # computes the absolute value of the fast fourier transform of the data, stores to be used for repeated plotting

plt.plot(freqdomain,a) # plots the fft of the data over the frequency domain
plt.xlim(0,nyquist) # scales the plot to fit from 0 to the nyquist frequency
plt.title("FFT of Bridge Data") # titles the plot
plt.xlabel("Frequency (Hz)") # labels the x-axis
plt.ylabel("Signal Amplitude") # labels the y-axis
plt.show()

# plots the same as above but for the range 0.6 to 1
plt.plot(freqdomain,a)
plt.xlim(0.6,1)
plt.title("FFT of Bridge Data Peak 1")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Signal Amplitude")
plt.show()

# plots the same as above but for the range 3 to 5
plt.plot(freqdomain,a)
plt.xlim(3,5)
plt.title("FFT of Bridge Data Peak 2")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Signal Amplitude")
plt.show()

# plots the same as above but for the range 17 to 20
plt.plot(freqdomain,a)
plt.xlim(17,20)
plt.title("FFT of Bridge Data Peak 3")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Signal Amplitude")
plt.show()
