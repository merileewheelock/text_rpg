from Monster import Monster

class Werewolf(Monster):
	def __init__(self):
		super(Werewolf, self).__init__("Werewolf")
		self.health = 10
		self.max_health = 10
		self.power = 8
		# self.name = "Werewolf"
		self.xp_value = 10
		self.gold = 8