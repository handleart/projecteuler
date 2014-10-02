#Project Euler, Problem 34
#Ardeshir Mostofi
#9/16/2014

#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
#are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

import itertools

def rwh_primes1(n):
	# From Stack Overflow
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
        	sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def circularComb(n):
	circ = []
	iStr = str(n)

	for k in range(len(iStr)):
		iStr = iStr[1:] + iStr[0]
		#if iStr[-1] not in '2468':
		circ.append(int(iStr))
	return circ

def findSol():
	p = rwh_primes1(1000000)
	test = True
	A = []
	for i in p:
		if '2' in str(i) or '4' in str(i) or '6' in str(i) or '8' in str(i):
			pass
		else:

			#find circular combinations
			circ = circularComb(i)
			
			for j in circ:
				#print jj
				#j = int(jj)
				if j in p:
					test = True
				else:
					test = False
					break

			if test == True:
				A.append(i)

	return len(A) + len([2])

if __name__ == '__main__':
	print findSol()
	#j = circularComb(197)

	

