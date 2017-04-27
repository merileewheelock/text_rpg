class Monster(object):
	def __init__(self, name):
		self.name = name
		self.health = 10		#Default values if the sub-class monster doesn't have value
		self.max_health = 10	#Default values if the sub-class monster doesn't have value
		self.power = 10			#Default values if the sub-class monster doesn't have value

	def take_damage(self, damage):
		self.health -= damage

	def is_alive(self):
		return self.health > 0