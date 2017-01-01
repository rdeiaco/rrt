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
	x1 = x
	y1 = y

	## First, find out which octant is being used for this line.
	## Switch the inputs, depending on the octant.	
	
	## Calculate the slope, checking for a zero division.
	## Assign 10000 to be the slope when dx is zero.
	if (x1 == x0):
		if (y1 - y0) > 0:
			slope = 10000
		else:
			slope = -10000
	else:
		slope = (y1 - y0) / (x1 - x0)

	## Assign the octant based on the line.
	if (x0 < x1) and (slope >= 0) and (slope <= 1):
		octant = 0
	elif (y0 < y1) and (slope > 1):
		octant = 1
	elif (y0 < y1) and (slope < -1):
		octant = 2
	elif (x1 < x0) and (slope >= -1) and (slope <= 0):
		octant = 3
	elif (x1 < x0) and (slope > 0) and (slope <= 1):
		octant = 4
	elif (y1 < y0) and (slope > 1):
		octant = 5
	elif (y1 < y0) and (slope < -1):
		octant = 6
	else:
		octant = 7


	## Switch the inputs, depending on the octant.
	if (octant == 0):
		x0 = nearestNode.x
		y0 = nearestNode.y
		x1 = x
		y1 = y
	elif (octant == 1):
		x0 = nearestNode.y
		y0 = nearestNode.x
		x1 = y
		y1 = x
	elif (octant == 2):
		x0 = nearestNode.y
		y0 = -nearestNode.x
		x1 = y
		y1 = -x
	elif (octant == 3):
		x0 = -nearestNode.x
		y0 = nearestNode.y
		x1 = -x
		y1 = y
	elif (octant == 4):
		x0 = -nearestNode.x
		y0 = -nearestNode.y
		x1 = -x
		y1 = -y
	elif (octant == 5):
		x0 = -nearestNode.y
		y0 = -nearestNode.x
		x1 = -y
		y1 = -x
	elif (octant == 6):
		x0 = -nearestNode.y
		y0 = nearestNode.x
		x1 = -y
		y1 = x
	else:
		x0 = nearestNode.x
		y0 = -nearestNode.y
		x1 = x
		y1 = -y

	dx = x1 - x0
	dy = y1 - y0
	D = 2*dy - dx
	yi = y0

	## Check the path leading up to the point for a collision.
	for xi in range(x0, x1+1):

		## Switch the outputs, depending on the octant.
		if (octant == 0):
			xOut = xi
			yOut = yi
		elif (octant == 1):
			xOut = yi
			yOut = xi
		elif (octant == 2):
			xOut = -yi
			yOut = xi
		elif (octant == 3):
			xOut = -xi
			yOut = yi
		elif (octant == 4):
			xOut = -xi
			yOut = -yi
		elif (octant == 5):
			xOut = -yi
			yOut = -xi
		elif (octant == 6):
			xOut = yi
			yOut = -xi
		else:
			xOut = xi
			yOut = -yi


		## Check the point (xOut, yOut) for a block.
		if grid.positions[xOut][yOut].isBlocked():
			return False
		if (D > 0):
			yi = yi + 1
			D = D - dx
		D = D + dy

	## Make sure that the final grid space is checked.
	if grid.positions[x][y].isBlocked():
		return False

	return True

## Checks potential collision possibilities when a new node is added.
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

## Draws the final path on the grid.
def drawPath(path, grid):
	return grid
