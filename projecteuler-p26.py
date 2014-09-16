#Project Euler, Problem 26
#Ardeshir Mostofi
#9/8/2014

#first attempt
def div(num, den, i = 0, r = []):
	if i < 120:
		#print str(num) + '/' + str(den)
		ret = []
		if num % den == 0:
			return [[num / den]]
		else:
			tmp = num / den
			#print tmp
			if r == tmp and r != 0:
				return [[]]
			else:
				ret.extend([tmp] + r for r in div(num % den * 10, den, i + 1, tmp))
		return ret
	else:
		return [[]]


#second better attempt
ff = {}

tmpKey = None
tmpLen = 0

for i in xrange(1, 1000):
	x, f, fRem, j = 1 , [], [], 1

	while True:
		j+=1
		lastX = x
		
		while x < i: x = x * 10

		f.append(x / i)
		x = x % i
		if x == 0 or x in fRem:
			break
		fRem.append(x % i)
	
	#ff[i] = f
	if len(f) > tmpLen:
		tmpKey, tmpLen = i, len(f)


# for e in ff:
# 	if len(ff[e]) > tmpLen:
# 		tmpKey = e
# 		tmpLen = len(ff[e])

print 'key: ', tmpKey
