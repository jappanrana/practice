import datetime
import crpt

def generate():

	currentDT = datetime.datetime.now()
	
	if currentDT.day < 10:
		day = "0"+str(currentDT.day)
	else:
		day = str(currentDT.day)
	if currentDT.hour < 10:
		hour = "0"+str(currentDT.hour)
	else:
		hour = str(currentDT.hour)
	minute = int(currentDT.minute)
	
	minute += 5
	if minute < 10:
		minute = "0"+str(minute)
	else:
		minute = str(minute)
	
	ootp = day+hour+minute
	
	otp = crpt.encrypt(ootp)
	
	print("your OTP is: %s" % otp)
	del currentDT
	del day
	del hour
	del minute
	del ootp
	del otp
	return

def check():

	otp = input("please enter your otp number:")
	
	dotp = crpt.decrypt(otp)
	
	currentDT = datetime.datetime.now()
	
	if currentDT.day < 10:
		day = "0"+str(currentDT.day)
	else:
		day = str(currentDT.day)
	if currentDT.hour < 10:
		hour = "0"+str(currentDT.hour)
	else:
		hour = str(currentDT.hour)
	if currentDT.minute < 10:
		minute = "0"+str(currentDT.minute)
	else:
		minute = str(currentDT.minute)
	
	cotp = day+hour+minute
	
	cotp = int(cotp)

	if cotp == dotp or cotp == dotp-1 or cotp == dotp-2 or cotp == dotp-3 or cotp == dotp-4 or cotp == dotp-5:
		del cotp
		del dotp
		del otp
		del currentDT
		del day
		del hour
		del minute
		return True
	else:
		print("unauthorized access!!")
		del cotp
		del dotp
		del otp
		del currentDT
		del day
		del hour
		del minute
		return False
	

#completed formatting