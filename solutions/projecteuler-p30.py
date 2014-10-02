#Project Euler, Problem 30
#Ardeshir Mostofi
#9/10/2014
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

degree = 5
A = []

for i in range(2,1000000):
	tmp = 0
	for j in str(i):
		tmp = tmp + int(j) ** degree

	if tmp == i:
		A.append(i)



print A, sum(A)

