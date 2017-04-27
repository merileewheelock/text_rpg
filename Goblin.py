from Monster import Monster

class Goblin(Monster):
	def __init__(self):
		super(Goblin, self).__init__("Goblin")
		self.health = 6
		self.max_health = 6
		self.power = 2
		# self.name = "Goblin"
		self.xp_value = 5
		self.gold = 5

class Hobgoblin(Goblin):
	def __init__(self):
		super(Hobgoblin, self).__init__()
		self.name = "Hobgoblin"
		self.power = 3