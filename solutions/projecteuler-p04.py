#Project Euler, Problem 4
#find the largest palindrom that is a product of two 3-digit numbers

#dumb way

#find all palindrome's between min and max

#then find the numbers that multiply them

a = range(1,10)
b = range(0,10)
c = range(0,10)

pal = []

for i in a:
	for j in b:
		for k in c:
			pal = pal + [int(str(i) + str(j) + str(k) + str(k) + str(j) + str(i))]

#now find two numbers that are multiple of these palindroms ...
a = range(999, 901, -2)
b = range(901, 999, 2)

multTable = []
calc = 'inf'
i = 0


for i in a:
	for j in b:
		calc = i * j
		if calc in pal: 
			multTable.append(calc)
			
print max(multTable)


#different way using palindrome's quality
# pal m*n = abccda
#         = a(10^5 + 1) + b(10^4 + 10) + c (10^3 + 10^2)
#	      = 11 ( 9091a + 910b + 100c)
# so m and n must be between 10, 90

tableMN = []

for i in range(9, 0, -1):
	for j in range(9, -1, -1):
		for k in range(9, -1, -1):
			num = 9091 * i + 910 * j + 100 * k
			for z in range(90, 9, -1):
				if (num % z == 0):
					if (num / z < 999):
						tableMN.append(num * 11)


tableMN.sort()
print max(tableMN)
