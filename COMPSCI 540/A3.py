# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:33:43 2024

@author: pbuttles
"""

"""Code Attribution: All coded myself as far as I'm aware"""

import numpy as np
import numpy.linalg as lg
import pyperclip as pp

# Create first axes (1,0,...,0),(0,1,...,0),...,(0,0,...,1)
print("Question 1")
axes = []
for i in range(25):
    q = np.zeros(784)
    q[i] = 1
    #print(",".join([str(int(x)) for x in q]))
    axes.append(q)
print('\n\n\n')



# Import test data
global test
filepath = "test.txt"
test = np.genfromtxt(filepath,delimiter=",")
test /= 255
test = test # analysis:ignore


# Project test data onto first axes
proj1 = []
for i in range(len(test)):
    proj = []
    for k in range(25):
        proj.append(np.dot(test[i],axes[k]))
    proj1.append(proj)
print("Question 2")
#for i in range(len(proj1)):
#    print(",".join([str(x) for x in proj1[i]]))
print('\n\n\n')

# Reconstruct test data 
recon1 = np.zeros([len(test),len(test[0])])
for i in range(len(recon1)):
    for j in range(len(proj1)):
        for k in range(len(proj1[j])):
            recon1[i][k] = proj1[j][k]
print("Question 3")
#for i in range(len(recon1)):
#    print(",".join([str(x) for x in recon1[i]]))
print('\n\n\n')

# Could not get PCA to work, using given PCA
'''
# Construct principle axes
# Calculate X
bigX = test
mu = np.mean(test,axis=0)
        
# Calculate Sigma
sigma = np.cov(bigX-mu,rowvar=False)
#sigma = np.transpose(bigX)@bigX

#Find eigenvalues/vectors, sort, and round
evals,evecs = lg.eig(sigma)
evals = evals.real
evecs = evecs.real

idx = evals.argsort()[::-1]   
evals = evals[idx]
evecs = evecs[:,idx]
evecs = np.around(evecs,4)
#print(evecs[0])

for i in range(len(evecs)): 
    evecs[i] /= lg.norm(evecs[i])
paste = ''
#pca=[]
#for i in range(25):
#    paste += ','.join([str(x) for x in np.around(evecs[i],4)])
#    paste += '\n'
#    pca.append(np.around(evecs[i],4))
#pp.copy(paste)
'''
        

# Find PCA features by projecting images onto PCAs, resulting in lengths
pcafilepath = "pca.txt"
pca = np.genfromtxt(pcafilepath,delimiter=",")
proj2 = []
for i in range(len(test)):
    proj = []
    for k in range(len(pca)):
        proj.append(round(np.dot(pca[k],test[i]),4))
    proj2.append(proj)
print("Question 5")
#for i in range(len(proj2)):
#    print(",".join([str(x) for x in proj2[i]]))
print('\n\n\n')
#paste = ''
#for proj in proj2:
#    paste += ','.join([str(x) for x in np.around(proj,4)])
#    paste += '\n'
#pp.copy(paste)

# Reconstruct images by weighting pcas by pca features/lengths and summing
recon2 = []
for i in range(len(proj2)):
    reconxi = np.dot(proj2[i],pca)
    recon2.append(reconxi)
print("Question 6")
#for i in range(len(recon2)):
#    print(",".join([str(x) for x in recon2[i]]))
print('\n\n\n')
#paste = ''
#for recon in recon2:
#    paste += ','.join([str(x) for x in np.around(recon,4)])
#    paste += '\n'
#pp.copy(paste)
        


    


# Import MNIST data, truncated to 1000 images
filepath = "mnist_train_truncated.csv"
data = np.genfromtxt(filepath,delimiter=',')
data = data[:,1:]
data = data/255
projdata = []
for i in range(len(data)):
    proj = []
    for k in range(len(pca)):
        proj.append(round(np.dot(pca[k],data[i]),4))
    projdata.append(proj)

# Defines Euclidean distance
def edist(x1,x2):
    if type(x1)==list:
        x1=np.array(x1)
    if type(x2)==list:
        x2=np.array(x2)
    return np.sqrt(sum((x1-x2)**2))

# Compare instruction data features to MNIST features, find smallest distance
# Return MNIST feature closest to each instruction feature (Q7)
# Return MNIST images corresponding to each closest feature (Q8)
neighborfeatures = []
neighborimages = []
for i in range(len(proj2)):
    mindist = edist(proj2[i],projdata[0])
    minind = 0
    for j in range(len(projdata)):
        newdist = edist(proj2[i],projdata[j])
        if newdist < mindist:
            mindist = newdist
            minind = j
    neighborfeatures.append(projdata[minind])
    neighborimages.append(data[minind])

print("Question 7")
#for i in range(len(neighborfeatures)):
#    print(",".join([str(x) for x in neighborfeatures[i]]))
print('\n\n\n')
#paste=''
#for i in range(len(neighborfeatures)):
#    paste += ",".join([str(x) for x in np.around(neighborfeatures[i],4)])
#    paste+='\n'
#pp.copy(paste)
print("Question 8")
#for i in range(len(neighborimages)):
#    print(",".join([str(x) for x in neighborimages[i]]))
print('\n\n\n')
#paste=''
#for i in range(len(neighborimages)):
#    paste += ",".join([str(x) for x in np.around(neighborimages[i],4)])
#    paste+='\n'
#pp.copy(paste)




# Reconstructing data from the nearest neighbor PCA features
recondata = []
for i in range(len(neighborfeatures)):
    reconxi = np.dot(neighborfeatures[i],pca)
    recondata.append(np.around(reconxi,4))
print("Question 9")
#for i in range(len(recondata)):
#    print(",".join([str(x) for x in recondata[i]]))
print('\n\n\n')
#paste = ''
#for recon in recondata:
#    paste += ','.join([str(x) for x in np.around(recon,4)])
#    paste += '\n'
#pp.copy(paste)
