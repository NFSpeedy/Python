import random
import time

#The Game
def game():
	computer = random.randint(1,3)
	X = {
		0: 0,
		1: "rock",
		2: "paper",
		3: "scissors"
	}
	Y = X[computer]
	#choise = raw_input("Rock, paper, scissors?: ")
	choise = "rock"
	print "\n"
	if choise == "rock":
		if Y == "rock":
			print "Computer: ", Y 
			print "it's a tie\n"
		elif Y == "paper":
			print "Computer: ", Y 
			print "You lose\n"
		elif Y == "scissors":
			print "Computer: ", Y 
			print "You Win\n"
		else:
			print"Something went wrong :("
	elif choise  == "paper":
		if Y == "rock":
			print "Computer: ", Y 
			print "You win\n"
		elif Y == "paper":
			print "Computer: ", Y
			print "it's a tie\n"
		elif Y == "scissors":
			print "Computer: ", Y
			print "You lose\n"
		else:
			print"Something went wrong :("
	elif choise  == "scissors":
		if Y == "rock":
			print "Computer: ", Y 
			print "You lose\n"			
		elif Y == "paper":
			print "Computer: ", Y
			print "You win\n"			
		elif Y == "scissors":
			print "Computer: ", Y
			print "it's a tie\n"
		else:
			print"Something went wrong :("
	else:
		print"Something went wrong :( !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	exit()

#The Exit
def exit():
	#exit = raw_input("Do you want to play again? Y/N: ")
	exit = "Y"
	if exit == "Y":
		game()
	elif exit == "N":
		quit()
	else:
		print"Something went wrong :("

game()
exit()
