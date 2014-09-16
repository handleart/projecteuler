#Project Euler, Problem 31
#Ardeshir Mostofi
#9/10/2014

#How many different ways can 200p be made using any number of coins?
#types of coins: 1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p).

#200 = a * 1p + b * 2p + c * 5p + d * 10p + e * 20p  + f * 50p + g * 100p + h * 200p

coins = [200, 100, 50, 20, 10, 5, 2, 1]
val = 200

#coins = [100, 50, 25, 10, 5, 1]
#val = 100

def findCombo(val, m):
	global coins
	x = 0
	if m == 7: return 1
	for i in range(m, len(coins)):
		if val - coins[i] == 0: x +=1
		elif val - coins[i] > 0: x += findCombo(val - coins[i], i)
	return x


if __name__ == '__main__':
	print findCombo(val, 0)
