#!/usr/bin/env python

import copy
import csv
import numpy as np

import genes

NODES = 12
CHILDS = 20
MUT = 20
ITERATION = 10

GRAPH = [[]]
n=0
with open('smallTopology.csv', "rt") as f:
    reader = csv.reader(f)
    for line in reader:
    	for x in range(len(line)):
    		GRAPH[n].append(int(line[x]))
    	if(n>0):
    		GRAPH[n].remove(n)
    	n = n + 1
    	GRAPH.append([n])
GRAPH.pop()

startCity = 3;
stopCity = 8;

print(np.matrix(GRAPH))
gen = genes.Genes(GRAPH, ITERATION, NODES, CHILDS, MUT, startCity, stopCity)
gen.makeRoute()