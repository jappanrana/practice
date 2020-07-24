import math

def add():
	rslt = 0
	data_list = []
	chc = str(input("have you counted the no of data you want to work on? enter yes/no:"))
	
	if chc == "yes":
		count = int(input("enter no of data you want to work on:"))
		
		i = 0
		while i < count:
			data_list.append(int(input("enter data:")))
			i += 1
		
		i = 0
		while i < count:
			rslt = rslt + data_list[i]
			i += 1
		
		print("provided data is:")
		print(data_list)
		print("total is %d" % rslt)
		
		del i

	elif chc == "no":
		print("OK so you will be asked whether you have more data or not\nafter every 3 entries please answer y for yes and n for no")
		print("NOTE :- enter 0 for extra enteries")
		
		i = 0
		while True:
			data_list.append(int(input("enter data:")))
			i += 1
			
			if i%3 == 0:
				chc_1 = input("do you have more entries? y/n:")
				
				if chc_1 == "n":
					break
		
		j = 0
		while j < i:
			rslt = rslt + data_list[j]
			j += 1
		
		print("provided data is:")
		print(data_list)
		print("total is %d" % rslt)
		
		del i
		del j
		del chc_1
	
	else:
		print("wrong input!")
	
	del rslt
	del data_list
	del chc
	return

def sub():
	print("please provide the POSITIVE and NEGATIVE values SEPERATELY and WITHOUT SIGN")
	prslt = 0
	nrslt = 0
	rslt = 0
	pdata_list = []
	ndata_list = []
	chc = str(input("have you counted the NUMBER of POSITIVE data you want to work on? enter yes/no:"))
	
	if chc == "yes":
		count = int(input("enter no of data you want to work on:"))
		
		i = 0
		while i < count:
			pdata_list.append(int(input("enter data:")))
			i += 1
		
		i = 0
		while i < count:
			prslt = prslt + pdata_list[i]
			i += 1
		
		del i
	elif chc == "no":
		print("OK so you will be asked whether you have more data or not\nafter every 3 entries please answer y for yes and n for no")
		print("NOTE :- enter 0 for extra enteries")
		
		i = 0
		while True:
			pdata_list.append(int(input("enter data:")))
			i += 1
			
			if i%3 == 0:
				chc_1 = input("do you have more entries? y/n:")
				
				if chc_1 == "n":
					break
		
		j = 0
		while j < i:
			prslt = prslt + pdata_list[j]
			j += 1
		
		del i
		del j
		del chc_1
	else:
		print("wrong input!")

	chc = str(input("have you counted the NUMBER of NEGATIVE data you want to work on? enter yes/no:"))

	if chc == "yes":
		count = int(input("enter no of data you want to work on:"))
		
		i = 0
		while i < count:
			ndata_list.append(int(input("enter data:")))
			i += 1

		i = 0
		while i < count:
			nrslt = nrslt + ndata_list[i]
			i += 1

		print("provided data is:-")
		print("positive:-")
		print(pdata_list)
		print("negative:-")
		print(ndata_list)
		
		rslt = prslt - nrslt
		print("answer is : %d" % rslt)
		
		del i

	elif chc == "no":
		print("OK so you will be asked whether you have more data or not\nafter every 3 entries please answer y for yes and n for no")
		print("NOTE :- enter 0 for extra enteries")

		i = 0
		while True:
			ndata_list.append(int(input("enter data:")))
			i += 1

			if i%3 == 0:
				chc_1 = input("do you have more entries? y/n:")

				if chc_1 == "n":
					break

		j = 0
		while j < i:
			nrslt = nrslt + ndata_list[j]
			j += 1

		print("provided data is:-")
		print("positive:-")
		print(pdata_list)
		print("negative:-")
		print(ndata_list)

		rslt = prslt - nrslt
		print("answer is : %d" % rslt)

		del i
		del j
		del chc_1
	else:
		print("wrong input!")

	del rslt
	del prslt
	del nrslt
	del pdata_list
	del ndata_list
	del chc
	return

def mult():
	rslt = 1
	data_list = []
	chc = str(input("have you counted the no of data you want to work on? enter yes/no:"))
	
	if chc == "yes":
		count = int(input("enter no of data you want to work on:"))
		
		i = 0
		while i < count:
			data_list.append(int(input("enter data:")))
			i += 1
		
		i = 0
		while i < count:
			rslt = rslt * data_list[i]
			i += 1
		
		print("provided data is:")
		print(data_list)
		print("total is %d" % rslt)
		
		del i
	
	elif chc == "no":
		print("OK so you will be asked whether you have more data or not\nafter every 3 entries please answer y for yes and n for no")
		print("NOTE :- enter 1 for extra enteries")
		
		i = 0
		while True:
			data_list.append(int(input("enter data:")))
			i += 1
			
			if i%3 == 0:
				chc_1 = input("do you have more entries? y/n:")
				
				if chc_1 == "n":
					break
		
		j = 0
		while j < i:
			rslt = rslt * data_list[j]
			j += 1
		
		print("provided data is:")
		print(data_list)
		print("total is %d" % rslt)
		
		del i
		del j
		del chc_1
	
	else:
		print("wrong input!")
	
	del rslt
	del data_list
	del chc
	return

def divi():
	print("division of only two numbers is calculated")
	
	x = int(input("enter no to be divided:"))
	y = int(input("enter divisor:"))
	q = int(x/y)
	r = x%y
	
	print("quotient is %d and remainder is %d" % (q,r))
	return

def maxm():
	print("uder construction")
	return

def minim():
	print("uder construction")
	return

def calc():
	print("make your choice.\n1 for addition.\n2 for subtraction.\n3 for multiplication.\n4 for division.\n5 for getting maximum no from provided numbers.\n6 for getting minimum no from provided numbers.")
	choice = int(input("enter your choice:"))
	
	if choice == 1:
		add()
	elif choice == 2:
		sub()
	elif choice == 3:
		mult()
	elif choice == 4:
		divi()
	elif choice == 5:
		maxm()
	elif choice == 6:
		minim()
	else:
		print("calculator is closed")
	del choice
	return

#completed formatting