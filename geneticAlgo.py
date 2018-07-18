#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import csv
import numpy as np

import randPaths
import genes

#Set here: number of iteration, childs(in one iteration), and possibility of mutation in percent:
ITERATION = 10
CHILDS = 100
MUT = 10

GRAPH = [[]]
NODES=0
with open('smallTopology.csv', "rt") as f:
    reader = csv.reader(f)
    for line in reader:
    	for x in range(len(line)):
    		GRAPH[NODES].append(int(line[x]))
    	if(NODES>0):
    		GRAPH[NODES].remove(NODES)
    	NODES += 1
    	GRAPH.append([NODES])
GRAPH.pop()


startCity = input('Please choose first Node(from 0 to ' + str(NODES-1) + '): ')
stopCity = input('Please choose last Node(from 0 to ' + str(NODES-1) + '): ')

startCity = int(startCity)
stopCity = int(stopCity)

paths = randPaths.randPaths(GRAPH, NODES, startCity, stopCity)
firstParent = paths.makeRoute()
secondParent = paths.makeRoute()

gen = genes.Genes(GRAPH, ITERATION, NODES, CHILDS, MUT, startCity, stopCity, firstParent, secondParent)
gen.makeRoute()

firstPath = gen.returnBestRoute()
print()
print('Best route: ' + str(firstPath))