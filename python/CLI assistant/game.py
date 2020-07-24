import random

def spc():
	spc_list = ["stone","paper","scissor"]
	while True:
		print("press\n1) for stone.\n2) for paper.\n3) for scissor.")
		y = int(input("play:"))
		x = random.randint(0,2)
		y -= 1
		print("your choice:- %s computers choice:- %s" % (spc_list[y],spc_list[x]))
		if x == y:
			print("tie")
		elif x == y+1 or (x == 0 and y == 2):
			print("I won")
		else:
			print("you won")
		print("\n")
		chc = input("play again? press y/n:")
		if chc == "n":
			break
	del spc_list
	del x
	del y
	del chc
	return

def nog():
	ans = random.randint(1,25)
	chance = 5
	print("Welcome to guess the number.\nThe no is between 1-25")
	while True:
		print("You have %d chances left" % chance)
		tmp = int(input("Enter your number:"))
		chance -= 1
		if tmp >= ans+5:
			print("too much")

		if tmp == ans:
			print("You Won")
			break
		
		if tmp <= ans-5:
			print("too less")
		
		if chance == 0:
			print("You Lose")
			print("no was %d" % ans)
			break
		del tmp
	return