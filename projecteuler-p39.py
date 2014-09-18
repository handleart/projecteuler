#Project Euler, Problem 39
#Ardeshir Mostofi
#9/18/2014

#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions
# for p = 120.

#{20,48,52}, {24,45,51}, {30,40,50}

#For which value of p <= 1000, is the number of solutions maximised?

#right triangle a ^ 2 + b ^ 2 = c ^ 2
#c is an integer

#p = a + b + c = a + b + (a^2 + b ^ 2) ** 0.5

import itertools

def p39():

	#499 is the max range since 499^2 + 1^2 = ~499^2 --> the param for this triangle would be a little larger than 1000
	x = xrange(1, 500)

	perm = itertools.combinations(x, 2)

	# keeps count of number of solutions for each perameter
	C = {}
	# keeps solution for each problem (mostly for troubleshooting purposes in this problem)
	D = {}

	#a^2 + b^2 = c^2
	c = lambda (a,b): (a ** 2 + b ** 2) ** 0.5 

	for i in perm:
		cc = c(i)
		if cc == int(cc) and (sum(i) + cc < 1000):
			cc = int(cc)
			tmp = sum(i) + cc
			if tmp not in D:
				D[tmp] = []
				C[tmp] = 0

			D[tmp].append(set(list(i) + [cc]))
			C[tmp] += 1

	p = 0
	comb = 0

	for key in C:
		if C[key] > p:
			p = C[key]
			comb = key

	#print p, comb, 'um'
	#print D, len(D)
	print p, comb

if __name__ == '__main__': 
	p39()