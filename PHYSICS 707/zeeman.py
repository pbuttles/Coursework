# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 23:28:12 2023

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

delta = np.array([-2.0,-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5,2.0])

position = np.array([[[1159,939],[1152,956],[1151,970],[1154,985],[1154,998],[1150,1011],[1153,1024],[1154,1035],[1153,1048]],[[1164,1078],[1164,1087],[1164,1096],[1159,1105],[1159,1115],[1164,1124],[1168,1133],[1161,1141],[1165,1150]],[[1161,1173],[1158,1180],[1159,1188],[1163,1195],[1164,1203],[1159,1210],[1161,1217],[1165,1224],[1167,1232]],[[1160,1251],[1159,1257],[1158,1264],[1162,1270],[1165,1277],[1163,1283],[1164,1289],[1164,1295],[1167,1301]]])
midpoint = np.array([1191,732])

radius2 = []

# Calculating our Radius2 values
for i in range(len(position)):
    radius2singleorder=[]
    for j in range(len(position[0])):
        distance = position[i][j] - midpoint
        radius2singleorder.append(distance[0]**2+distance[1]**2)
    radius2.append(radius2singleorder)

# Calculate uncertainty in Radius2
sigmaradius2 = []
for i in range(len(radius2)):
    for j in range(len(radius2[0])):
        sigmaradius2.append(np.ceil(6*(np.sqrt(radius2[0]))))

# Calculating epsilon for each delta by p vs rp^2
epsilon = []
for j in range(len(radius2[0])):
    r2 = []
    sigmar2 = []
    p = [1,2,3,4]
    for i in range(len(radius2)):
        r2.append(radius2[i][j])
        sigmar2.append(sigmaradius2[i][j])
    plt.scatter(r2,p)
    slope,intercept,rval,pval,stderr = stats.linregress(r2,p)
    e = 1-intercept
    epsilon.append(e)
    plt.errorbar(r2,p,xerr=sigmar2, ls='none')
    plt.xlabel("Radius Squared ($R_p^2$)")
    plt.ylabel("Ring Order (p)")
    plt.suptitle("Ring Order vs. Radius Squared for $\delta$ = " + str(delta[j]))
    plt.plot(range(0,r2[-1]),slope*range(0,r2[-1])+intercept)
    # Rounding to 3 sig figs
    slope = '%s' % float('%.3g' % slope)
    intercept = '%s' % float('%.3g' % intercept)
    stderr = '%s' % float('%.3g' % stderr)
    dispeps = '%s' % float('%.3g' % epsilon[j])
    plt.title("y = " + str(slope) + "x + " + str(intercept) + ", $\sigma$ = " + str(stderr) + ", $\epsilon$ = " + str(dispeps))
    plt.show()
    
# Calculating Bohr magneton and charge/mass ratio from epsilon vs delta
plt.scatter(delta,epsilon)
slope,intercept,rval,pval,stderr = stats.linregress(delta,epsilon)
# Rounding to two sigfigs
if round(stderr,2) == 0:
    stderr = 0.01
else:
    stderr = round(stderr,2)
plt.errorbar(delta,epsilon,yerr = stderr,ls='none')
plt.suptitle("$\epsilon$ vs. $\delta$")
plt.plot(range(-2,3),range(-2,3)*slope + intercept)
slope = '%s' % float('%.2g' % slope)
intercept = '%s' % float('%.2g' % intercept)
stderr = '%s' % float('%.2g' % stderr)
plt.title("y = " + slope + "x + " + intercept + ", $\sigma$ = " + stderr)
plt.xlabel("$\delta$")
plt.ylabel("$\epsilon$")
plt.show()
    
# Physical constants and experimental measurements
h = 6.62607015*10**(-34) #J/Hz
c = 299792458 #m/s
t = 0.0046 #m
sigmat = 0.000005 #m
B = 4650 #Gauss
B = B*0.0001 #Tesla
sigmaB = 31 #Gauss
sigmaB = sigmaB*0.0001 #Tesla

# Calculating the Bohr magneton and comparing to accepted value
mu_B = (float(slope)*h*c)/(2*t*B)
print("Measured mu_B: " + str(mu_B))
sigmamu_B = mu_B*np.sqrt((float(0.01)/float(slope))**2 + (sigmat/t)**2 + (sigmaB/B)**2)
print("sigma_mu_B: " + str(sigmamu_B))
acceptedmagneton = 9.2740100783*10**(-24)
print("Percent Error in mu_B: " + str(100*(mu_B-acceptedmagneton)/acceptedmagneton))
print("")

#Calculating the charge-mass ratio of an electron and comparing to accepted value
cmr = (2*mu_B)/(1.054571817*10**(-34))
print("Measured e/me: " + str(cmr))
sigmacmr = (2*sigmamu_B)/(1.054571817*10**(-34))
print("sigma_e/me: " + str(sigmacmr))
acceptedcmr = 1.75882001076*10**11
print("Percent Error in e/me: " + str(100*(cmr-acceptedcmr)/acceptedcmr))