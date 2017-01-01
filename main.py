import grid
import planner
import tree

LENGTH = 16
X_START = 0
Y_START = 0
MAX_STEP = 4


destination = tree.RRTree(9, 6)
gridMap = grid.Grid(LENGTH)
#gridMap.printGrid(LENGTH)

rrt = tree.RRTree(X_START, Y_START)
#rrt.addNode(1, 0)
#rrt.addNode(0, 1)
#temp = rrt.nextNodes[1]
#temp.addNode(1, 1)
#temp = temp.nextNodes[0]
#temp.addNode(1, 2)
#temp.addNode(2, 1)
#temp = temp.nextNodes[0]
#temp.addNode(1, 3)
#
#temp = rrt.nextNodes[0]
#temp.addNode(2, 0)
#temp = temp.nextNodes[0]
#temp.addNode(3, 0)
#temp = temp.nextNodes[0]
#temp.addNode(3, 1)
#temp.addNode(4, 0)
#
#randNode = tree.RRTree(7, 3)
#
#print(planner.inTree(rrt, 3, 1))
#print(planner.inTree(rrt, 6, 6))
#print(planner.inTree(rrt, 0, 0))

while True:
	## Generate a new random node.
	randNode = getRandNode(LENGTH)
	## Bias the node towards the destination.
	if (random.random() < 0.1):
		randNode = destination

	## Find the location in the tree that the random node is closest to.
	addLocation = planner.findNearestNode(rrt, randNode)
	## Check for collisions with obstacles, then add to the tree
	nearestNode = rrt
	for i in range(len(addLocation)):
		nearestNode = nearestNode.nextNodes[addLocation[i]]


	nodeToAdd = planner.collisionCheck(nearestNode, randNode, gridMap, MAX_STEP)
	if nodeToAdd:
		nearestNode.addNodeCopy(nodeToAdd)
		if (nodeToAdd.x == destination.x) and (nodeToAdd.y = destination.y):
			break	

finalPath = planner.findnearestNode(rrt, nodeToAdd)
finalGrid = planner.drawPath(finalPath, gridMap)
gridMap.printGrid(LENGTH)



