#Project Euler, Problem 36
#Ardeshir Mostofi
#9/18/2014

gNums = {}
import time

def base10to2base(n):
	j = ''
	i = 0

	if n == 0:
		return '0'

	while n > 0:
		if n % 2 == 0:
			j = '0' + j
		elif n % 2 == 1:
			j = '1' + j
		n = n / 2


	return j

def calcBase2nums(maxNum):
	F = {}
	F[0] = '0'
	F[1] = '1'
	for i in range(2, maxNum):
		j = len(F[i-1]) - 1
		jF = j
		while True:
			#print F, 'j:', j, 'v:', F[i-1][j]
			#time.sleep(1)
			if F[i-1][j] == '0':
				F[i] = F[i-1][:j] + '1' + (jF - j) * '0'
				break
			elif j <= 1:
				F[i] = '1' + (jF + 1) * '0'
				break
			else:
				j -= 1
		#print F[i]

	return F

if __name__ == '__main__':
	m = 1000000
	#create a list of both base 10 and base 2 numbers
	F = calcBase2nums(m)
	j = 0
	A = []

	for i in F:
		#j += i if (str(i) == str(i)[::-1]) and (str(F[i]) == str(F[i][::-1])) else 0
		if (str(i) == str(i)[::-1]) and (str(F[i]) == str(F[i][::-1])):
			A.append(i)	
			j += i

	print j

	#for v in A:
	#	print v, F[v]

	#for i in range(m):
	#	base10to2base(i)

	#print base10to2base(1000)