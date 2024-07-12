# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:05:22 2024

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt
import qutip
from qutip import (Qobj, about, basis, coherent, coherent_dm, create, destroy,
                   expect, fock, fock_dm, mesolve, qeye, sigmax, sigmay,
                   sigmaz, tensor, thermal_dm, Bloch)

ipsi=Qobj([[1],[0]])
iipsi=Qobj([[1],[1]]).unit()
iiipsi=Qobj([[1/np.sqrt(2)],[0.5*(1+1j)]]).unit()

print("Question 3b(i):")
print("<sigmax> = "+str(expect(sigmax(),ipsi)))
print("<sigmay> = "+str(expect(sigmay(),ipsi)))
print("<sigmaz> = "+str(expect(sigmaz(),ipsi)))
print("Question 3b(ii):")
print("<sigmax> = "+str(expect(sigmax(),iipsi)))
print("<sigmay> = "+str(expect(sigmay(),iipsi)))
print("<sigmaz> = "+str(expect(sigmaz(),iipsi)))
print("Question 3b(iii):")
print("<sigmax> = "+str(expect(sigmax(),iiipsi)))
print("<sigamy> = "+str(expect(sigmay(),iiipsi)))
print("<sigmaz> = "+str(expect(sigmaz(),iiipsi)))
print("")

print("Question 3c(i):")
bloch = Bloch()
bloch.add_states(ipsi)
bloch.show()
bloch = Bloch()
bloch.add_states(iipsi)
print("")
print("Question 3c(ii):")
bloch.show()
bloch = Bloch()
bloch.add_states(iiipsi)
print("")
print("Question 3c(iii):")
bloch.show()
print("")
print("")

g=2
muB=1.4#MHz/Gauss
def H(Bx):
    B=[Bx,0,0]
    sigma=[sigmax(),sigmay(),sigmaz()]
    sigmadotB = sum(x * y for x, y in zip(sigma,B))
    H = -0.5*g*muB*sigmadotB
    return H
evals, evecs = H(Bx=100).eigenstates()
print("Question 3e:")
print("Two Eigenvalues: "+str(evals[0])+", "+str(evals[1]))
print("Two Eigenvectors:")
print(str(evals[0])+': \n'+str(evecs[0].full()))
print(str(evals[1])+': \n'+str(evecs[1].full()))
print("")

print("Question 3f:")
Bx=np.arange(0,150)
Hvalsminus=[]
Hvalsplus=[]
for i in range(len(Bx)):
    Hvalsminus.append(H(Bx[i]).eigenstates()[0][0])
    Hvalsplus.append(H(Bx[i]).eigenstates()[0][1])

plt.plot(Bx,Hvalsminus)
plt.plot(Bx,Hvalsplus)  
plt.xlabel("Magnetic Field Strength Bx (Gauss)")
plt.ylabel("Eigenvalues (MHz)")
plt.title('Hamiltonian Frequency Spectrum, \nEigenvalues (MHz) vs. Bx (Gauss)')
plt.show()