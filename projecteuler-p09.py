#Project Euler, Problem 9
#find the product of a Pythagorean triplet for which a + b + c = z

def pythagorean(numEq):
	z = 0
	val = []
	for a in range(numEq+1):
		for b in range(numEq+1): 
			c = (a**2 + b ** 2) ** 0.5

			if (a + b + c == numEq):
				print a, b, c
				val.append(a*b*c)

	return val

print(pythagorean(1000))