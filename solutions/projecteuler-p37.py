#Project Euler, Problem 37
#Ardeshir Mostofi
#9/17/2014

#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


def rwh_primes1(n):
	# From Stack Overflow
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
        	sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


upperLimit = 1000000

p = rwh_primes1(upperLimit)
pL = filter(lambda x: x < upperLimit / 10, p)

#print p
isTrue = False
A = []

for pp in p:
	pStr = str(pp)
	f = len(pStr)
	i = 1
	
	if not set(pStr).intersection(set([2, 4, 5, 6, 8, 0])):
		if pStr[-1] == '3' or pStr[-1] == '7':	
			while i < f:
				left = pStr[i:]
				right = pStr[:-i]

				#if (left[-1] == '2' and len(left) > 1) or left[-1] == '4' or left[-1] == '6' or left[-1] == '8' or left[-1] == '0' or (right[-1] == '2' and len(left) > 1) or right[-1] == '4' or right[-1] == '6' or right[-1] == '8' or right[-1] == '0':
				#if set(left).intersection(set([2, 4, 5, 6, 8, 0])):
				#	isTrue = False
				#	break
				if (int(left) not in pL) or (int(right) not in pL):
					isTrue = False
					break
				else:
					isTrue = True
				
				#print pStr[i:], pStr[:-i], isTrue
				i += 1
			
			if isTrue == True:
				A.append(pp)

if len(A) == 11:
	print A, 'sum: ', sum(A)
else:
	print 'no dice', A