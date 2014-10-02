#Project Euler, Problem 3
#Find Largest Prime Factor for a number
#Example: The prime factors of 13195 are 5, 7, 13, 29

import math

def rwh_primes1(n):
	# From Stack Overflow
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


def findPrimeFactor(num):
	#Find all prime factors for a number
	primes = rwh_primes1(int(num ** 0.5))
	primeFactors = []

	for i in primes:
		if (num % i == 0):
			primeFactors.append(i)

	return primeFactors

def findLargestPrimeFactor(num):
	#find the max prime factor
	return max(findPrimeFactor(num))


def tester():
	#This was a solution by someone else on project euler
	d, n = 3, 600851475143
	while (d * d < n):
		#keep dividing back factors until you get to the largest remaining prime factor
		if n % d == 0: n /= d
		else: d +=2
	print n

print (findPrimeFactor(600851475143))
tester()