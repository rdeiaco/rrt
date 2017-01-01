import grid
import planner
import tree

LENGTH = 16
X_START = 0
Y_START = 0
MAX_STEP = 4




rrt = tree.RRTree(X_START, Y_START)
rrt.addNode(1, 0)
rrt.addNode(0, 1)
temp = rrt.nextNodes[1]
temp.addNode(1, 1)
temp = temp.nextNodes[0]
temp.addNode(1, 2)
temp.addNode(2, 1)
temp = temp.nextNodes[0]
temp.addNode(1, 3)

temp = rrt.nextNodes[0]
temp.addNode(2, 0)
temp = temp.nextNodes[0]
temp.addNode(3, 0)
temp = temp.nextNodes[0]
temp.addNode(3, 1)
temp.addNode(4, 0)

randNode = tree.RRTree(7, 3)

## Test findNearestNode method
testNode = tree.RRTree(0, 0)
assert planner.findNearestNode(rrt, testNode) == []
testNode = tree.RRTree(7, 3)
assert planner.findNearestNode(rrt, testNode) == [0, 0, 0, 1]
testNode = tree.RRTree(0, 2)
assert planner.findNearestNode(rrt, testNode) == [1]


## Test inTree method.
assert planner.inTree(rrt, 3, 1) == True
assert planner.inTree(rrt, 6, 6) == False 
assert planner.inTree(rrt, 0, 0) == True

## Test gridSafe method.
nearestNode = tree.RRTree(4, 6)
gridMap = grid.Grid(LENGTH)
x = 6 
y = 9
assert planner.gridSafe(nearestNode, x, y, gridMap) == True

for i in range(LENGTH):
	gridMap.positions[5][i].block()
assert planner.gridSafe(nearestNode, x, y, gridMap) == False 

x = 5
y = 4
assert planner.gridSafe(nearestNode, x, y, gridMap) == False

x = 4
y = 10
assert planner.gridSafe(nearestNode, x, y, gridMap) == True


print("Tests Passed.")
