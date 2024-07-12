# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:51:25 2020

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt

image = plt.imread("HW08image.jpg") # imports the image data as an array of uint8
plt.imshow(image, cmap="Greys_r") # displays image in greyscale
plt.show()

imageFFT = np.fft.fft2(image) # performs a 2D fourier transform on the image data
plt.imshow(np.log(np.abs(imageFFT)), cmap="Greys_r") # displays the log of the absolute value of the complex-valued fourier transformed image
plt.show()

deltak = 1 # the delta k is one pixel

mask = np.zeros((1100,1100)) # generates a 1100x1100 array to be used for the mask
for i in range(1100): # 
    for j in range(1100):
        if (i-550)**2 + (j-550)**2 < (30*deltak)**2: # finds all (i,j) such that their distance from the center, (550,550), is less than the radius n*deltak squared
            mask[i][j] = 1 # sets these values equal to one, keeping them in the mask
        else:
            mask[i][j] = 0 # filters the rest of the data from the mask

maskshift = np.fft.ifftshift(mask) # shifts the circular mask to the outside corners as desired
plt.imshow(maskshift, cmap="Greys_r") # displays the final image of the mask
plt.show()

maskedimageFFT = imageFFT*maskshift # multiplies the image fourier transform by the final mask to filter out undesired data
maskedimage = np.abs(np.fft.ifft2(maskedimageFFT)) # inverse fourier transforms the iamge fourier transform to return the masked image
plt.imshow(maskedimage, cmap="Greys_r") # displays the low passed image
plt.show()

highpass = (mask-1)*-1 # shifts all 0 to -1, and all 1 to 0, then multiplies by -1 to invert the values of the mask
highpassimage = np.abs(np.fft.ifft2(imageFFT*np.fft.ifftshift(highpass))) # applies the highpass mask, inverse fourier transforms, and returns the high passed image
plt.imshow(highpassimage, cmap="Greys_r") # displays the high passed image
plt.show()

# replica of the code above but with slight modifications to make it easily repeatable for arbitrary aperature size n
# all code is effectively the same, and as such re-commenting would be superfluous
def lowAndHighPass(n):
    mask = np.zeros((1100,1100))
    for i in range(1100):
        for j in range(1100):
            if (i-550)**2 + (j-550)**2 < (n*deltak)**2:
                mask[i][j] = 1
            else:
                mask[i][j] = 0

    maskshift = np.fft.ifftshift(mask)
    maskedimageFFT = imageFFT*maskshift
    maskedimage = np.abs(np.fft.ifft2(maskedimageFFT))
    plt.imshow(maskedimage, cmap="Greys_r")
    plt.title("n = " + str(n))
    plt.show()

    highpass = (mask-1)*-1
    highpassimage = np.abs(np.fft.ifft2(imageFFT*np.fft.ifftshift(highpass)))
    plt.imshow(highpassimage, cmap="Greys_r")
    plt.title("n = " + str(n))
    plt.show()
    return

lowAndHighPass(10) # displays low and high pass filter for n = 10
lowAndHighPass(30) # displays low and high pass filter for n = 30
lowAndHighPass(100) # displays low and high pass filter for n = 100
lowAndHighPass(300) # displays low and high pass filter for n = 300