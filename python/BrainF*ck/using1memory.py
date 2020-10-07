# ord(value) is inbuilt function for getting ASCII value of char
x = input("Enter your string to be printed:")
x = list(x)
currentvalue = 0
# empty list for storing ascii value
asciilst = []
# getting ascii value of every char
for item in x:
	asciilst.append(ord(item))
# declaring empty list for storing BF code chars
final = ""
# code to get BF code that changes 1 memory location value to required value and prints it
for item in asciilst:
	while currentvalue != item:
		if currentvalue > item:
			final += "-"
			currentvalue -= 1
		else:
			final += "+"
			currentvalue += 1
	final += "."
# write final string on file to copy
f_obj = open("answer.txt","w")
f_obj.write(final)
f_obj.close()
# print str
print(final)
input("bye!")