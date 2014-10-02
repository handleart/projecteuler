#Project Euler, Problem 41
#Ardeshir Mostofi
#9/18/2014

import itertools

def rwh_primes1(n):
	# From Stack Overflow
    sieve = [True] * (n/2)
    #print n**0.5+1
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
        	sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


def ending(vv):
	v = str(vv)
	if (v[-1] == '3' or v[-1] == '7') and v[0] == '9':
		return True
	else:
		return False



i = range(1,10)
comb = itertools.permutations(i, 4)
#for i in comb:
#	print i

tmp = map(lambda (a, b, c, d, e, f, g, h, i): int(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i)), itertools.permutations(i))
#tmp = map(lambda (a, b): int(str(a) + str(b)),  comb)


perm = filter(lambda x: ending(x), tmp)

print len(perm), perm[-1]
#for j in perm:
#	print j


#reduce(lambda y: str(y), itertools.permutations(i)))


#p = rwh_primes1(int(max(perm)))
#p = rwh_primes1(int(max(perm)))
p = [3, 5]
A = []

#print perm
print p

print set(perm).intersection(p)