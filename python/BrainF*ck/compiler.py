memoryblocks = [0]
runtimepos = 0
memorypos = 0
openedloops = []
BFPrg = input("enter your string:")
BFPrg = list(BFPrg)
while runtimepos < len(BFPrg):
	if memorypos < 0:
		print("Illegal use of < as memory ran beyond first bit,\nTry again with better code.")
		exit = input("Programe will exit")
		exit()
	elif BFPrg[runtimepos] == "+":
		if memoryblocks[memorypos] < 127:
			memoryblocks[memorypos] += 1
		else:
			print("since memory increased more then 127 its reset to 0")
			memoryblocks[memorypos] = 0
	elif BFPrg[runtimepos] == "-":
		if memoryblocks[memorypos] > 0:
			memoryblocks[memorypos] -= 1
		else:
			print("since memory decreased less then 0 its reset to 127")
			memoryblocks[memorypos] = 127
	elif BFPrg[runtimepos] == ">":
		memoryblocks.append(0)
		memorypos += 1
	elif BFPrg[runtimepos] == "<":
		memorypos -= 1
	elif BFPrg[runtimepos] == ".":
		print(chr(memoryblocks[memorypos]) , end = "")
	elif BFPrg[runtimepos] == ",":
		tmp = input("\nInput Requested")
		tmp = list(tmp)
		memoryblocks[memorypos] = ord(tmp[0])
	elif BFPrg[runtimepos] == "[":
		openedloops.append(runtimepos)
	elif BFPrg[runtimepos] == "]":
		if memoryblocks[memorypos] == 0:
			garbeg = openedloops.pop()
		else:
			runtimepos = openedloops[len(openedloops)-1]
	else:
		print("\n\nIllegal charcter at %d" %(runtimepos+1))
	runtimepos += 1

print("")
bye = input("Brainf*ck Compiler made by Jappan Rana.\nFor any problem contact us.")
# ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.(hello world!)