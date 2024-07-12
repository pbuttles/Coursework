# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:42:23 2020

@author: pbuttles
"""

import numpy as np

### Problem 1 of PS2.2, Part 1A ###
a = np.array([[3,-3,3],[-3,5,1],[3,1,5]]) # assigning the given matrix a
b = np.array([9,-7,12]) # assigning the given matrix b
x = np.linalg.solve(a,b) # using np.linalg.solve to solve for x in ax=b
print("Problem 1 x vector = " + str(x))

### Problem 1 of PS2.2, Part 1B ###
residuals = np.dot(a,x) - b # calculates the residuals by taking the difference between ax and b, which should be 0
print("Problem 1 residuals = " + str(residuals))
print()

### Problem 2 of PS2.2, Part 1A ###
a = np.array([[4,8,20],[8,13,16],[20,16,-91]]) # assigning the given matrix a
b = np.array([24,18,-119]) # assigning the given matrix b
x = np.linalg.solve(a,b) # using np.linalg.solve to solve for x in ax=b
print("Problem 2 x vector = " + str(x))

### Problem 2 of PS2.2, Part 1A ###
residuals = np.dot(a,x) - b # calculates the residuals by taking the difference between ax and b, which should be 0
print("Problem 2 residuals = " + str(residuals))
print()

### Problem 17 of PS2.2, Part 1E ###
R = 5 #this is the given resistor value of 5 ohms
a = np.array([[50 + R,-1,-30],[-1,65 + R,-15],[-30,-15,45]]) # this is the system of equations corresponding to i1, i2, i3
b = np.array([0,0,120]) # this is the right hand side of the system of equations
a_inv = np.linalg.inv(a) # this is the inverse of the a matrix
x = np.dot(a_inv,b) # this comes from ax=b, a_inv*ax=a_inv*b, thus x = a_inv*b
print("Problem 17 currents (220V) = " + str(x))

residuals = np.dot(a,x) - b # calculates the residuals by taking the difference between ax and b, which should be 0
print("Problem 17 residuals (220V) = " + str(residuals))
print()

### Problem 17 of PS2.2, Part 1F ###
#only values on the righthand side are being changed, thus only b needs to be modified
b = np.array([60,0,0]) # new b vector with update 60V
x = np.dot(a_inv,b) #from derivation given
print("Problem 17 currents (60V) = " + str(x))

residuals = np.dot(a,x) - b # calculates the residuals by taking the difference between ax and b, which should be 0
print("Problem 17 residuals (60V) = " + str(residuals))
print()

b = np.array([30,0,0]) # new b vector with update 30V
x = np.dot(a_inv,b) #from derivation given
print("Problem 17 currents (30V) = " + str(x))

residuals = np.dot(a,x) - b # calculates the residuals by taking the difference between ax and b, which should be 0
print("Problem 17 residuals (30V) = " + str(residuals))