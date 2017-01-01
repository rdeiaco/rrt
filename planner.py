import tree

import random
import math

global distance
global path

## Returns the nearest node in the tree to a given new node.
def findNearestNode(tree, newNode):
	global distance
	global path
	distance = 100000
	path = []

	nearestNode(tree, newNode, list(path))
	return path

## Recursive helper function for finding the nearest node.
def nearestNode(tree, newNode, nodePath):
	global distance
	global path
	
	
	tempDistance = ((newNode.x - tree.x)**2 + (newNode.y - tree.y)**2)**0.5

	
	if tempDistance < distance:
		distance = tempDistance
		path = list(nodePath)

	if (tree.nextNodes):
		for i in range(len(tree.nextNodes)):
			tempPath = list(nodePath)
			tempPath.append(i)
			nearestNode(tree.nextNodes[i], newNode, tempPath)


## Generates a new random node to add. 
def getRandNode(length):
	x = random.randrange(length)
	y = random.randrange(length)
	return tree.RRTree(x, y)

## Checks to see if a node location is already within the tree.
def inTree(tree, x, y):
	if (tree.x == x) and (tree.y == y):
		return True
	
	contained = False
	for i in range(len(tree.nextNodes)):
		contained = contained or inTree(tree.nextNodes[i], x, y)
	
	return contained


## Checks to see if there is a safe linear path on the grid from the 
## nearest node to the new point.
def gridSafe(nearestNode, x, y, grid):
	## Check all point along the line from the nearest node
	## to the point that we are adding to see if there are any
	## grid collisions.
	## Use Bresenham's line algorithm.
	x0 = nearestNode.x
	y0 = nearestNode.y
	dx = x - x0
	dy = y - y0
	D = 2*dy - dx
	yi = y0

	## Check the path leading up to the point for a collision.
	for xi in range(x0, x+1):
		## Check the point (xi, yi) for a block.
		print([xi, yi])
		if grid.positions[xi][yi].isBlocked():
			return False
		if (D > 0):
			yi = yi + 1
			D = D - dx
		D = D + dy

	## Make sure that the line goes all the way to the final y-value.
	while (yi <= y):
		print([xi, yi])
		if grid.positions[xi][yi].isBlocked():
			return False
		yi = yi + 1

	return True


def collisionCheck(rootNode, nearestNode, randNode, grid, maxStep):
	## First, calculate where the new node will be placed based on
	## the maximum step size.
	deltaX = randNode.x - nearestNode.x
	deltaY = randNode.y - nearestNode.y
	deltaMag = (deltaX**2 + deltaY**2)**0.5
	## Normalize the step if it exceeds the maximum step size.
	if deltaMag > maxStep:
		angle = math.atan2(deltaY, deltaX)
		newX = math.floor(maxStep*math.cos(angle) + nearestNode.x)
		newY = math.floor(maxStep*math.sin(angle) + nearestNode.y)
	else:
		newX = randNode.x
		newY = randNode.y
	

	## Check to see point is on the grid.
	if (newX >= LENGTH) or (newY >= LENGTH):
		return False

	## Next, see if the new node location is already in the tree.
	if not inTree(rootNode, newX, newY):
		return False


	## Finally, see if there are any collisions along the grid.
	if not gridSafe(nearestNode, newX, newY, grid):
		return False

	## If all checks pass, return the new node to add.
		return tree.RRTree(newX, newY)
