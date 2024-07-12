# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 18:08:03 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

m = 15; gamma = 2.2; k = 32; w0 = np.sqrt(k/m) # given physical quantities

# this function computes the amplitude of cos(2pift) using a Lorentzian function
def cosdrivingforce(f):
    ampl = (1/m)/(np.sqrt((w0**2 - f**2)**2 + f**2*gamma**2/m**2))
    return ampl

frange = np.arange(0,5,0.001) # this is the mesh to plot the driving force over
plt.plot(frange,cosdrivingforce(frange)) # plots the cosine driving force
plt.title("Amplitude of cosine-driven damped spring motion vs. frequency")
plt.show()

# this is the function F given to us
def F(t,tau):
    F = np.exp((-t**2)/(tau**2))
    return F

def gaussian(tau):
    dt = 0.01 # this is the given mesh size for the time range
    trange = np.arange(-1000,1000,dt) # this is the time domain mesh
    N = len(trange) # this is the number of points we sample over
    df = 1/(N*dt) # this is the mesh size for the frequency domain
    wrange = np.arange(0,N*df,df) # this is the frequency domain mesh
    Ft = F(trange,tau) # this computes F over our time domain mesh
    Fw = np.fft.fft(Ft) # this fourier transforms our F in the time domain to F in the frequency domain
    Xw = Fw/(-m*(wrange*2*np.pi)**2+gamma*(wrange*2*np.pi)*1j+k) # this convert F(w) to X(w), F in frequency domain to motion in frequency domain
    xt = np.fft.ifft(Xw) # this given motion in the time domain from motion in frequency domain by inverse fourier transform
    return Ft, xt, Fw, Xw, trange, wrange

Ft1, xt1, Fw1, Xw1, trange1, wrange1 = gaussian(1) # runs and outputs values for tau = 1
Ft3, xt3, Fw3, Xw3, trange3, wrange3 = gaussian(3) # runs and outputs values for tau = 3
Ft10, xt10, Fw10, Xw10, trange10, wrange10 = gaussian(10) # runs and outputs values for tau = 10

# plots F(t) for taus
plt.plot(trange1,Ft1,label="tau = 1s")
plt.plot(trange3,Ft3,label="tau = 3s")
plt.plot(trange10,Ft10,label="tau = 10s")
plt.xlim(-50,50)
plt.title("F(t) vs w for tau = 1, 3, 10")
plt.legend()
plt.show()

# plots F(w) for taus
plt.plot(wrange1,np.abs(Fw1),".",label="tau = 1s")
plt.plot(wrange3,np.abs(Fw3),".",label="tau = 3s")
plt.plot(wrange10,np.abs(Fw10),".",label="tau = 10s")
plt.xlim(0,1)
plt.title("F(w) vs w for tau = 1, 3, 10")
plt.legend()
plt.show()

# plots X(w) for taus
plt.plot(wrange1,np.abs(Xw1),".",label="tau = 1s")
plt.plot(wrange3,np.abs(Xw3),".",label="tau = 3s")
plt.plot(wrange10,np.abs(Xw10),".",label="tau = 10s")
plt.xlim(0,1)
plt.title("X(w) vs w for tau = 1, 3, 10")
plt.legend()
plt.show()

# plots x(t) for taus
plt.plot(trange1,xt1,label="tau = 1s")
plt.plot(trange3,xt3,label="tau = 3s")
plt.plot(trange10,xt10,label="tau = 10s")
plt.xlim(-50,50)
plt.title("x(t) vs t for tau = 1, 3, 10")
plt.legend()
plt.show()
