#Project Euler, Problem 16
#Find the maximum total from top to bottom of the 'triangle' below:

from graph import Graph 
from functools import reduce
from priorityqueue import PriorityQueue

def vals_test():
	x = {}
	x[0] = [3]
	x[1] = [7, 4]
	x[2] = [2, 4, 6]
	x[3] = [8, 5, 9, 3]

	return x

def vals():
	x = {}

	x[0]=   [75]
	x[1]=	[95,64]
	x[2]=	[17,47,82]
	x[3]=	[18,35,87,10]
	x[4]=	[20,4,82,47,65]
	x[5]=	[19,1,23,75,3,34]
	x[6]=	[88,2,77,73,7,63,67]
	x[7]=	[99,65,4,28,6,16,70,92]
	x[8]=	[41,41,26,56,83,40,80,70,33]
	x[9]=	[41,48,72,33,47,32,37,16,94,29]
	x[10]=	[53,71,44,65,25,43,91,52,97,51,14]
	x[11]=	[70,11,33,28,77,73,17,78,39,68,17,57]
	x[12]=	[91,71,52,38,17,14,91,43,58,50,27,29,48]
	x[13]=	[63,66,4,68,89,53,67,30,73,16,69,87,40,31]
	x[14]=	[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

	return x

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

			#ver.setVal(dictNum[i][j])
	
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

x = vals()
g = defGraph(x, 0, 0)

vtest = g.getVertex('0,0')

#print g.getVertex('13,8').getVal()

print findMax(g, g.getVertex('0,0'))
