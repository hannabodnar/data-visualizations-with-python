from random import randint

class Die():
	# A class representing a single die

	def __init__(self, num_sides=8):
		# Assume an eight-sided die.
		self.num_sides = num_sides

	def roll(self):
		# Returns a random value between 1 and 8.
		return randint(1, self.num_sides)