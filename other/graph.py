#based on code / lessons from interactive python algoritms with my tweaks

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self, key):
		self.numVertices += 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self, n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			None

	def __contains__(self, n):
		return n in self.vertList

	def addEdge(self, f, t, cost = 0):
		if f not in self.vertList:
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv = self.addVertex(t)

		self.vertList[f].addNeighbor(self.vertList[t], cost)

	def getVertices(self):
		return iter(self.vertList.values())

	def __iter__(self):
		return iter(self.vertList.values())


class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}
		self.val = 0
		self.maxpath = None

	def addNeighbor(self, nbr, weight = 0):
		self.connectedTo[nbr] = weight

	def __str__(self):
		return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

	def getWeight(self, nbr):
		return self.connectedTo[nbr]

	def setVal(self, val):
		self.val = val

	def getVal(self):
		return self.val

	def setMaxPath(self, dist):
		self.maxpath = dist

	def getMaxPath(self):
		return self.maxpath


	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id
