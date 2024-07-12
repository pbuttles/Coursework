# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:43:36 2020

@author: pbuttles
"""
import numpy as np

#this proved to be very helpful to have. rather than rewriting a new algorithm for upper triangular matrices,
#I simply use the lower triangular solving algorithm after I manipulate A and b to be lower triangular through
#regular row operations. The mathematics are completely preserved and it made for a bit less work. We can't use 
#built in functions, so I wrote up this (probably somewhat inefficient) function that flips a list. That way, 
#I can flip the entirety of A, then flip its sublists, flip b, and I have a lower triangular matrix that solves
#for a (flipped) version of the appropriate x vector
def listflip(matrix):
    flipped = []
    for q in range(1,len(matrix)+1):
        flipped.append(matrix[-q])
    return flipped

#this function takes an input matrix A, input vector b, and 0 for lower/1 for upper triangular matrix, and solves for x
def triSolve(A,b,upperOrLower):
    if upperOrLower == 1: #checks if this is an upper tri matrix
        b = listflip(b) #flips the b column vector vertically
        A = listflip(A) #flips the whole list of A, essentially flipping the matrix vertically
        for k in range(len(A)): #for loop flips each of the sublists in A, essentially flipping the matrix horizontally
            A[k] = listflip(A[k])
    x = [b[0]/A[0][0]] #computes x_0 and stores it in a list, which is particularly helpful for the algorithm referencing prior values of x
    c = 0 #initializing c
    for i in range(1,len(A)): #because the first element in x is already found, this is summed from an index of 1 (thus 2nd element) to the end of the matrix
        for j in range(i): #sums up A(ij)*x(j) from 0 to i and adds it to the variable c to be used in the external for loop its inside of
            c += A[i][j] * x[j] 
        xi = (b[i] - c) / A[i][i] #computes the rest of the algorithm using the respective values for c to find xi
        x.append(xi) #appends the found xi to the x vector
        c = 0 #resets c to zero for each iteration
    if upperOrLower == 1:
        x = listflip(x) #if the input was upper triangular, the output comes out flipped, and must be unflipped
    return x

#computes the residuals between A, the found x vector, and b by taking the difference Ax-b=0
def checkSolve(A,x,b):
    residuals = np.dot(A,x) - b
    return residuals

##### Equation 1 #####
A = [[9,0,0],[-4,2,0],[1,0,5]] #given
b = [8,1,4] #given

x = triSolve(A,b,0) #computes x from A,b
res = checkSolve(A,x,b) #checks residuals
print(np.average(res))

##### Equation 2 #####
A = [[2,4,5],[0,2,-4],[0,0,5]] #given
b = [-4,9,4] #given

x = triSolve(A,b,1) #computes x from A,b
res = checkSolve(A,x,b) #checks residuals
print(np.average(res))

#this function uses np.random.randint to produce nxn matrices with random integers from 1 to 20
def matrixRandomizer(n,upperOrLower):
    A = [] #initializing the A matirix
    for d in range(n):
        A.append([]) #appends sublists (columns) according to matrix size nxn
    for e in range(n):
        for f in range(n): 
            A[e].append(np.random.randint(1,20)) #appends n random integers to a sublist, cycles through the n sublists, thus creating a full random matrix
    if upperOrLower == 0: #with the full matrix, it now sets necessary elements to 0 to become lower triangular
        for d in range(n): #cycles through every row
            for e in range(d+1,n): #cycles through every column, setting every element from one after the diagonal (d,d) through the end of the row equal to zero, thus lower triangular
                A[d][e] = 0 #sets these elements as zero
    if upperOrLower == 1: #with the full matrix, it now sets necessary elements to 0 to become lower triangular
        for d in range(n): #cycles through every row
            for e in range(d): #cycles through every column, setting one additional element to zero with every row, thus upper triangular
                A[d][e] = 0
    return A

#this function generates a random column vector b using the same random.randint function
def bRandomizer(n):
    b = []
    for l in range(n):
        b.append(np.random.randint(1,20))
    return b

n = 3
A = matrixRandomizer(n,0)
b = bRandomizer(n)
x = triSolve(A,b,0)
res = checkSolve(A,x,b)
print(np.average(res))

n = 10
A = matrixRandomizer(n,1)
b = bRandomizer(n)
x = triSolve(A,b,1)
res = checkSolve(A,x,b)
print(np.average(res))

n = 30
A = matrixRandomizer(n,1)
b = bRandomizer(n)
x = triSolve(A,b,1)
res = checkSolve(A,x,b)
print(np.average(res))

n = 100
A = matrixRandomizer(n,1)
b = bRandomizer(n)
x = triSolve(A,b,1)
res = checkSolve(A,x,b)
print(np.average(res))
