#!/usr/bin/python2.6
# -*-coding:Latin-1 -*
from numpy import *

f = open('rattus.txt', 'r')
a = loadtxt(f, skiprows = 1, usecols = (0,1,2), dtype = int)

# List of unique proteins
b = concatenate((a[:,1],a[:,2]),axis=0)
b = unique(b)
b.sort() 

# Number of proteins
n = len(b)

# Number of interactions
m = len(a)

# Adjacence matrix
c = zeros((n, n), dtype = int)

# Boucle de P. Grobatar
for i in range(0, n):
	for j in range(0, m):
		if(b[i] == a[j,1]):
			c[(b.tolist()).index(a[j,2]),i] +=1
			c[i,(b.tolist()).index(a[j,2])] +=1
		if(b[i] == a[j,2]):
			c[(b.tolist()).index(a[j,1]),i] +=1
			c[i,(b.tolist()).index(a[j,1])] +=1