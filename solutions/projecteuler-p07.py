#Project Euler, Problem 7
#Find the xth Prime. I already had the code from a previous assignment.

def rwh_primes1(n):
	# From Stack Overflow
    sieve = [True] * (n/2)
    #print n**0.5+1
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
        	sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


p = rwh_primes1(150000)
#print len(p)

print (p[10000])