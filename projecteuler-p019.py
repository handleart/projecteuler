#Project Euler, Problem 19
#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def isLeapYear(x):
	if((x % 4) == 0 and (x % 100 != 0 or x % 400 ==0)):
		return True
	else:
		return False


def findDayMonthComb(day):

	daysInMonth = {}

	daysInMonth['feb'] = [28, 29]
	daysInMonth['jan'], daysInMonth['mar'], daysInMonth['may'], daysInMonth['jul'], daysInMonth['aug'], daysInMonth['oct'], daysInMonth['dec'] = [31], [31], [31], [31], [31], [31], [31]
	daysInMonth['apr'], daysInMonth['jun'], daysInMonth['nov'], daysInMonth['sept'] = [30], [30], [30], [30]

	daysInAWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']

	#isLeapYear = lambda x: 'Yes' if((x % 4) == 0 and (x % 100 != 0 or x % 400 ==0)) else 'No'

	yearMin = 1901
	initMonth = 'jan'
	initYear = 1900
	initDate = 1
	initDay = 'Monday'
	initDayNum = 0

	#year = xrange(1900,2001)
	year = range(1900,2001)

	dd = {}
	for i in daysInAWeek:
		dd[i] = []

	j = 0

	for y in year:
		for m in xrange(12):
			if isLeapYear(y):
				#month is feb ?
				if m == 1: 
					l = 1
				else:
					l = 0
			else:
				l = 0
			

			days = daysInMonth[months[m]][l]

			for d in xrange(days):
				mm = str(y) + ',' + months[m]

				#if d == 0, its the first day of the month
				if daysInAWeek[initDayNum % 7] == day and y >= yearMin and d == 0:
					print mm
					j += 1

				initDayNum += 1
					

	return j




# print detDay(2000)
# print detDay(2100)
# print detDay(2200)
# print detDay(2300)

x = findDayMonthComb('Sunday')
print x

