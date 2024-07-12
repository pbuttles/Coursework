# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:54:58 2020

@author: pbuttles
"""
#Paul Buttles, HW1p3, 08/22/2020

outary = [] #create some empty python array "outary"
#define maskn function that takes a python array "ary" and some integer to sort for "i"
def maskn(ary,i):
    for a in ary: #checks each element "a" in the list
        if a % i == 0: #checks if element "a" is divisible by i
            outary.append(1) #writes divisible element to be 1
        if a % i != 0: #checks if element "a" is not divisible by i
            outary.append(0) #writes indivisible element to be 0
    return outary
