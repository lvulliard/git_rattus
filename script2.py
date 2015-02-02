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
c = loadtxt('matrixa')

cd = [0.0] * n
# Protein with the biggest cd
# First value is the maximum, and the second is the index
maxcd = [0,-1]
for i in range(0, n):
	cd[i] += sum(c[:,i])
	cd[i] /= n-1
	if(cd[i] > maxcd[0]):
		maxcd[1] = i
		maxcd[0] = cd[i]

print("La protéine avec le plus grand degré est la protéine : ")
print(b[maxcd[1]])

# See linalg.eig