#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
#for example, the 5-digit number, 15234, is 1 through 5 pandigital.

#The product 7254 is unusual, as the identity, 39 x 186 = 7254, 
#containing multiplicand, multiplier, and product is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 
#pandigital.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

#abcdefghi are #s and are distinct
#abc * de = fghi < 9900 
#abc < 100, de < 98
#abcd * e = fghi < 9900
#abcd < 1237, e < 9

import itertools
import re

r = range(1,10)

abc = map(lambda x: str(x[0]) * 100 + str(x[1]) * 10 + str(x[2]), itertools.permutations(r, 3))
de = map(lambda x: str(x[0]) * 10 + str(x[1]), itertools.permutations(r, 2))
abcd = filter(lambda x: x < 1237, map(lambda x: str(x[0]) * 1000 + str(x[1]) * 100 + str(x[2]) * 10 + str(x[3]), itertools.permutations(r, 4)))

#abc = [102, 103]
#de = [32, 43, 21]

tmp = []
for i in abc:
	for j in de:
		word = str(i) + str(j) + str(int(i) * int(j))
		
		
		#tmp.append(word)

for i in range(1,9):
	for j in abcd:
		l = str(i) + str(j) + str(int(i) * int(j))
		tmp.append(l)


tmp = ['1234', '1224']

for word in tmp:
	for letter in word:
		if len(re.findall(letter, word)) > 1:
			break
		else:
			print word