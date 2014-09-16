#Project Euler, Problem 31 --- Attempt 3
#Ardeshir Mostofi
#9/10/2014


coins = [1, 2, 5, 10, 20, 50, 100, 200]

def func(n, k):
	global coins
	if k < 0 or n < 0:
		return 0
	elif n == 0: 
		return 1
	else:
		return func(n, k-1) + func(n - coins[k], k)


print func (200,len(coins) - 1)
