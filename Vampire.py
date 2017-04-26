class Vampire(object):
	def __init__(self):
		self.health = 12
		self.max_health = 12
		self.power = 5
		self.name = "Vampire"
		self.xp_value = 10
		self.gold = 10

	def take_damage(self, damage):
		self.health -= damage

	def is_alive(self):
		return self.health > 0