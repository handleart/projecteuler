#Project Euler, Problem 25

#The Fibonacci sequence is defined by the recurrence relation:

#Fn = Fn - 1 + Fn - 2, where F1 = 1 and F2 = 1

#What is the first term in the Fibonacci sequence to contain 1000 digits?


Fib = []

Fib.append(0)
Fib.append(1)
Fib.append(1)

i = 2

while (len(str(Fib[i])) < 1000):
	i += 1
	Fib.append(Fib[i-1] + Fib[i-2])

print Fib[3]
print Fib[i], Fib[i-1]
print '--'
print i
print len(str(Fib[i]))


