class Werewolf(object):
	def __init__(self):
		self.health = 10
		self.max_health = 10
		self.power = 8
		self.name = "Werewolf"
		self.xp_value = 10
		self.gold = 8

	def take_damage(self, damage):
		self.health -= damage

	def is_alive(self):
		return self.health > 0