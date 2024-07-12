# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 23:03:37 2023

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import odr

# Plotting B field vs. current, for relating current to B field later
current = [0.250,0.300,0.350,0.400,0.450,0.500,0.550,0.600,0.650,0.700]
Bfield = [454,515,581,655,726,799,870,945,1019,1094]
sigmaB = [6,7,7,7,8,8,9,9,10,10]
Bslope, Bintercept, rval, pval, Bstderr = stats.linregress(current,Bfield)
plt.errorbar(current,Bfield,yerr=sigmaB,ls='none')
plt.scatter(current,Bfield)
plt.xlabel("Current (A)")
plt.ylabel("B Field (G)")
plt.suptitle("B Field (B) vs. Current (I)")
plt.title("B = " + str(int(round(Bslope))) + "$I$ + " + str(int(round(Bintercept))) + ", $\sigma_B$ = " + str(int(round(Bstderr))))
plt.plot(np.arange(0.25,0.75,0.05),Bslope*np.arange(0.25,0.75,0.05)+Bintercept)
plt.show()


# Plotting counts vs voltage, shows plateau
volts = np.arange(300,750,50)
counts = [0,0,22,26,30,31,30,56,58]
plt.plot(volts,counts)
plt.scatter(volts,counts)
plt.xlabel("Voltage (V)")
plt.ylabel("Counts")
plt.title("Counts vs. Voltage per 30s interval at 0.25A")
plt.show()

# Plotting counts vs current at 550V over 90s interval
current = np.array([0.000,0.050,0.100,0.150,0.200,0.250,0.300,0.325,0.350,0.375,0.400,0.425,0.450,0.475,0.500,0.550,0.570,0.580,0.590,0.600,0.610,0.620,0.630,0.650,0.700])
counts = [91,97,118,233,311,386,399,432,446,380,333,282,213,176,157,139,387,546,596,560,468,310,176,128,97]
backgroundcounts = [83,76,75,72,61,86,70,66,82,76,68,83,85,80,77]
avgbackgroundcounts = np.average(backgroundcounts)
sigmacounts = np.sqrt(counts + avgbackgroundcounts)
counts = counts - np.average(backgroundcounts)
plt.xlabel("Current (A)")
plt.ylabel("Counts")
plt.title("Counts vs. Current per 90s interval at 550V")
plt.errorbar(current,counts,yerr=sigmacounts,ecolor='black')
plt.show()

# Converting current to B field to energy
Bfield = current*Bslope + Bintercept
Bfield *= 0.0001 # Gauss to Tesla
sigmaB = np.round(np.sqrt((Bslope**2)*(current**2)*((Bstderr/Bslope)**2 + (0.001/current)**2) + Bstderr**2))
sigmaB[0] = 12 # accounting for I=0
sigmaB *= 0.0001 # Gauss to Tesla
e = 1.60217663*10**(-19) # Coulombs
r = 0.0381 # radius in meters
sigmar = 0.003 # m
E0 = 510998.95 # given from literature
sigmaE0 = 0.00015
c = 299790000 # speed of light
E = np.sqrt(E0**2 + (Bfield*r*c)**2) - E0
y = np.sqrt(counts/(Bfield**3))
sigmaE = ((Bfield**2)*(c**4)*(r**4)*(sigmaB**2))/(E0**2+(Bfield**2)*(c**2)*(r**2)) + ((E0/(np.sqrt(E0**2+(Bfield**2)*(c**2)*(r**2)))-1)**2)*(sigmaE0**2) + ((Bfield**4)*(c**4)*(r**2)*(sigmar**2))/(E0**2+(Bfield**2)*(c**2)*(r**2))
sigmaE = sigmaE.astype(float)
sigmaE = np.sqrt(sigmaE)
plt.scatter(E[8:14],y[8:14])
sigmay = np.sqrt((sigmacounts**2)/(4*counts*Bfield**3) + (9*counts*sigmaB**2)/(4*Bfield**5))
slope, intercept, rval, pval, stderr = stats.linregress(E[8:14],y[8:14])
plt.plot(np.arange(E[8],E[13]),slope*np.arange(E[8],E[13])+intercept,color='orange')
plt.xlabel("Energy (eV)")
plt.ylabel("$\sqrt{A/{B^3}}$ (counts/$T^3$)")
plt.suptitle("Kurie Plot")
plt.title("y = " + str(round(slope,5)) + "x + " + str(round(intercept,-1)) + ", $R^2$ = " + str(round(rval**2,3)) + ", $\sigma$ = " + str(round(stderr,6)))
plt.show()

# Calculating Kurie fit uncertainty
weightsE = 1/sigmaE**2
weightsy = 1/sigmay**2
def model(B,x):
    return B[0]*x+B[1]
odrmodel = odr.Model(model)
odrdata = odr.Data(E[8:14],y[8:14],weightsE[8:14],weightsy[8:14])
myODR = odr.ODR(odrdata,odrmodel,beta0=[0.005,3030])
result = myODR.run()
Emax = -result.beta[1]/result.beta[0] #keV
sigmaEmaxx = Emax*np.sqrt((result.sd_beta[0]/result.beta[0])**2+(result.sd_beta[1]/result.beta[1])**2) #keV

# Calculating internal conversion peak energy
peakindex = 18
p = Bfield*e*r # momentum in joules
psigma = p*np.sqrt((sigmaB/Bfield)**2 + (sigmar/r)**2)
p *= 6.242*10**18 # eV/c
psigma *= 6.242*10**18 # eV/c
print(p[peakindex])
print(psigma[peakindex])
E = np.sqrt(E0**2 + (p[peakindex]*c)**2) - E0
plt.scatter(p,counts)
plt.plot(p,counts)
plt.axvline(p[peakindex],color='orange')
plt.xlabel("Momentum p (eV/c)")
plt.ylabel("Counts")
plt.suptitle("Count rate vs. momentum p")
plt.title("Internal Conversion Peak p = " + str(round(p[18],5)) + "eV, E = " + str(int(round(E,-3)/1000)) + "keV")
