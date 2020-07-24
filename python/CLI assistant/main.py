import greet
from custom_datetime import get_date as date
from custom_datetime import get_time as time
import calculator
import game
#main

greet.greeting()

print("\nwhat you want to do:\n1)check date.\n2)check time.\n3)to open calculator.\n4)to play stone,paper,scissor.\n5)to play number guess game.")
c_1 = int(input("\nenter our choice:"))

if c_1 == 1:
	date()
elif c_1 == 2:
	time()
elif c_1 == 3:
	calculator.calc()
elif c_1 == 4:
	game.spc()
elif c_1 == 5:
	game.nog()
else:
	print("bye bye")
del c_1
input("\npress enter to exit")
#add unit converter
#min and max in calculator is still left