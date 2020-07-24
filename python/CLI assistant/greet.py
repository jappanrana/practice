import datetime
import getpass
import stranger

def greeting():
	currentDT = datetime.datetime.now()
	hour = int(currentDT.hour)
	minute = int(currentDT.minute)

	if hour >= 6 and hour < 12:
		greeting = "good morning"
	elif hour == 12 and minute == 0:
		greeting = "noon"
	elif hour <= 17:
		greeting = "good afternoon"
	elif hour <= 20:
		greeting = "good evening"
	else:
		greeting = "good night"

	del currentDT
	del hour
	del minute

	family = ["sanjay","shilpa","dhruvi"]
	friend = ["kunj","preet","darshan","ayush"]
	name = str(input("please enter your name:"))
	if name == "jappan":
		pswd = int(getpass.getpass("enter password:"))
		if pswd == 9876:
			print("hey! %s sir" % greeting)
			del pswd
		else:
			input("wrong password liar get lost")
			exit()
	elif name in family:
		if name == family[0]:
			print("hello papa %s" % greeting)
		elif name == family[1]:
			print("hello mummy %s" % greeting)
		else:
			print("hello didi %s" % greeting)
	elif name in friend:
		print("hey buddy %s" % greeting)
	else:
		print("hey! stranger %s.\nhope you will enjoy the code." % greeting)
		stranger.stranger()

	del family
	del friend
	del name
	del greeting
	return
#completed formatting