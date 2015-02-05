#!/usr/bin/python2.6
# -*-coding:Latin-1 -*
from numpy import *
from pylab import *

# List of unique proteins
b = loadtxt('prot_list', dtype= int)

# Eig centrality
ce = loadtxt('ce_matrix', dtype= float)

# Deg centrality
cd = loadtxt('cd_matrix', dtype= float)

# Linear regression
(x,y) = polyfit(ce,cd,1)
print("cd = %f * ce + %f"%(x,y))

# Polyval evaluates the line equation at each point
yp = polyval([x,y],ce)

# Plot
plot(ce,yp)
scatter(ce, cd)
show()

# Delete biggest value
ce = delete(ce, ce.argmax(), 0)
cd = delete(cd, cd.argmax(), 0)

# Linear regression
(x,y) = polyfit(ce,cd,1)
print("cd = %f * ce + %f"%(x,y))

# Polyval evaluates the line equation at each point
yp = polyval([x,y],ce)

# Plot
plot(ce,yp)
scatter(ce, cd)
show()