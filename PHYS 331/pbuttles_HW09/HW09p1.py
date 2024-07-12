# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:51:13 2020

@author: pbuttles
"""

import numpy as np

A = np.random.random([4,4]) # generates random 4x4 matrix
eig = np.linalg.eig(A) # calculates eigenvalues and eigenvectors of A
lambda1 = eig[0][0] # indexes the first eigenvalue
lambda2 = eig[0][1] # indexes the second eigenvalue
lambda3 = eig[0][2] # indexes the third eigenvalue
lambda4 = eig[0][3] # indexes the fourth eigenvalue
print("lambda1 = " + str(lambda1)) # prints first eigenvalue
print("lambda2 = " + str(lambda2)) # prints second eigenvalue
print("lambda3 = " + str(lambda3)) # prints third eigenvalue
print("lambda4 = " + str(lambda4)) # prints fourth eigenvalue
P = eig[1] # indexes P matrix
w1 = eig[1][:,0] # indexes the first eigenvector 
print("Aw1 = " + str(np.dot(A,w1))) # prints the dot product of A and the first eigenvector
print("lambda1*w1 = " + str(np.dot(w1, lambda1))) # print the dot product of the first eigenvector and the first eigenvalue
print()
Pinv = np.linalg.inv(P) # takes the inverse of P
lambdamatrix = np.dot(np.dot(Pinv,A),P) # computes Pinv*A*P = lambda
print("lambda matrix: ")
print(lambdamatrix) # prints the diagonal matrix of lambdas
print()

########################
##### EXTRA CREDIT #####
########################

def GenerateHermitian(size):
    n = size
    H = np.zeros([n,n], dtype="complex") # initializes a complex nxn matrix
    for i in range(len(H)):
        H[i][i] = np.random.random(1) # writes reals along the diagonal of the matrix
    for i in range(len(H)):
        for j in range(len(H)):
            if j > i: # loops over off-diagonals
                H[i][j] = np.random.random(1) + np.random.random(1)*1j # writes random complex numbers to upper off-diagonals
                H[j][i] = np.conjugate(H[i][j]) # write complex conjugates of upper off-diagonals to lower off-diagonal transpose positions
    return H

H = GenerateHermitian(5) # generates 5x5 hermitian matrix
HermitianEigenvalues, HermitianEigenvectors = np.linalg.eig(H) # computes eigenvalues and eigenvectors of H
print("Hermitian Eigenvalues: " + str(HermitianEigenvalues)) # prints hermitian eigenvalues
orthotest = np.dot(HermitianEigenvectors[0],np.conjugate(HermitianEigenvectors[1])) # computes dot product of two eigenvectors to check for orthogonality
print(orthotest) # should be 0 within machine precision if eigenvectors are orthogonal