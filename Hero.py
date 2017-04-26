class Hero(object):
	def __init__(self, name = "Incognito"):
		self.name = name
		self.health = 20
		self.power = 5
		self.max_health = self.health
		self.xp = 0		#experience points
		self.level = 1
		self.gold = 0

	def check_level(self):
		if self.xp > 3:
			self.level = 2
			self.level_up()

	def level_up(self):
		self.max_health += 10
		self.health = self.max_health
		self.power += 5
		print "Thou hast leveled up, %s! Thy health is now %d and thy power is now %d." % (self.name, self.max_health, self.power)


	def pickup_gold(self):
		print "You have %d gold!" % self.gold

	def cheer_hero(self):
		print "Fight hard, %s!" % self.name

		#This class method returns a boolean. True if hero alive, False if hero dead.
	def is_alive(self):
		#return self.health > 0 (Another way to write the code below)
		if(self.health > 0):
			return True
		else:
			return False

	def attack(self, who_to_attack):
		who_to_attack.health -= self.power	#who_to_attack is effectively the_goblin

	def increase_health(self, amount):
		self.health += amount
		if self.health > self.max_health:
			self.health = self.max_health
