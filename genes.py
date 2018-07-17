#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np
import random

class Genes:
	#initialize variables 
	def __init__ (self, GRAPH, ITERATION, NODES, CHILDS, MUT, start, stop, firstParent, secondParent):
		self.iteration = ITERATION
		self.numberOfNodes = NODES
		self.numberOfChilds = CHILDS
		self.mutateLvl = MUT
		self.GRAPH = GRAPH
		self.startCity = start
		self.stopCity = stop
		self.newChilds = [[-1]*self.numberOfNodes]*self.numberOfChilds
		self.bestRoute = []
		self.offSpring = [-1]*self.numberOfNodes
		self.cpyOffSpring = [-1]*self.numberOfNodes
		self.costOfParent1 = 0
		self.costOfParent2 = 0
		self.parent1 = firstParent
		self.parent2 = secondParent

	def makeRoute(self):
		print(np.matrix(self.GRAPH))
		self.setParents()

		for i in range(self.iteration):
			nChild = 0

			print( )
			print('Iteration number:  '+ str(i+1))
			self.printParents()
			self.printBestRoute()
			print( )

			for j in range(self.numberOfChilds):
				self.offSpring[0] = self.startCity
				self.cpyOffSpring[0] = self.startCity

				for k in range(1, self.numberOfNodes):
					self.offSpring[k] = -1
					self.cpyOffSpring[k] = -1

				for k in range(1, self.numberOfNodes):
					choose = random.randint(0, 1)
					mutate = random.randint(1, 100)

					if choose==0 or k>len(self.parent2):
						if k<len(self.parent1):
							self.offSpring[k] = self.parent1[k]
					elif choose==1 or k>len(self.parent1): 
						if k<len(self.parent2):
							self.offSpring[k] = self.parent2[k]

					if mutate<self.mutateLvl: 
						self.offSpring[k] = random.randint(0, self.numberOfNodes-1)

					if self.offSpring[k] == self.stopCity: 
						break

				ii = 1
				needCpy = False
				for k in range(1, self.numberOfNodes):
					if self.offSpring[k-1] == self.offSpring[k]: 
						needCpy = True
					else: 
						self.cpyOffSpring[ii] = self.offSpring[k]
						ii += 1
				if needCpy==True: 
					for k in range(1, self.numberOfNodes): self.offSpring[k] = self.cpyOffSpring[k];


				properOffspring = True
				for k in range(1, self.numberOfNodes):
					if self.offSpring[k-1] != -1 and self.offSpring[k] != -1:
						if self.GRAPH[self.offSpring[k-1]][self.offSpring[k]] <= 0:
							properOffspring = False


				for k in range(self.numberOfNodes):
					for k2 in range(self.numberOfNodes):
						if self.offSpring[k] == self.offSpring[k2] and k!=k2 and self.offSpring[k] != -1:
							properOffspring = False
							break


				isStopCity = False
				for k in range(1, self.numberOfNodes):
					if self.offSpring[k] == self.stopCity:
						isStopCity = True
						break
				if isStopCity == False: properOffspring = False

				for k in range(self.numberOfNodes):
					if self.offSpring[k]==self.stopCity: break
					if self.offSpring[k]==-1:
						properOffspring = False
						break

				if properOffspring == True:
					for k in range(self.numberOfNodes):
						self.newChilds[nChild][k] = self.offSpring[k]
					nChild += 1

			#self.printChilds(nChild)

			for j in range(nChild):
				if(self.newChilds[j][0]==self.startCity):
					cost = 0
					diff = 0
					for k in range(1, self.numberOfNodes):
						if self.newChilds[j][k]==-1: break
						cost += self.GRAPH[self.newChilds[j][k-1]][self.newChilds[j][k]]

					diff = self.costOfParent1 - self.costOfParent2

					if diff >= 0 and cost<=self.costOfParent1:
						self.parent1 = []
						for c in range(self.numberOfNodes):
							self.parent1.append(self.newChilds[j][c])
							self.costOfParent1 = cost

					if diff<0 and cost<=self.costOfParent2:
						self.parent2 = []
						for c in range(self.numberOfNodes):
							self.parent2.append(self.newChilds[j][c])
							self.costOfParent2 = cost

					if cost<=self.costOfBestRoute:
						self.bestRoute = []
					for c in range(self.numberOfNodes):
						if cost<=self.costOfBestRoute:
							self.bestRoute.append(self.newChilds[j][c])
							self.costOfBestRoute = cost


			print('Iteration finished!')
			for p in range(40): print('-', end=" ", flush=True)
			print()
		self.printBestRoute()

			

	def setParents(self):
		for i in range(len(self.parent1)):
			self.costOfParent1 += self.GRAPH[self.parent1[i-1]][self.parent1[i]] 
		
		for i in range(len(self.parent2)):
			self.costOfParent2 += self.GRAPH[self.parent2[i-1]][self.parent2[i]]

		if self.costOfParent1 > self.costOfParent2:
			self.costOfBestRoute = self.costOfParent2
			for i in range(len(self.parent2)):
				self.bestRoute.append(self.parent2[i])
		else:
			self.costOfBestRoute = self.costOfParent1
			for i in range(len(self.parent1)):
				self.bestRoute.append(self.parent1[i])


	def printParents(self):
		#Method to print info about parents
		print('First parent: ', end="", flush=True)
		for i in range(len(self.parent1)):
			if self.parent1[i]!=-1: print(self.parent1[i], end=" ", flush=True)
		print('		Cost: ' + str(self.costOfParent1))

		print('Second parent: ', end="", flush=True)
		for i in range(len(self.parent2)):
			if self.parent2[i]!=-1: print(self.parent2[i], end=" ", flush=True)
		print('		Cost: ' + str(self.costOfParent2))


	def printBestRoute(self):
		print('Currently best route: ', end="", flush=True) 
		for i in range(len(self.bestRoute)):
			if self.bestRoute[i]!=-1: print(self.bestRoute[i], end=" ", flush=True)
		print('	Cost: ' + str(self.costOfBestRoute))


	def printChilds(self, childsNum):
		print('Correct childs made in this iteration: ')
		for i in range(childsNum):
			for j in range(self.numberOfNodes):
				print(self.newChilds[i][j], end=" ", flush=True)
				if self.newChilds[i][j] == self.stopCity: break
			print( )