#Project Euler, Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#finds the prime roots and the number of times their multiples appear in that set
def smallestMultipleRoots(rngMin, rngMax):
	prime = rwh_primes1(rngMax)
	x = {}
	for p in prime:
		x[p] = 0
		for i in range(rngMax, rngMin-1, -1):
			j = i
			tmp = 0
			while j >= p: 
				j = j / p
				tmp += 1
			if x[p] < tmp: x[p] = tmp
	return x

#calculates the smallest multiple based on a dict of primes and the number of times their multiples appear in that set
def calcSmallestMultiple(vals):
	smallestMultiple = 1
	for k in vals.keys():
		 smallestMultiple = smallestMultiple * (k ** vals[k])

	return smallestMultiple

def rwh_primes1(n):
	# From Stack Overflow
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


x = smallestMultipleRoots(1, 20)
smallestMultiple = calcSmallestMultiple(x)
print smallestMultiple