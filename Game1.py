import string
import random


#Art
def art1():
	print "                         /   ))     |\         )               ).           "
	print "                   c--. (\  ( `.    / )  (\   ( `.     ).     ( (           "
	print "                   | |   ))  ) )   ( (   `.`.  ) )    ( (      ) )          "
	print "                   | |  ( ( / _..----.._  ) | ( ( _..----.._  ( (           "
	print "     ,-.           | |---) V.'-------.. `-. )-/.-' ..------ `--) \._        "
	print "     | /===========| |  (   |      ) ( ``-.`\/'.-''           (   ) ``-._   "
	print "     | | / / / / / | |--------------------->  <-------------------------_>=-"
	print "     | \===========| |                 ..-'./\.`-..                _,,-'    "
	print "     `-'           | |-------._------''_.-'----`-._``------_.-----'         "
	print "                   | |         ``----''            ``----''                 "
	print "                   | |                                                      "
	print "                   c--` 													   "
	print "\n\n"
#End Art

#-------------------------------- Player --------------------------------#

#Race
def race():
	loop = True
	while loop:
		#NOTE: .lower() is fixed. Integrate it in if/else it was in the string library import string
		race_choice = raw_input("Are you an elf, human or dwarf? \n")
		#race_choice = "hUman"
		'''NOTE!!!'''
		#mod must be lower than
		#attack, because it's used
		#to calculate the attack
		#in a combat. This is the
		#upper limit. Look up HeroDmg()
		if race_choice.lower() == "elf":
			kind = "elf"
			mod = 1
			attack = 8
			loop = False
		elif race_choice.lower() == "human":
			kind = "human"
			mod = 2
			attack = 6
			loop = False
		elif race_choice.lower() == "dwarf":
			kind = "dwarf"
			mod = 3
			attack = 4
			loop = False
		else:
			print "Wrong input."
			loop = True
	#return stuff
	race.kind = kind
	race.mod = mod
	race.attack = attack
	return race.kind 										#Kind of race
	return race.mod 										#Race modifier
	return race.attack 									    #Character attack
#End race

#ID: Map, Mood
map = {
	0: ["Icemarsh", "cold"],
	1: ["Ironwood", "lost"],
	2: ["Applelake", "calm and happy"],
	3: ["Lakecastle", "the guards watching you"],
	4: ["Faycliff", "that something is wrong"]
	}
#End map and feel library

#Walking
def walk():
	#hours = raw_input("Hours? From 0 to 4: ")
	hours = "3"
	walking = random.randint(0,int(hours))
	print "You walk for " + hours + " hours. You are in " + map[walking][0] + " and you are feeling " + map[walking][1] + "."
	walk.zone = map[walking]
	walk.hours = int(hours)
	return walk.hours
	return walk.zone
#End walking

#Hero dmg
def HeroDmg():
	RandAttack = race.attack * (race.attack - race.mod)
	attack = random.randint(1, RandAttack)
	print "Hero attack:", attack

#End hero dmg

#Endurance = race + modifier
def endu():
	health = random.randint(1,6)
	endu.health = health * race.mod * 10
	atm_health = 0
	atm_health = endu.health
	return endu.health										#Character maximum health
	return atm_health
#End endurance

#------------------------------- Monsters -------------------------------#

#Monsters
def monster():
	monsters_dictionary = {
#		ID: ["name", attack, health, presence, modifier, A/An]
		0: ["noone", 0, 0, False, 0, "NaN"],
		1: ["spider", 2, 10, True, 1, "A"],
		2: ["big spider", 3, 15, True, 2, "A"],
		3: ["ghost", 4, 17, True, 3, "A"],
		4: ["goblin", 5, 19, True, 2, "A"],
		5: ["cockatrice", 7, 26, True, 10, "A"]
	}
	monster_count = len(monsters_dictionary)
	spawn = random.randint(0, monster_count - 1) # -1 to start count from 0
	monster.creature = monsters_dictionary[spawn][0]
	monster.attack = monsters_dictionary[spawn][1]
	monster.health = monsters_dictionary[spawn][2]
	monster.combat = monsters_dictionary[spawn][3]
	monster.mod = monsters_dictionary[spawn][4]
	monster.aoran = monsters_dictionary[spawn][5]
	return monster.creature
	return monster.attack
	return monster.health
	return monster.combat
	return monster.mod
	return monster.aoran
	print monster.aoran + " " + monster.creature
	print "Attack:", monster.attack
	print "Health:", monster.health
	print "Spawn:", monster.combat
