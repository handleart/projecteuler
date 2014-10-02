#Project Euler, Problem 40
#Ardeshir Mostofi
#9/18/2014
#
#Take the number 192 and multiply it by each of 1, 2, and 3:
#
#192 x 1 = 192
#192 x 2 = 384
#192 x 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated 
#product of 192 and (1,2,3)
#
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 
#918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of 
#an integer with (1,2, ... , n) where n > 1?

#we need the first digit to be 9. so its has to be  
#s

def p38():
	L = []
	D = {}
	n = '123456789'

	for i in range(9000,10000):
		s = ''
		for j in range(1, 10):
			sTmp = str(i * j)
			if len(sTmp + s) > 9:
				break

			s += sTmp

			if len(s) == 9:
				if len(set(s).intersection(n)) == 9:
					L.append(s)
					D[str(i) + ',' + str(j)] = s
				break

	#print len(L)
	return max(L), D

if __name__ == '__main__':
	lMax, D = p38()

	print lMax
	print D


