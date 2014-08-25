#Project Euler, Problem 14
#Longest Collatz sequence

#

nDictCalced = {}

numList = []
maxLen = 0
nMaxLen = 0

nDictCalced[1] = 1
nDictMap = {}

numRange = xrange(1000000, 1, -1)

#calc evens:

for n in numRange:
	i = 0
	nTmp = n
	while nTmp > 1:
		if nTmp in nDictMap:
			i = i + nDictMap[nTmp]
			break	
		if (nTmp % 2 == 0):
			nTmp = nTmp / 2
			i += 1
		elif (nTmp % 2 == 1):
			nTmp = 3*nTmp + 1
			i += 1
		
	nDictMap[n] = i + 1


maxLen = 0
maxNum = 0

for key in nDictMap.keys():
	if nDictMap[key] > maxLen:
		maxLen = nDictMap[key]
		maxNum = key

print maxLen, maxNum



