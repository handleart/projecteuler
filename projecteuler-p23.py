#Project Euler, Problem 23
#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
#For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a
# perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if 
#this sum exceeds n. As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
#the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
#it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
#However, this upper limit cannot be reduced any further by analysis even though it is known that the 
#greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import itertools

def factors(num):
	factors = []
	tmp = []
	for p in xrange(2, int(num ** 0.5) + 1):
		if num % p == 0 :
			if p not in factors: factors.append(p)
			if (num / p) not in factors: factors.append(num / p)
	return [1] + factors

#num = 30
num = 28123
d = {}
l = []

for i in xrange(1, num+1):	
	d[i] = factors(i)
	#print i, f[i]
	if sum(d[i]) > i:
		l.append(i)


sumSet = lambda (x,y) : x + y
sumSet2 = lambda x: x*2

allCombos = itertools.combinations(l, 2) 
#allCombos2 = itertools.permutations(l, 2)

#allSums = set(filter(lambda x: x <=num, (map(sumSet, allCombos) + map(sumSet2, l))))
allSums = set(map(sumSet, allCombos) + map(sumSet2, l))
#allSums2 = set(map(sumSet, allCombos2))
print allSums == allSums2

#print allSums

tmp = filter(lambda x: x not in allSums, xrange(1, num+1))
result = reduce(lambda x, y: x + y, tmp)
print result

#print sum(range(1, 31)) - 12 - 18





