import sys

import position

class Grid:
	def __init__(self, length):
		self.positions = []
		for i in range(length):
			self.positions.append([])
			for j in range(length):
				self.positions[i].append(position.Position(False))

	def printGrid(self, length):
		for i in range(length):
			
			if (i == 0):
				for j in range(length+2):
					sys.stdout.write("=")

			sys.stdout.write("\n|")

			for j in range(length):
				if (self.positions[i][j].blocked):
					sys.stdout.write("|")
				else:
					sys.stdout.write("_")
			
			sys.stdout.write("|\n")

			if (i == (length-1)):
				for j in range(length+2):
					sys.stdout.write("=")

				sys.stdout.write("\n")
	
					
