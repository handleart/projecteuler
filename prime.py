import csv

def rwh_primes1(n):
	# From Stack Overflow
    sieve = [True] * (n/2)
    #print n**0.5+1
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
        	sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def writePrimes():

	x = rwh_primes1(100000)
	xx = []	

	myfile = open('prime.txt', 'wb')
	wr = csv.writer(myfile)
	wr.writerow(x)

def readPrimes():
	result = []
	with open('prime.txt', 'rb') as f:
		reader = csv.reader(f)
		for row in reader: 
			result.append(row)

	return result

writePrimes()
f = readPrimes()
#print f[:50]

print f[:50]
print 4 in f
