#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random
import copy

class randPaths:

	def __init__(self, GRAPH, NODES, startCity, stopCity):
		self.GRAPH = GRAPH
		self.numberOfNodes = NODES
		self.startCity = startCity
		self.stopCity = stopCity
		self.route = []
		self.availableNodes = []


	def makeRoute(self):
		newGRAPH = copy.deepcopy(self.GRAPH)

		self.route = []
		self.route.append(self.startCity)

		i = 0
		while self.route[-1]!=self.stopCity:
			self.availableNodes = []
			available = 0
			for j in range(self.numberOfNodes):
				if newGRAPH[self.route[-1]][j] > 0:
					self.availableNodes.append(j)
					available += 1

			for k in range(self.numberOfNodes):
				newGRAPH[k][self.route[-1]] = 0
				newGRAPH[self.route[-1]][k] = 0
			
			if available==0:
				i = 0
				self.route = []
				self.route.append(self.startCity)
				newGRAPH = copy.deepcopy(self.GRAPH)

			else:
				self.route.append(self.availableNodes[random.randint(0, available-1)])
				i += 1

		return self.route