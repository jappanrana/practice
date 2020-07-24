import datetime

def get_time():
	currentDT = datetime.datetime.now()
	hour = int(currentDT.hour)
	tmp = 0
	time_list = ["am","pm"]
	if hour > 12:
		hour = hour - 12
		tmp = 1
	print ("Current time is: %d%s %dmins" % (hour,time_list[tmp],currentDT.minute))
	del currentDT
	del hour
	del tmp
	del time_list
	return

def get_date():
	currentDT = datetime.datetime.now()
	month_list = ["","january","february","march","april","may","june","july","august","september","october","november","december"]
	month = month_list[currentDT.month]
	print ("Current date is: %d %s,%d" % (currentDT.day,month,currentDT.year))
	del currentDT
	del month_list
	del month
	return
#completed formatting