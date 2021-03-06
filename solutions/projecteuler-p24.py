#Project Euler, Problem 24

#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 
#1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, 
#we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools

# def perm(x):
# 	if len(x) <=1:
# 		yield x
# 	else:
# 		for i in perm(x[1:]):
# 			for j in range(len(x)):
# 				yield i[:j] + x[0:1] + i[j:] 



n = 10
x = [str(i) for i in xrange(n)]
y = itertools.permutations(x, n)
tmp = perm(x)
tmp2 = map(lambda x: x,tmp)
tmp2.sort()
print tmp2[1000000-1]

z = map(lambda x: x, y)

z.sort()

iStr = ''
for i in z[1000000-1]:
	iStr = iStr + i

print int(iStr)

