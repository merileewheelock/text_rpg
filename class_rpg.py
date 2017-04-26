# Import the Hero class from Hero.py
from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
from Werewolf import Werewolf
from Win import Win
from random import randint

the_hero = Hero()
# the_hero.cheer_hero()

print "What is thy name, brave adventurer?"
the_hero.name = raw_input("> ")

print "How many monsters are you willing to fight?"
num_of_enemies = int(raw_input("> "))

monsters_objects = []
monsters_objects.append(Goblin())
monsters_objects.append(Vampire())
monsters_objects.append(Werewolf())

monsters = []
for i in range(0, num_of_enemies):
	rand = randint(0, len(monsters_objects) - 1)
	monsters.append(monsters_objects[rand])

for monster in monsters:
	monster.health = monster.max_health
	# Run game as long as BOTH characters have health
	while monster.is_alive() and the_hero.is_alive():
		print "Brave %s, you have encountered a %s." % (the_hero.name, monster.name)
		print "\nYou have %d health and %d power." % (the_hero.health, the_hero.power)
		print "The %s has %d health and %d power.\n" % (monster.name, monster.health, monster.power)
		print "What do you want to do?"
		print "1. Fight %s" % monster.name
		print "2. Do nothing"
		print "3. Flee"
		print "4. Drink potion of life"
		print "5. Go to store"
		print "> ",
		user_input = raw_input()
		if user_input == "1":
			#Hero is going to attack
			# monster.health -= the_hero.power	Commented out for below
			the_hero.attack(monster)
			# monster.take_damage(the_hero.power)	#This would belong in the goblin class if used
			print "You have done %d damage to the %s." % (the_hero.power, monster.name)
			if monster.health <= 0:
				print "Great job, %s! You have defeated the %s!" % (the_hero.name, monster.name)
				the_hero.xp += monster.xp_value
				the_hero.gold += monster.gold
				the_hero.pickup_gold()
				the_hero.check_level()
				Win()
		elif user_input == "2":
			#Hero is going to do nothing
			pass
		elif user_input == "3":
			print "Goodbye, coward."
			the_hero.health = 0
			break
		elif user_input == "4":
			the_hero.increase_health(20)
		elif user_input == "5":
			print "What would you like to purchase from the store?"
			print "1. Weapons"
			print "2. Healing potion"
			store_purchase = raw_input("> ")
			if store_purchase == "1":
				the_hero.power += 4
				print "Your power has increased to %d!\n" % the_hero.power
			elif store_purchase == "2":
				the_hero.health += 4
				print "Your health has increased to %d!\n" % the_hero.health
			elif store_purchase != "1" or store_purchase != "2":
				print "Not available at store."
		else:
			print "Invalid input %s" % user_input

		if monster.health > 0:
			#Hero has attacked (or not) and goblin is still alive
			the_hero.health -= monster.power
			print "The %s hits you for %d damage." % (monster.name, monster.power)
			if the_hero.health <= 0:
				print "You have been killed by the %s." % monster.name

		if the_hero.health > 0 and the_hero.health < 5:
			print "You have gone into a rage. Your power has increased!"
			the_hero.power += 5