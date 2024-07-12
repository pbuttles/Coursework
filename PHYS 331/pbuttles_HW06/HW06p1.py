# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 22:06:01 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

# this function computes the Euclidean norm of a matrix as defined by the book
# it was made separate for convenience sake and debugging purposes, and is called by checkConditioning
def euclidNorm(A):
    norm = 0
    for j in range(len(A)):
        for k in range(len(A)):
            norm += A[j][k]**2
    norm = np.sqrt(norm)
    return norm

# this function takes a vector of times tvec, then computes the A matrix, the determinant, the norm, and outputs the ratio R of determinant over norm
def checkConditioning(tvec):
    A = np.array([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]]) #initializing the A matrix in Ax=b
    for i in range(len(A)): 
        A[i] = [1, tvec[i], 0.5*tvec[i]**2] # evaluates the A matrix for respective values of t from tvec
    det = np.abs(np.linalg.det(A)) # computes the determinant of A
    norm = euclidNorm(A) # computes the norm of A from the euclidNorm function written above
    R = det / norm # computes the ratio of det A to norm A
    return R

# this funtion generates a vector tvec of times over evenly spaced time intervals, starting at t=0
def evenTime(interval):
    tvec = np.array([0.,1.*interval,2.*interval])
    return tvec

Rvalues = [] # initializing a list of R values
interval = np.arange(0.1,5,0.001) # initializing the range of time intervals to be graphed over
for i in interval:
    Rvalues.append(checkConditioning(evenTime(i))) # computes R over the range of times intervals and appends to list of R values
plt.plot(interval,Rvalues) # plots R values against their respective time intervals
plt.title("R vs. delta t") # adds plot title
plt.xlabel("delta t (sec)") # adds x-axis label
plt.ylabel("R") # adds y-axis label
plt.show()

# this function generates a vector tvec of times from 0 to t2 to 10
def variableTime(t2):
    tvec = np.array([0.,1.*t2,10.])
    return tvec

Rvalues = [] # re-initializing the list of R values 
t2 = np.arange(0.1,9.9,0.01) # initializing the range of t2 values to be graphed over
for i in t2:
    Rvalues.append(checkConditioning(variableTime(i))) # computes R over the range of t2 values and appends to list of R values
plt.plot(t2,Rvalues) # plots R values against their respective t2 values
plt.title("R vs. t2") # adds plot title
plt.xlabel("t2 (sec)") # adds x-axis label
plt.ylabel("R") # adds y-axis label
plt.show()

# this function takes a vector of times, tvec, and a vector of x(t) values, b, and solves 
def solveX(tvec,b):
    A = np.array([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]]) # initializes the A matrix in Ax=b
    for i in range(len(A)):
        A[i] = [1, tvec[i], 0.5*tvec[i]**2] # evaluates the A matrix for respective values of t from tvec
    x = np.linalg.solve(A,b) # computes x from Ax=b using the built-in numpy linalg solver function
    return x

strat1 = solveX([0.,5.,10.],[0.30,4.425,14.30]) # solves for best-fit parameters given tvec and x(t) values for Strategy 1
strat2 = solveX([0.,1.,10.],[0.30,0.665,14.30]) # solves for best-fit parameters given tvec and x(t) values for Strategy 2
print("Strategy 1: x0 = " + str(strat1[0]) + ", v0 = " + str(strat1[1]) + ", a = " + str(strat1[2]))
print("Strategy 2: x0 = " + str(strat2[0]) + ", v0 = " + str(strat2[1]) + ", a = " + str(strat2[2]))

############## Part F ##############

deltax = 0.005 # given measurement accuracy value
unc = np.array([0,deltax,deltax]) # array of uncertainties in (x0,v0,a)

tvec1 = np.array([0.,5.,10.]) # given t values for Strategy 1
b1 = np.array([0.30,4.425,14.30]) # given x(t) values for Strategy 1
b1upper = b1 + unc # computes upper bound x(t) values
b1lower = b1 - unc # computes lower bound x(t) values

tvec2 = np.array([0.,1.,10.]) # given t values for Strategy 2
b2 = np.array([0.30,0.665,14.30]) # given x(t) values for Strategy 2
b2upper = b2 + unc # computes upper bound x(t) values
b2lower = b2 - unc # computes lower bound x(t) values

strat1upper = solveX(tvec1,b1upper) # solves for x values for strategy 1 upper bound b vector
strat1lower = solveX(tvec1,b1lower) # solves for x values for strategy 1 lower bound b vector
strat1error = strat1upper - strat1lower # takes upper-lower bound difference as error

strat2upper = solveX(tvec2,b2upper) # solves for x values for strategy 2 upper bound b vector
strat2lower = solveX(tvec2,b2lower) # solves for x values for strategy 2 lower bound b vector
strat2error = strat2upper - strat2lower # takes upper-lower bound difference as error
#print(strat1upper[1:3])
#print(strat1lower[1:3])
#print(strat1error[1:3])
#print(strat2upper[1:3])
#print(strat2lower[1:3])
#print(strat2error[1:3])
