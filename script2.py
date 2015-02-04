#!/usr/bin/python2.6
# -*-coding:Latin-1 -*
from numpy import *

f = open('rattus.txt', 'r')
a = loadtxt(f, skiprows = 1, usecols = (0,1,2), dtype = int)

# List of unique proteins
b = loadtxt('prot_list', dtype= int)

# Number of proteins
n = len(b)

# Number of interactions
m = len(a)

# Adjacence matrix
c = loadtxt('adj_matrix')

eigval, eigvect = linalg.eig(c)
#First value is the biggest

ce = [0.0] * n
# Protein with the biggest cd
# First value is the maximum, and the second is the index
maxce = [0,-1]
for i in range(0, n):
	ce[i] += eigvect[i,0]
	if(ce[i] > maxce[0]):
		maxce[1] = i
		maxce[0] = ce[i]

print("La protéine avec la plus grande centralité par valeur propre est la protéine : ")
print(b[maxce[1]])

savetxt('ce_matrix', eigvect[:,0], delimiter=' ', fmt='%.5f')

# See linalg.eig