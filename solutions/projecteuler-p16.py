#Project Euler, Problem 14
#What is the sum of the digits of the number 2^1000?


x = 2**20
sumX = 0 

for i in str(x):
	sumX = sumX + int(i)

print sumX