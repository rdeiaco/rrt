import grid

class RRTree:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.nextNodes = []

	def addNode(self, x, y):
		self.nextNodes.append(RRTree(x, y))

	def addNodeCopy(self, node):
		self.nextNodes.append(node)

	def removeNode(self, position):
		if (position < len(self.nextNodes)):
			del self.nextNodes[position]



	

