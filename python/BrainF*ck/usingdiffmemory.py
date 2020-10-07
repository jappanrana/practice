# ord(value) is inbuilt function for getting ASCII value of char
x = input("Enter your string to be printed:")
x = list(x)
# empty list for storing ascii value
asciilst = []
# getting ascii value of every char
for item in x:
	asciilst.append(ord(item))
# declaring empty list for storing BF code chars
final = ""
# code to get BF command for storing every ascii value in different memory
for item in asciilst:
	i=0
	while i < item:
		final += "+"
		i +=1
	# to print and move
	if i == item:
		final += ".>"
# write final string on file to copy
f_obj = open("answer.txt","w")
f_obj.write(final)
f_obj.close()
# print str
print(final)
input("bye!")