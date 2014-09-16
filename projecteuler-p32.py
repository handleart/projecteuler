#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
#for example, the 5-digit number, 15234, is 1 through 5 pandigital.

#The product 7254 is unusual, as the identity, 39 x 186 = 7254, 
#containing multiplicand, multiplier, and product is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 
#pandigital.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

#bah --- this assumption was wrong

#abcdefghi are #s and are distinct
#abc * de = fghi < 9900 
#abc < 100, de < 98
#abcd * e = fghi < 9900
#abcd < 1237, r < 9

import itertools

def findSol():

	r = range(1,10)

	abc = map(lambda x: int(x[0]) * 100 + int(x[1]) * 10 + int(x[2]), itertools.permutations(r, 3))
	de = map(lambda x: int(x[0]) * 10 + int(x[1]), itertools.permutations(r, 2))
	#abcd = filter(lambda x: x < 10000, map(lambda x: int(x[0]) * 1000 + int(x[1]) * 100 + int(x[2]) * 10 + int(x[3]), itertools.permutations(r, 4)))
	abcd = map(lambda x: int(x[0]) * 1000 + int(x[1]) * 100 + int(x[2]) * 10 + int(x[3]), itertools.permutations(r, 4))
	
	#test data
	#abc = [102, 103, 186]
	# de = [32, 43, 21, 39]
	
	tmp = []
	for i in abc:
		for j in de:
			word = str(i) + str(j) + str(i * j)
			if len(set(word)) == 9 and len(word) == 9 and ('0' not in word):
				#tmp.append((i,j,i*j))
				tmp.append(i*j)

	for i in abcd:
		for j in r:
			word = str(i) + str(j) + str(i * j)
			if len(set(word)) == 9 and len(word) == 9 and ('0' not in word):
				#tmp.append((i,j,i*j))
				tmp.append(i*j)

	#print len(tmp)
	#for i in tmp:
	#	print i
	return sum(set(tmp))


if __name__ == '__main__':
	print findSol()

