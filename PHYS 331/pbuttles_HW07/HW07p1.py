# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:21:41 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

def funcSawtooth(nmax):
    A0 = 1 # A_0 = 1 as determined mathematically in part a
    AN = 0 # initializes AN, the sum of all An
    mesh = 1/(10*nmax)
    #mesh = 0.01
    x = np.arange(-2,2,mesh) # sets the range to be evaluated and graphed over
    for n in range(1,nmax+1): # makes a for loop from 1 to nmax
        An = (-2/(np.pi**2*n**2))*np.cos(np.pi*n) + (2/(np.pi**2*n**2)) # computes An for any n as determined analytically
        AN += An * np.cos(np.pi*n*x/2) # computes the summation for An and adds it to the sum of An terms, AN
    fx = A0/2 + AN # computes the fourier series representation of fx
    plt.plot(x,fx) # plots the fourier series representation over x
    
    leftx = np.arange(-2,0+mesh,mesh) # mesh for left half of the piecewise f(x) graph
    rightx = np.arange(0,2,mesh) # mesh for right half of the piecewise f(x) graph
    plt.plot(leftx,leftx/2 + 1, color="orange") # plots the left half of the piecewise f(x)
    plt.plot(rightx,-rightx/2 + 1, color="orange") # plots the right half of the piecewise f(x)
    plt.show()
    return

funcSawtooth(1)
funcSawtooth(2)
funcSawtooth(3)
funcSawtooth(30)

def ModFuncSawtooth(nmax):
    A0 = 1 # A_0 = 1 as determined mathematically in part a
    AN = 0 # initializes AN, the sum of all An
    mesh = 1/(10*nmax)
    #mesh = 0.01
    x = np.arange(-6,6,mesh) # sets the range to be evaluated and graphed over
    for n in range(1,nmax+1): # makes a for loop from 1 to nmax
        An = (-2/(np.pi**2*n**2))*np.cos(np.pi*n) + (2/(np.pi**2*n**2)) # computes An for any n as determined analytically
        AN += An * np.cos(np.pi*n*x/2) # computes the summation for An and adds it to the sum of An terms, AN
    fx = A0/2 + AN # computes the fourier series representation of fx
    plt.plot(x,fx) # plots the fourier series representation over x
    plt.show()
    return

ModFuncSawtooth(1)
ModFuncSawtooth(3)
ModFuncSawtooth(30)