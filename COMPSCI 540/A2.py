# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 18:54:04 2024

@author: pbuttles
"""

"""Code Attribution: Loosely used ChatGPT to import and set up the data but it
was fairly useless, so I used small pieces and wrote the rest. 
PROMPT: I have a csv with country information listed row by row, the first 
four columns of which identify the country, the rest of which is a time series 
containing numerical information of various length. Can you write some python 
to import this into a dictionary associating the country code in the 2nd 
column with a numpy array of the time series data?"""
"""The line np.unravel_index(x.argmin(), x.shape) was taken from Stack
Overflow Question 30180241"""

import csv
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

d = {}
filepath = "API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_474.csv"

countrycatalog=[]
with open(filepath, mode='r') as file:
    reader = csv.reader(file)
    for i in range(4): next(reader)
    years = next(reader)[4:]
    for row in reader:
        code = row[1]
        countrycatalog.append(code)
        data = row[4:]
        data_pruned = []
        for i in range(len(data)):
            if data[i] != '':
                data_pruned.append(data[i])
        data_pruned = np.array(data_pruned).astype(float)
        if len(data_pruned) > 1:
            d[code] = data_pruned
print("Question 1")
print(",".join([str(x) for x in d['USA']]))
print(",".join([str(x) for x in d['CAN']]))
print('\n\n\n')



def mean(data):
    T = len(data)
    mu = sum(data)/T
    return round(mu,4)

def stdev(data):
    T = len(data)
    mu = mean(data)
    sigma = (sum((data-mu)**2)/(T-1))**0.5
    return round(sigma,4)

def median(data):
    data = np.sort(data)
    if len(data)%2 == 1:
        med = data[int(round(len(data)/2))]
    else:
        med = (data[int(len(data)/2)]+data[int(len(data)/2-1)])/2
    return round(med,4)

def beta(data):
    T = len(data)
    t = (T+1)/2
    mu = mean(data)
    beta = sum((data - mu)*(np.arange(len(data))+1-t))/sum((np.arange(len(data))+1-t)**2)
    return round(beta,4)

def rho(data):
    mu = mean(data)
    rho = sum((data[0:len(data)-1]-mu)*(data[1:]-mu))/sum((data-mu)**2)
    return round(rho,4)



print("Question 2")
def getparams(data):
    return [mean(data),stdev(data),median(data),beta(data),rho(data)]
q2 = getparams(d['USA'])
print(",".join([str(x) for x in q2]))
q2 = getparams(d['CAN'])
print(",".join([str(x) for x in q2]))
print('\n\n\n')



n = len(d)
m = 5

p = []
for country in d:
    params = getparams(d[country])
    p.append(params)


pmin = []
pmax = []
for i in range(len(p[0])):
    pmin.append(min(np.swapaxes(np.array(p),0,1)[i]))
    pmax.append(max(np.swapaxes(np.array(p),0,1)[i]))
for i in range(len(p)):
    for j in range(len(p[0])):
        p[i][j] = round((p[i][j]-pmin[j])/(pmax[j]-pmin[j]),4)
print("Question 4")
for line in p:
    print(",".join([str(x) for x in line]))
print('\n\n\n')



# Defines Euclidean distance
def edist(x1,x2):
    return np.sqrt(sum((x1-x2)**2))

# Find Single Linkage Distance between two clusters
def single_linkage_dist(cluster1,cluster2):
    sdist = edist(cluster1[0],cluster2[0])
    for i in range(len(cluster1)):
        for j in range(len(cluster2)):
            newdist = edist(cluster1[i],cluster2[j])
            if newdist < sdist:
                sdist = newdist
    return sdist

# Find Complete Linkage Distance between two clusters
def complete_linkage_dist(cluster1,cluster2):
    cdist = edist(cluster1[0],cluster2[0])
    for i in range(len(cluster1)):
        for j in range(len(cluster2)):
            newdist = edist(cluster1[i],cluster2[j])
            if newdist > cdist:
                cdist = newdist
    return cdist


# Clusters list contains points for distance calculation and merging
# Countries list contains indices of countries to track what is being merged
clusters = []
countries = []
for i in range(len(p)):
    clusters.append([np.array(p[i])])
    countries.append([i])
countrycount = len(countries)

# Recursively calculate upper triangular matrix of distances between all 
# clusters, put max possible distance on diagonal and lower triag entries
# Find pair with smallest distance, append latter to former, delete latter
# Repeat until 7 clusters are left
def combine_clusters(clusters,method,k):
    # Stop once we reach 7 clusters
    if len(clusters) <= k:
        return
    # For ease of minimizing, dist is an "empty" array of distances greater
    # than the maximum distance, which for an n-parameter space, is sqrt(n)
    maxpossibledist = round(np.sqrt(5)+1)
    dist = np.zeros([len(clusters),len(clusters)])+maxpossibledist
    if method == 'single':
        for i in range(len(clusters)):
            for j in range(i+1,len(clusters)):
                newdist = single_linkage_dist(clusters[i],clusters[j])
                dist[i][j] = newdist
    elif method == 'complete':
        for i in range(len(clusters)):
            for j in range(i+1,len(clusters)):
                newdist = complete_linkage_dist(clusters[i],clusters[j])
                dist[i][j] = newdist
    else:
        print("ERROR: Select 'single','complete' linkage method")
        return
    pairindex = np.unravel_index(dist.argmin(), dist.shape)
    clusters[pairindex[0]] += clusters[pairindex[1]]
    clusters.pop(pairindex[1])
    countries[pairindex[0]] += countries[pairindex[1]]
    countries.pop(pairindex[1])
    combine_clusters(clusters,method,k)
    
    

# Cluster by single linkage
combine_clusters(clusters,method='single',k=7)
q5 = np.arange(countrycount)
for i in range(len(countries)):
    for j in range(len(countries[i])):
        q5[countries[i][j]] = i
print("Question 5")
print(",".join([str(x) for x in q5]))
for i in range(len(countries)):
    print("Group "+str(i+1))
    print(",".join([countrycatalog[x] for x in countries[i]]))
print('\n\n\n')





# Cluster by complete linkage
clusters = []
countries = []
for i in range(len(p)):
    clusters.append([np.array(p[i])])
    countries.append([i])
countrycount = len(countries)
combine_clusters(clusters,method='complete',k=7)
q6 = np.arange(countrycount)
for i in range(len(countries)):
    for j in range(len(countries[i])):
        q6[countries[i][j]] = i
print("Question 6")
print(",".join([str(x) for x in q6]))
for i in range(len(countries)):
    print("Group "+str(i+1))
    print(",".join([countrycatalog[x] for x in countries[i]]))
print('\n\n\n')

    



# K means clustering
k=7
ck = []
for i in range(len(p)): p[i] = np.array(p[i])
for i in range(k):
    randk = np.random.randint(len(p))
    ck.append(p[randk])


def get_centers(clusters):
    newck = []
    for cluster in clusters:
        newck.append(sum(cluster)/len(cluster))
    return newck

def kmean(ck,threshold):
    clusters = []
    countries = []
    for i in range(k):
        clusters.append([])
        countries.append([])
    for i in range(len(p)):
        mindist = edist(p[i],ck[0])
        center = 0
        for j in range(1,len(ck)):
            newdist = edist(p[i],ck[j])
            if newdist < mindist:
                mindist = newdist
                center = j
        clusters[center].append(p[i])
        countries[center].append(i)
    newck = get_centers(clusters)
    error_rate = sum(sum(abs(np.array(newck) - np.array(ck))))
    if error_rate < threshold:
        return [clusters, countries]
    else:
        ck = newck
        return kmean(ck,threshold)

# Execute clustering with arbitrarily small threshold
clusters, countries = kmean(ck,0.00000001)
print("Question 7")
q7 = np.arange(countrycount)
for i in range(len(countries)):
    for j in range(len(countries[i])):
        q7[countries[i][j]] = i
print(",".join([str(x) for x in q7]))
print('\n\n\n')

print("Question 8")
for c in ck:
    print(",".join([str(x) for x in c]))
print('\n\n\n')


# Calculate distortion from clustered data
distortion = 0
for i in range(len(ck)):
    for j in range(len(clusters[i])):
        distortion += edist(clusters[i][j],ck[i])**2
print("Question 9")
print(distortion)
