# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 17:47:46 2020

@author: pbuttles
"""
#Paul Buttles, HW1p2, 08/22/2020

#homemade factorial function for convenience and efficiency
def myfactorial(n):
    fn = n #defining a separate fn to be modified so the original n remains unchanged for use in line 17
    if n == 0: #special case of 0!=1
        fn = 1
    if n != 0: #general case, repeatedly multiply terms substracting by 1 until being multiplied by 1
        while n > 1:
            n = n-1
            fn = fn*n
    return fn

#defining sin_taylor function that takes the nth term of the nth order expansion of sin around x0
def sin_taylor(x0,n):
    if n == 0 or n < 0: #displays an error message for non-positive order inputs
        return 'ERROR: non-positive order expansion'
    if n > 0:
        if (n % 2) == 1: #sorting for odd values of n
            if (n % 4) == 1: #terms 1, 5, 9, ... are positive
                j=1
            if (n % 4) == 3: #terms 3, 7, 11, ... are negative
                j=-1
            yn = x0**n*j/myfactorial(n) #compute non-zero term
        if (n % 2) == 0: #sorting for even values of n
            yn = 0 #even order terms are always 0 for taylor expansion of sinx
    return yn
