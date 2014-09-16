#Project Euler, Problem 31
#Ardeshir Mostofi
#9/10/2014

#How many different ways can 200p be made using any number of coins?
#types of coins: 1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p).

coins = [200, 100, 50, 20, 10, 5, 2, 1]
val = 200

#coins = [100, 50, 25, 10, 5, 1]
#val = 100

def bruteForce(val):
	x = lambda a, b, c, d, e, f, g, h: a * 1 + b * 2 + c * 5 + d * 10 + e * 20  + f * 50 + g * 100 + h * 200
	i = 0

	for a in range(1, 201):
		for b in range (1, 101):
			for c in range(1, 41):
				for d in range(1, 21):
					for e in range(1, 101):
						for f in range (1, 5):
							for g in range(1, 3):
								for h in range(1, 2):
									if x(a,b,c,d,e,f,g,h) == 200:
										i += 1

	return i

if __name__ == '__main__':
	print bruteForce(val)
