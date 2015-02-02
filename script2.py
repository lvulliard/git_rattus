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
eigvect[:,0]

# See linalg.eig