# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:52:21 2020

@author: pbuttles
"""
#Paul Buttles, HW1p1, 08/22/2020

#importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#defining the plot_tanh function
def plot_tanh(xlim,dx):
    x = np.arange(-1*xlim,xlim,dx) #creating the range from -xlim to xlim, divided along the mesh dx
    plt.plot(x,np.tanh(x)) #plots tanh(x) along the mesh
    plt.xlabel('x-axis') #x-axis label
    plt.ylabel('y-axis') #y-axis label
    plt.legend(['mesh size = ' + str(dx)]) #creates a legend specific to mesh size dx
    plt.show() #update with labels and legend
    return 

#defining the plot_tanh2 function
def plot_tanh2(a):
    meshsize = 0.01
    x = np.arange(-5,5,meshsize) #creates mesh with a fixed meshsize and range
    plt.plot(x,np.tanh(a*x)) #plots tanh(ax) along the mesh
    plt.xlabel('x-axis') #x-axis label
    plt.ylabel('y-axis') #y-axis label
    plt.legend(['a = 0.5','a = 1.3','a = 2.2']) #creates legend for all three plots
    return

#plots tanh with xlim = +-3, dx = 1, 0.3, 0.1, 0.01 on separate graphs
plot_tanh(3,1)
plot_tanh(3,0.3)
plot_tanh(3,0.1)
plot_tanh(3,0.01)

#plots tanh2 with a = 0.5, 1.3, 2.2 on the same graph
plot_tanh2(0.5)
plot_tanh2(1.3)
plot_tanh2(2.2)
