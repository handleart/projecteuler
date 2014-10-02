#Project Euler, Problem 28
#Ardeshir Mostofi
#9/9/2014

#Considering quadratics of the form:
#n^2 + an + b, where |a| < 1000 and |b| < 1000
#where |n| is the modulus/absolute value of n
#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
#primes for consecutive values of n, starting with n = 0.


import threading

class myThread(threading.Thread):
	def __init__(self, p, a, b, counter):
		threading.Thread.__init__(self)
		self.p = p
		self.a = a
		self.b = b
		self.c = counter
	def run(self):
		l, ab = maxP(self.p, self.a, self.b, self.c)		
		print l, ab

def rwh_primes1(n):
	# From Stack Overflow
    sieve = [True] * (n/2)
    #print n**0.5+1
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
        	sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]



def quad(a, b, p):
	n = [1, 1, 1, 1]

	m = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
	v = [0, 1, 2, 3]	

	tmp = []
	brk = False


	while True:
		for i in v:
			l = n[i] ** 2 + a * n[i] * m[i][0] + b * m[i][1]
			if l not in p: 
				if len(v) == 1:
					brk = True
					a_ret = a * m[i][0]
					b_ret = b * m[i][1]
					n_ret = n[i]
				else:
					v.remove(i)
			else:
				n[i] = n[i] + 1
		
		if brk == True:
			break
		#print n, '-', l, l in p


	return n_ret, a_ret, b_ret


def maxP(p, aa,bb, c=0):
	maxQuadLen = 0
	maxQuadab = ()

	q = {}

	p = p + [1]

	i = 0

	for b in bb:
		for a in aa:
			q[str(a) + ',' + str(b)] = quad(a, b, p)
			#print a, b, q[str(a) + ',' + str(b)]
			if q[str(a) + ',' + str(b)] > maxQuadLen:
				maxQuadLen = q[str(a) + ',' + str(b)]
				maxQuadab = (a, b)

			i += 1
			if i % 10000 == 0 : print 'thread' + str(c) + ' - ' + str(i)

	return maxQuadLen, maxQuadab
  
def ab(a, b):
	yield n ** 2 + a * n + b * n 
			
p = rwh_primes1(10000)
p2 = rwh_primes1(1000)

a, b = p2, p2

#print p[:252]
#print p.index(1601)

# n,b,c = quad(1, 41, p)
# print '41-', n, b, c

# q = quad(-79, 1601, p)
# print '1601-', q

print ' -- '

#l, ab = maxP(p)
#print l, ab


#l, i = maxP(p, a, b)
#print l, i
#print 'result: ' + str(l[1] * l[2])

#q = quad(i[0], i[1], p)
#print i, '-', q

thread1 = myThread(p, a, b, 1)
# thread2 = myThread(p, a, b, 2)
thread1.run()
# thread2.run()
