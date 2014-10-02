#Project Euler, Problem 23
#Find the maximum total from top to bottom of the 'triangle' below:
#the algorithm is not efficient. it is exponential

from graph import Graph 
from functools import reduce
from priorityqueue import PriorityQueue
import csv
import random

def vals_test():
	x = {}
	x[0] = [3]
	x[1] = [7, 4]
	x[2] = [2, 4, 6]
	x[3] = [8, 5, 9, 3]
	return x

def vals_test2():
	x = {}
	l = []
	for i in range(21):
		for j in range(i+1):
			l.append(random.randrange(1, 200))
		x[i] = l
		l = []
	return x

def loadFile():
	# sepVal = ''
	# y = {}
	# i = 0
	# with open('p067_triangle.txt', 'rU') as csvfile:
	# 	loadList = csv.reader(csvfile, delimiter=' ')

	# 	for row in loadList:
	# 		y[i] = row
	# 		i += 1
	# 		if i > 1:
	# 			break
	# print y[0]
	# return y
	data = [map(int, row.split()) for row in open("p067_triangle.txt")]
	
	

	return data


#create graph from dict with a starting index
def defGraph(dictNum, currentIndexY, currentIndexX):
	g = Graph()
	nextIndexY = currentIndexY + 1
	for i in dictNum:
		k = 0
		for j in range(len(dictNum[i])):
			currentVerName = str(i) + ',' + str(j)
			if currentVerName not in g:
				ver = g.addVertex(currentVerName)		
			g.getVertex(currentVerName).setVal(dictNum[i][j])
	
			if i+1 in dictNum:
				edge1 = str(i+1) + ',' + str(j)
				edge2 = str(i+1) + ',' + str(j+1)
				g.addEdge(currentVerName, edge1)
				g.addEdge(currentVerName, edge2)	
	return g

def findMax(g, v):
	#if no more vertices return 0
	if v.getConnections() == []: 
		if v.getMaxPath() == None:
			v.setMaxPath(v.getVal())
		return v.getMaxPath()
	#if vertices exist, the max distance for that node is the max of the distance of its kids

	# more complicated than is needed but I wanted to learn how to use a graph instead of a tree
	v.setMaxPath(v.getVal() + max(map(lambda x: findMax(g, x), v.getConnections())))
	#v.setMaxPath(v.getVal() + max(x, map(lambda x: x**2, [1, 2, 3])))

	return v.getMaxPath()



#x = loadFile()
x = vals_test2()
print x[5]
g = defGraph(x, 0, 0)
#print g.getVertex('0,0')


#vtest = g.getVertex('0,0')

#print g.getVertex('13,8').getVal()

print findMax(g, g.getVertex('0,0'))
