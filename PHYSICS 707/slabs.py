# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 04:17:24 2023

@author: pbuttles
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

thick = [[1.6,1.5],[3.1,2.9],[4.7,4.5],[6.3,6.1],[7.9,7.7],[9.5,9.2]]
sigmathick = [0.1,0.1,0.1,0.1,0.1,0.1]
thin = [[2.9,2.6],[5.9,5.4],[6.3,5.9],[9.6,9.1],[13.0,12.2]]
sigmathin = [0.1,0.1,0.1,0.1,0.1]

thickx = []
thinx = []

thickdiff = []
thindiff = []

for i in range(len(thick)):
    thickx.append(thick[i][0])
    thickdiff.append(thick[i][0]-thick[i][1])
    

for i in range(len(thin)):
    thinx.append(thin[i][0])
    thindiff.append(thin[i][0]-thin[i][1])
    

thinreg = stats.linregress(thinx,thindiff)
thickreg = stats.linregress(thickx,thickdiff)

print(thinreg)
print(thickreg)

    
plt.errorbar(thickx,thickdiff,yerr=sigmathick,ecolor='black',capsize=5,barsabove=False,marker='o',ls='',color='red',label='Thick slabs (0.014in)')
plt.errorbar(thinx,thindiff,yerr=sigmathin,ecolor='black',capsize=5,barsabove=False,marker='o',ls='',color='blue',label='Thin slabs (0.062in)')
plt.xlabel("Starting Height (mm)")
plt.ylabel("Compression (mm)")
plt.title("Compression vs. Starting Height")
plt.plot(np.arange(1.6,13.1,0.1),thickreg.slope*np.arange(1.6,13.1,0.1)+thickreg.intercept,
         '--',color='red',label="y = " + str(round(thickreg.slope,3)) + "x + " + str(round(thickreg.intercept,2)))
plt.plot(np.arange(1.6,13.1,0.1),thinreg.slope*np.arange(1.6,13.1,0.1)+thinreg.intercept,
         '--',color='blue',label="y = " + str(round(thinreg.slope,3)) + "x + " + str(round(thinreg.intercept,2)))
handles, labels = plt.gca().get_legend_handles_labels()
order = [2,0,3,1]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
plt.show()
    