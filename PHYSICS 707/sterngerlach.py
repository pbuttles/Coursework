# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:34:26 2023

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

# Importing data
sg = np.genfromtxt("Stern.dat")
sg = sg[2:]

# Building arrays
position = []
Boff = []
sigmaBoff = []
Bon = []
sigmaBon = []
background = []
sigmabackground = []
for i in range(len(sg)):
    position.append(sg[i][0])
    Boff.append(sg[i][1])
    sigmaBoff.append(sg[i][2])
    Bon.append(sg[i][3])
    sigmaBon.append(sg[i][4])
    background.append(sg[i][5])
    sigmabackground.append(sg[i][6])
position = np.array(position)
Boff = np.array(Boff)
sigmaBoff = np.array(sigmaBoff)
Bon = np.array(Bon)
sigmaBon = np.array(sigmaBon)
background = np.array(background)
sigmabackground = np.array(sigmabackground)

plt.plot(position,Boff,'-o',label="Signal")
plt.plot(position,background,'-o',label="Background")
plt.errorbar(position,Boff,yerr=sigmaBoff,capsize=1.0,fmt='none',ecolor='black')
plt.errorbar(position,background,yerr=sigmabackground,capsize=1.0,fmt='none',ecolor='black')
plt.xlabel("Position (mils)")
plt.ylabel("Detector Current (pA)")
plt.title("Detector Current vs. Position, B Field off")
plt.legend()
plt.show()

plt.plot(position,Bon,'-o',label="Signal")
plt.plot(position,background,'-o',label="Background")
plt.errorbar(position,Bon,yerr=sigmaBon,capsize=1.0,fmt='none',ecolor='black')
plt.errorbar(position,background,yerr=sigmabackground,capsize=1.0,fmt='none',ecolor='black')
plt.xlabel("Position (mils)")
plt.ylabel("Detector Current (pA)")
plt.title("Detector Current vs. Position, B Field on")
plt.legend()
plt.show()

# Computing and removing background, propagate uncertainty
background = np.nanmean(background)
sigmabackground = np.nanmean(sigmabackground)
Boff -= background
Bon -= background
#sigmaBoff = np.ceil(np.sqrt(sigmaBoff**2 + sigmabackground**2)*100)/100
#sigmaBon = np.ceil(np.sqrt(sigmaBon**2 + sigmabackground**2)*100)/100
sigmaBoff = np.sqrt(sigmaBoff**2 + sigmabackground**2)
sigmaBon = np.sqrt(sigmaBon**2 + sigmabackground**2)

plt.plot(position,Boff,'-o')
plt.errorbar(position,Boff,yerr=sigmaBoff,capsize=1.0,fmt='none',ecolor='black')
plt.xlabel("Position (mils)")
plt.ylabel("Detector Current (pA)")
plt.title("Detector Current vs. Position, B Field off (sans background)")
plt.show()

plt.plot(position,Bon,'-o')
plt.errorbar(position,Bon,yerr=sigmaBon,capsize=1.0,fmt='none',ecolor='black')
plt.xlabel("Position (mils)")
plt.ylabel("Detector Current (pA)")
plt.title("Detector Current vs. Position, B Field on (sans background)")
plt.show()

plt.plot(position,Boff,'-o',label="B Field off")
plt.errorbar(position,Boff,yerr=sigmaBoff,capsize=1.0,fmt='none',ecolor='black')
plt.plot(position,Bon,'-o',label="B Field on")
plt.errorbar(position,Bon,yerr=sigmaBon,capsize=1.0,fmt='none',ecolor='black')
plt.xlabel("Position (mils)")
plt.ylabel("Detector Current (pA)")
plt.title("Detector Current vs. Position (sans background)")
plt.legend()
plt.show()
