	#Project Euler, Problem 40
	#Ardeshir Mostofi
	#9/18/2014

#An irrational decimal fraction is created by concatenating the positive integers:

#0.123456789101112131415161718192021..

#It can be seen that the 12th digit of the fractional part is 1.

#If dn represents the nth digit of the fractional part, find the value of the following e*pression.

#d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000



def p40():
	d = ''
	for i in range(1000000):
		if len(d) > 1000000:
			break
		d = d + str(i)

	return d


if __name__ == '__main__':
	d = p40()
	print d[0:13]
	print 'result: ', int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000]) * int(d[100000]) * int(d[1000000])