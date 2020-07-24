import OTP

def stranger():
	print("hope you have generated otp from generate_otp file\nit's in the same folder if not go!!")
	rsl = OTP.check()
	if rsl == True:
		del rsl
		print("access granted")
	else:
		del rsl
		input("access denied press enter to exit")
		exit()
	return
#completed formatting