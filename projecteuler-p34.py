#Project Euler, Problem 34
#Ardeshir Mostofi
#9/16/2014

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# def factorial(n):
# 	x = 1
# 	if n <= 1:
# 		return 1
# 	else:
# 		x *= n * factorial(n-1)

# 	return x

A = {}

A[0] = 1
A[1] = 1

result = []
for j in range(2,10):
	A[j] = A[j-1] * j


upperBound = 100000

for j in range(10, upperBound):
	tmp = 0
	for l in str(j):
	 	tmp += A[int(l)]
	if tmp == j:
	 	result.append(j)


print result, 'sum: ', sum(result)