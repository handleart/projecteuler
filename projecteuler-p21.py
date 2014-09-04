#Project Euler, Problem 21

#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.


def factors(num):
	factors = []
	tmp = []
	for p in xrange(2, int(num ** 0.5 + 1)):
		if num % p == 0:
			factors.append(p)
			factors.append(num / p)
	return [1] + factors


num = 10000

f = {}
g = {}
k = []

#for i in range(1, num+1):
for i in range(1, num):	
	f[i] = factors(i)
	g[i] = sum(f[i])

print f[220], f[284]
print g[220], g[284]

for key in g:
	if g[key] in g:	
		a = g[g[key]]
		b = g[key]

		keyB = key
		keyA = g[key]

		if (keyB != keyA):
			if a == keyB and b == keyA and (keyA not in k) and (keyB not in k) :
				k.append(keyA)
				k.append(keyB)

#print f[284], f[220]
#print g[284], g[220]
print f[6], f[28]
k.sort()
print k
print sum(k)

#print p

#ff = factors(f, p)

#calc sum of divisors of num not including num and assign to a dict


#find which one are amicable numbers