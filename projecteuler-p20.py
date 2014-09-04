#Project Euler, Problem 20

from functools import reduce

#method 1

x = 100
factorial = 1
sumDigits = 0

for i in xrange(1, x+1):
	factorial = factorial * i

for i in str(factorial):
	sumDigits = sumDigits + int(i)

print factorial
print sumDigits

# one liner

print(reduce(lambda x,y: x + y, (int(i) for i in str(reduce(lambda x, y: x*y, range(1,100))))))