#Project Euler, Problem 12
#What is the value of the first triangle number to have over five hundred divisors?

#More efficient smarter choice. The whole process took 0.8 sec after 
def calcTriangleNum(num):
	return num * (num + 1) / 2

#First implementation (took 28 seconds to run the whole process)
def calcTriangleNumSlow(maxNum):
	x = []
	for i in xrange(1, maxNum+1):
		if len(x) > 0:
			tmp = lastVal + i
			x.append(tmp)
		else:
			x.append(i)
			tmp = i
		lastVal = tmp
	return x

#Find all the divisors
def rwh_primes1(n):
	# From Stack Overflow
	#
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
        	sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

#calculates all the prime number divisors 
def calcDivisors(num, primeList):
	factors = []
	for p in primeList:
		if p**2 > num: break
		i = 0
		while num % p == 0:
			num = num / p
			i += 1
		if i > 0:
			factors.append((p,i))
	if num > 1: factors.append((num,1))

	return factors

#Take an input of a range of numbers and the number of divisors we are looking for
def calcNumDivisorsList(listOfNum, numDiv):
	y = max(listOfNum)
	prime = rwh_primes1(y)

	tmp = [1]
	dictOfFactors = {}

	for num in listOfNum:
		triNum = calcTriangleNum(num)
		factors = calcDivisors(triNum, prime)

		for (a, exp) in factors:
			tmp = [i * a**e for i in tmp for e in xrange(exp+1)]

		#dictOfFactors[num] = tmp

		if len(tmp) > numDiv: return triNum

		tmp = [1]
	return False


def calcHighestTriNumDiv():
	x = xrange(1, 20000)
	
	factors = calcNumDivisorsList(x, 500)

	return factors



factors = calcHighestTriNumDiv()
print factors