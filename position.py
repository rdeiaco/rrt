class Position:
	def __init__(self, isBlocked):
		self.blocked = isBlocked

	def block(self):
		self.blocked = True

	def unblock(self):
		self.blocked = False

	def isBlocked(self):
		return self.blocked
