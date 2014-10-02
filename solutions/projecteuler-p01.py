#Project Euler, Problem 1
#Find the sum of natural numbers below topRange where those numbers are a multiple of mul1 or mul2
#Problem 1 from Project Euler

def sumMultipleRange(topRange, mul1, mul2):
	listNum = []
	for i in range(topRange):
		if (((i % mul1 == 0) or (i % mul2) == 0) and i >= (min(mul1, mul2))):
			listNum.append(i)
	
	return sum(listNum)


def testSumMultipleRange():
	topRange = 100
	mul1 = 3
	mul2 = 5

	tmp = sumMultipleRange(topRange, mul1, mul2)

	print tmp
	print tmp == 23

#testSumMultipleRange()

print sumMultipleRange(1000, 3, 5)