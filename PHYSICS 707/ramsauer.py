# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 20:22:48 2023

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt
    
# Importing data and building arrays
xenon = np.genfromtxt("ramsauer without nitrogen 8.1.csv",delimiter=',',dtype=float)[1:]
noxenon = np.genfromtxt("ramsauer  with nitrogen 8.1.csv",delimiter=',',dtype=float)[1:]
vp = []
vpstar = []
vvs = []
vvsstar = []
vs = []
vsstar = []
for i in range(len(xenon)):
    vp.append(xenon[i][0])
    vpstar.append(noxenon[i][0])
    vvs.append(xenon[i][1])
    vvsstar.append(noxenon[i][1])
    vs.append(xenon[i][2])
    vsstar.append(noxenon[i][2])
vp = np.array(vp)
vpstar = np.array(vpstar)
vvs = np.array(vvs)
vvsstar = np.array(vvsstar)
vs = np.array(vs)
vsstar = np.array(vsstar)

# Calculating Ip, Ipstar
rp = 10000 #ohms
Ip = vp/rp
Ipstar = vpstar/rp
muIp = Ip*10**6 # muA
muIpstar = Ipstar*10**6 #muA

# Plotting Ip,Ipstar vs sqrt(V-Vs)
plt.plot(np.sqrt(vvs),muIp,'-o')
plt.plot(np.sqrt(vvsstar),muIpstar,'-o')
plt.xlabel("$\sqrt{V-V_s}$ ($V^{1/2}$)")
plt.ylabel("Plate current $I_p$ and $I_p^*$ ($\mu$A)")
plt.title("$I_p$ and $I_p^*$ vs. $\sqrt{V-V_s}$")
plt.legend(["$I_p$, with xenon","$I_p^*$, xenon frozen out","",""])
plt.show()
plt.plot(np.sqrt(vvs[0:20]),muIp[0:20],'-o')
plt.plot(np.sqrt(vvsstar[0:20]),muIpstar[0:20],'-o')
plt.xlabel("$\sqrt{V-V_s}$ ($V^{1/2}$)")
plt.ylabel("Plate current $I_p$ and $I_p^*$ ($\mu$A)")
plt.title("$I_p$ and $I_p^*$ vs. $\sqrt{V-V_s}$")
plt.legend(["$I_p$, with xenon","$I_p^*$, xenon frozen out","",""])
plt.show()

# Calculating T and plotting against V-Vs and sqrt(V-Vs)
T = (vp*vsstar)/(vs*vpstar)
vpsigma = 0.001
vsstarsigma = 0.001
vssigma = 0.001
vpstarsigma = 0.001
Tsigma = T*np.sqrt((vpsigma/vp)**2 + (vsstarsigma/vsstar)**2 + (vssigma/vs)**2 + (vpstarsigma/vpstar)**2)
print(T)
print(Tsigma)
plt.plot(np.sqrt(vvs),T,'-o')
plt.title("Transmission probability T vs. $\sqrt{V-V_s}$")
plt.xlabel("$\sqrt{V-V_s}$ ($V^{1/2}$)")
plt.ylabel("Transmission probability T")
plt.errorbar(np.sqrt(vvs),T,yerr=Tsigma,fmt='none',ecolor='black',capsize=1.0)
plt.show()
plt.plot(np.sqrt(vvs)[0:16],T[0:16],'-o')
plt.title("Transmission probability T vs. $\sqrt{V-V_s}$")
plt.xlabel("$\sqrt{V-V_s}$ ($V^{1/2}$)")
plt.ylabel("Transmission probability T")
plt.errorbar(np.sqrt(vvs)[0:16],T[0:16],yerr=Tsigma[0:16],fmt='none',ecolor='black',capsize=1.0)
peak = (np.sqrt(vvs)[5]+np.sqrt(vvs)[7])/2
plt.axvline(peak,color='orange',label="Peak at " + str(round(peak,6)))
plt.legend()
plt.show()
plt.plot(vvs,T,'-o')
plt.title("Transmission probability T vs. $V-V_s$")
plt.xlabel("$V-V_s$ ($V$)")
plt.ylabel("Transmission probability T")
plt.errorbar(vvs,T,yerr=Tsigma,fmt='none',ecolor='black',capsize=1.0)
plt.show()
plt.plot(vvs[0:16],T[0:16],'-o')
plt.title("Transmission probability T vs. $V-V_s$")
plt.xlabel("$V-V_s$ ($V$)")
plt.ylabel("Transmission probability T")
plt.errorbar(vvs[0:16],T[0:16],yerr=Tsigma[0:16],fmt='none',ecolor='black',capsize=1.0)
peaksqrt = (vvs[5]+vvs[7])/2
plt.axvline(peaksqrt,color='orange',label="Peak at " + str(round(peaksqrt,6)))
plt.legend()
plt.show()

print()
