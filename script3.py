#!/usr/bin/python2.6
# -*-coding:Latin-1 -*
from numpy import *

# List of unique proteins
b = loadtxt('prot_list', dtype= int)

# Eig centrality
ce = loadtxt('ce_matrix', dtype= float)

# Deg centrality
cd = loadtxt('cd_matrix', dtype= float)

# Dictionaries mapping centralities to corresponding proteins
cd_dic = dict(zip(cd,b))
ce_dic = dict(zip(ce,b))

ranked_cd = sorted(cd_dic.items(), reverse = True)
ranked_ce = sorted(ce_dic.items(), reverse = True)

for i in range(40) :
	for j in range(40) :
		if ranked_ce[i][1] == ranked_cd[j][1] :
			print "La proteine %d est au rang %d dans le classement par centralite de degre, et au rang %d dans le classement par centralite de valeurs propres."%(ranked_cd[j][1], j+1, i+1)

savetxt('ce_ranking', ranked_ce, delimiter=' ', fmt='%.5f')		
savetxt('cd_ranking', ranked_cd, delimiter=' ', fmt='%.5f')		