#End monsters

#Combat check
def combat_check():
	if monster.combat == True:
		print "Combat true \n\n"
		combat()
	else:
		print "combat false \n\n"
		walk_nospawn()
#End combat check

#Character status at the moment
#atm_health = 0
#atm_health = endu.health 							#Character health at the moment. Maximum health is endu.health
#End character status at the moment

#Combat
def combat():
	print monster.aoran + " " + monster.creature + " appears before you."
	print "The " + monster.creature + " has " + str(monster.health) + " health and " + str(monster.attack) + " attack."
	print "You have " + str(endu.health) + " health and " + str(race.attack) + " attack."
	duel = raw_input("If you want to kill with " + monster.creature +" write \"kill\" if you want to try to run away from " + monster.creature + " write \"evade\".\n")
	#duel = "evade"
	#atm_health = endu.health
	if duel == "kill" or duel == "Kill" or duel == "KILL":
		print "\n-->Combat<--\n"
		atm_health = endu.health
		print atm_health
		while monster.health > 0 and atm_health > 0:
			print "-->Hit<--"
			monster.health = monster.health - race.attack
			atm_health = atm_health - monster.attack
			if monster.health <= 0:
				print "The monster died"
				print atm_health
				idle()
			elif atm_health <= 0:
				print "You died"
		else:
			print "combat() works fine"


	elif duel == "evade" or duel == "Evade" or duel == "EVADE":
		print "Evade --> -->"
		evade_limit = (20 - race.mod) + monster.mod * 10
		evade = random.randint(0, evade_limit)
		if evade >= (evade_limit * 0.67):
			print "You have evaded " + monster.creature + " successfully."
		else:
			print "You've angered " + monster.creature + " and it attacks you!"

	else: "Something went wrong in combat()"
#End combat

#No spawned monster
def walk_nospawn():
	quest_check()
#End no spawned monster

#Quest check
def quest_check():
	print "needs edit: maybe bigger numbers"
	chance_limit = walk.hours * 256
	chance = random.randint(0,chance_limit)
	if chance >= 500 and chance < 800:
		print "quest in quest_check()"
	elif chance >= 800 and chance < 1012:
		print "item in quest_check()"
	elif chance >= 1012:
		print "epic item in quest_check()"
	else:
		print "After hours of exploring you found nothing. What now?"
		idle()
		whereto = raw_input("If you want to go in another zone write \"walk\".\n If to want to continue exploring write \"explore\".\n Where to? ")
		print "\n\n"
		if whereto == "walk" or whereto == "Walk" or whereto == "WALK":
			walk()
			monster()
			combat_check()
		elif whereto == "explore" or whereto == "Explore" or whereto == "EXPLORE":
			monster()
			combat_check()
		else:
			print "something is wrong in quest_check()"
#End quest check

#when idle
def idle():
	whereto = raw_input("If you want to go in another zone write \"walk\".\n If to want to continue exploring write \"explore\".\n Where to? ")
	#print "\n\n"
	if whereto == "walk" or whereto == "Walk" or whereto == "WALK":
		walk()
		monster()
		combat_check()
	elif whereto == "explore" or whereto == "Explore" or whereto == "EXPLORE":
		monster()
		combat_check()
	else:
		print "something is wrong in quest_check()"
#end when idle

#---------------------------------- Items ---------------------------------#

#================= Weapons =================#

#================== Potions =================#

#================== Armor ==================#

#--------------------------------- Game ---------------------------------#

#Start of the game
print "+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+"
print "|		                                                             |"
print "|                                    Welcome                                 |"
print "|                            This is the tale of                             |"
print "|                             The flaming sword                              |"
print "|		                                                             |"
print "|		                                                             |"
print "+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ \n\n"

art1()

name = raw_input("What is your name? \n")
#name = "Nasko"
#End start

#Character
race()
endu()
HeroDmg()
print name + " is born a " + race.kind + " and has " + str(endu.health) + " endurance."
#End character

print name, "walks alone. \n"
walk()
print "\n"
monster()
print "\n"
combat_check()

print "\n\n"
print "+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+"
print "|		                                                             |"
print "|                                    The End                                 |"
print "|		                                                             |"
print "|		                                                             |"
print "+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+"
