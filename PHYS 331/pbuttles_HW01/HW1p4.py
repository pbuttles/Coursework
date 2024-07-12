# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:31:34 2020

@author: pbuttles
"""

# Template File for Homework 1, Problem 4
# PHYS 331
# Amy Oldenburg
#-------------------------------------
import numpy as np
def calcSum_16bit(delta):
    sum = np.float16(0.0)
    delta = np.float16(delta)  # Convert delta to a 16-bit floating point number.

    if delta == np.float16(0.0):  # If the 16-bit representation is exactly zero, throw an error.
        print("Error: delta = " + str(delta) + " is equal to zero at this precision of 16 bits.")
        return

    for i in range(0, int(round(1.0 / delta))):  # Compute the sum using a for loop.
        sum += delta
    return sum

def calcSum_32bit(delta):
    sum = np.float32(0.0)
    delta = np.float32(delta)  # Convert delta to a 32-bit floating point number.

    if delta == np.float32(0.0):  # If the 32-bit representation is exactly zero, throw an error.
        print("Error: delta = " + str(delta) + " is equal to zero at this precision of 32 bits.")
        return

    for i in range(0, int(round(1.0 / delta))):  # Compute the sum using a for loop.
        sum += delta
    return sum

def calcSum_64bit(delta):
    sum = np.float64(0.0)
    delta = np.float64(delta)  # Convert delta to a 64-bit floating point number.

    if delta == np.float64(0.0):  # If the 64-bit representation is exactly zero, throw an error.
        print("Error: delta = " + str(delta) + " is equal to zero at this precision of 64 bits.")
        return

    for i in range(0, int(round(1.0 / delta))):  # Compute the sum using a for loop.
        sum += delta
    return sum
#--------------------------------
#Paul Buttles, HW1p4, 08/22/2020

#define a function to test the 16-, 32-, and 64-bit computation values of 1
def testfunc(delta):
    print('delta = ' + str(delta) + ', 16 bit, 1 = ' + str(calcSum_16bit(delta))) #labels and outputs 16-bit test
    print('delta = ' + str(delta) + ', 32 bit, 1 = ' + str(calcSum_32bit(delta))) #labels and outputs 32-bit test
    print('delta = ' + str(delta) + ', 64 bit, 1 = ' + str(calcSum_64bit(delta))) #labels and outputs 64-bit test
    return

#execute function for 10^-1,10^-2,...,10^-6
testfunc(10**-1)
testfunc(10**-2)
testfunc(10**-3)
testfunc(10**-4)
testfunc(10**-5)
testfunc(10**-6)

#16-bit limit
#testfunc(10**-8)
#32-bit limit
#testfunc(10**-46)
#64-bit soft limit
#testfunc(10**-309)
#64-bit hard limit
#testfunc(10**-324)
    