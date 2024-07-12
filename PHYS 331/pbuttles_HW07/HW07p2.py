# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:10:06 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

R_A_array = np.zeros(1000) # initializes the array of R_A values
C_A_array = np.zeros(1000) # initialiizes the array of condition numbers
residual_norm_array = np.zeros(1000) # initializes the array of residual norms

for i in range(1000):
    A = np.random.randn(10,10) # defines random 10x10 A matrix
    b = np.random.randn(10,1) # defines random 10X1 column vector b
    Ainv = np.linalg.inv(A) # takes inverse of A matrix
    x = np.dot(Ainv,b) # calculated x from Ax=b by x = Ainv * b
    r = np.dot(A,x)-b # calculates residual from r = Ax-b
    R_A_array[i] = np.abs(np.linalg.det(A))/np.abs(np.linalg.norm(A)) # calculates the ratio of |det(A)|/norm(A), stores in array
    C_A_array[i] = np.linalg.norm(A)*np.linalg.norm(Ainv) # calculates condition number |A|*|Ainv|, stores in array
    residual_norm_array[i] = np.linalg.norm(r) # calculates norm of residual, stores in arrray

plt.scatter(np.log(C_A_array),np.log(R_A_array)) # plots log of the ratio vs log of condition number
plt.title("R_A vs. Conditional")
plt.xlabel("Condition Number")
plt.ylabel("|det(A)|/norm(A)")
plt.show()

plt.scatter(np.log(C_A_array),np.log(residual_norm_array)) # plots log of residual norm vs log of condition number
plt.title("Residual norm vs. Conditional")
plt.xlabel("Condition Number")
plt.ylabel("Norm of Residual")
plt.show()