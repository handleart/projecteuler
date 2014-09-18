#Project Euler, Problem 33
#Ardeshir Mostofi
#9/16/2014

#strings are immutable

#import re
import fractions

num = filter(lambda x: x % 10 != 0, range(10,100))
den = filter(lambda x: x % 10 != 0, range(10,100))
#num = range(10, 100)
#den = range(10, 100)

A = []


for i in num:
	for j in den: 
		if float(i) / float(j) < 1:
			# figure out if a number occurs in both num and den		
			word = str(i) + str(j)
			for k in word:
				if word.count(k) == 2 and str(i).count(k) == 1 and str(j).count(k) == 1:
					if(str(i).find(k)) == 1:
						n = int(str(i)[0])
					else:
						n = int(str(i)[1])

					if(str(j).find(k)) == 1:
						d = int(str(j)[0])
					else:
						d = int(str(j)[1])

					#if i == 49 and j == 98:
					#	print n, d, i, j
					#	break

					#figure out if the value is a non-trivial solution
					if float(i) / float(j) == float(n) / float(d):
						if i == 98 and j == 99:
							print i, j, n, d

						A.append((i, j))
			

			#if i / j < 1:
			#	print str(i) + '/' + str(j)

num = 1
dem = 1

for i in set(A):
	num *= i[0]
	dem *= i[1]

print fractions.Fraction(num, dem)


# i = 49
# j = 98
# A = []

# word = str(i) + str(j)
# for k in word:
# 	if word.count(k) > 1:
# 		if(str(i).find(k)) == 1:
# 			n = int(str(i)[0])
# 		else:
# 			n = int(str(i)[1])

# 		if(str(j).find(k)) == 1:
# 			d = int(str(j)[0])
# 		else:
# 			d = int(str(j)[1])



# 		if float(i) / float(j) == float(n) / float(d):
# 			A.append((i, j))
# 		break

# print A

