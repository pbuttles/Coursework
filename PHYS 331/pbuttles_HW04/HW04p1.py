# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:14:30 2020

@author: pbuttles
"""

import numpy as np

# This function defines the system of equations we find the roots of
def F(x_vec): 
    x = x_vec[0] # initializing x from the input vector
    y = x_vec[1] # initializing y from the input vector
    Re = 2*(x**3) - 6*x*(y**2) - 1 # The first equation in the system is the real portion of the original equation
    Im = 6*(x**2)*y - 2*(y**3) + 3 # The second equation in the system is the imaginary portion of the original equation
    return np.array([Re,Im]) # outputs a numpy array of the system of equations

# This function defines the inverse of the jacobian of the system of equations F(x)
def Jinv(x_vec):
    x = x_vec[0] # initializing x from the input vector
    y = x_vec[1] # initializing y from the input vector
    a = 1/(36*x**4 + 72*x**2*y**2 + 36*y**4) # calculating and storing the determinant of the jacobian
    Jinv11 = a * (6*x**2 - 6*y**2) # calculating the [1,1] element of the inverse jacobian 
    Jinv21 = a * (12*x*y) # calculating the [2,1] element of the inverse jacobian
    Jinv12 = a * (-12*x*y) # calculating the [1,2] element of the inverse jacobian
    Jinv22 = a * (6*x**2 - 6*y**2) # calculating the [2,2] element of the inverse jacobian
    Jinv = np.array([[Jinv11,Jinv12],[Jinv21,Jinv22]]) # storing the four elements of the inverse jacobian in a numpy array
    return Jinv 

# This function is the 2 dimensional newton-raphson root finder
def rf_newton2d(F_system,Jinv_system,x_vec0,tol,maxiter):
    F_vector = F(x_vec0) # initializing the F vector by passing the x vector into the system of equations
    Jinv_matrix = Jinv(x_vec0) # initializing the inverse jacobian by passing the x vector into the system of equations
    err = tol + 1 # intializing the error counter as more than the tolerance for the sake of starting the while loop
    iters = 0 # initiailizing the iteration counter
    while err > tol and iters < maxiter: # looping until the error is less than the tolerance or max iterations are reached
        F_vector = F(x_vec0) #updating the F vector upon looping
        Jinv_matrix = Jinv(x_vec0) #updating the inverse jacobian upon looping
        delta1 = -1 * (Jinv_matrix[0][0]*F_vector[0] + Jinv_matrix[1][0]*F_vector[1]) # computing d = -J^(-1)*F for the first row
        delta2 = -1 * (Jinv_matrix[0][1]*F_vector[0] + Jinv_matrix[1][1]*F_vector[1]) # computing d = -J^(-1)*F for the second row
        xnew = x_vec0[0] + delta1 # computing the new x value by adding the x delta to the original x
        ynew = x_vec0[1] + delta2 # computing the new y value by adding the y delta to the original y
        err = (delta1**2 + delta2**2)**(1/2) # calculating the error between iterations based on the pythagorean distance of the deltas
        x_vec0 = np.array([xnew,ynew]) # updating the x vector with new x and y values
        iters += 1 # updating the iteration counter
    if iters == maxiter:
        print("WARNING: Max Iterations Reached") # warning message for reaching max iterations
    #print(str(iters) + " iterations")
    return x_vec0
        
print(rf_newton2d(F,Jinv,np.array([1,0]),10**(-5),20))
print(rf_newton2d(F,Jinv,np.array([-1,0]),10**(-5),20))
print(rf_newton2d(F,Jinv,np.array([0,1]),10**(-5),20))
print(rf_newton2d(F,Jinv,np.array([0,-1]),10**(-5),20))
print(rf_newton2d(F,Jinv,np.array([-1,-1]),10**(-5),20))
print(rf_newton2d(F,Jinv,np.array([1,1]),10**(-5),20))
print(rf_newton2d(F,Jinv,np.array([1,-1]),10**(-5),20))
print(rf_newton2d(F,Jinv,np.array([-1,1]),10**(-5),20))
#print(rf_newton2d(F,Jinv,np.array([0,0]),10**(-5),20)) #this does not converge
