#Project Euler, Problem 28
#Ardeshir Mostofi
#9/8/2014

#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

f = 1
diag = 1001
dd = int((diag - 1) / 2 + 1)
#print dd

A = [1]

for i in range(dd):
	x = (1 + (2 * i)) ** 2 
	if i > 0:
		for j in range(4):
			A.append(x - 2 * j * i)

#print A
print sum(A)

