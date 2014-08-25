#Project Euler, Problem 2
#Find the sum of even values of fib sequenece up to 4M

def fib(maxNum):
	fibSeq = []
	fibSeq = [1, 2]
	while True:
		if sum([fibSeq[-1] + fibSeq[-2]]) > maxNum: break
		fibSeq = fibSeq + [fibSeq[-1] + fibSeq[-2]] 		
	return fibSeq

def removeOdds(fibSeq):
	tmp = []
	for val in fibSeq:
		if (val % 2 == 0):
			tmp.append(val)
		#else:
		#	print val
	return tmp
	
topRange = 4000000

fibSeq = fib(topRange)

EvenFibSeq= removeOdds(fibSeq)
print EvenFibSeq
print sum(EvenFibSeq)
