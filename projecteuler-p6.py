#problem 6 from project euler
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#brute force
def sumSquareDifference(maxRng):
	sumOfSquares = 0
	squareOfSum = 0 
	for i in range(1, maxRng + 1):
		sumOfSquares = sumOfSquares + i ** 2
		squareOfSum = squareOfSum + i
	squareOfSum = squareOfSum ** 2

	#print sumOfSquares
	#print squareOfSum
	print squareOfSum - sumOfSquares 

#smarter way?
def sumSquareDifference2(maxRng):
	sumOfSquares = maxRng*(maxRng + 1)*(2*maxRng + 1) / 6

	squareOfSum = ((maxRng + 1) * maxRng / 2) ** 2
	
	print squareOfSum - sumOfSquares



sumSquareDifference(100)
sumSquareDifference2(100)
	