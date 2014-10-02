#Project Euler, Problem 11

import csv
from time import sleep
from functools import reduce

def getList():
	sepVal = ''
	xList = []
	yList = []

	with open('problem11.csv', 'rU') as csvfile:
		loadNum = csv.reader(csvfile, dialect=csv.excel_tab)

		for row in loadNum:
			for val in row[0]:
				if val == ',':
					xList.append(int(sepVal))
					sepVal = ''
				elif val == '|':
					continue
				else:
					sepVal = sepVal + val
				#sleep(0.5)
			yList.append(xList)
			xList = []
				
		return yList

#main method to call
def gridMul(gridList, numLen):
	x = max(gridMulx(gridList, numLen))
	y = max(gridMuly(gridList, numLen))
	d1 = max(gridMuldRL(gridList, numLen))
	d2 = max(gridMuldLR(gridList, numLen))
	
	return max(x, y, d1, d2)

#x axis
def gridMulx(gridList, numLen):
	mulxy = []
	mulx = []

	for row in gridList:
		for i in range(len(row) - numLen - 1):
			mulVal = reduce(lambda x,y: x*y, row[i:i+numLen])
			mulx.append(mulVal)
		mulxy.append(max(mulx))

	return mulxy

#y axis
def gridMuly(gridList,numLen):	
	gridListZip = zip(*gridList)

	return gridMulx(gridListZip, numLen)

#diagnol -- left to right, assume square
def gridMuldLR(gridList, numLen):
	return gridMuldHelper(gridList, numLen,'LR')

#diagnol -- right to left, assume square
def gridMuldRL(gridList, numLen):
	return gridMuldHelper(gridList, numLen, 'RL')

def gridMuldHelper(gridList, numLen, direction):
	mulx = []
	mulxy = []
	val = []

	if direction == 'LR': 
		ind = -1
		iRange = range(len(gridList) -1 , numLen - 1, ind)
		jRange = range(0, len(gridList) - numLen + 1 )
	elif direction == 'RL':
		ind = 1
		iRange = range(0, len(gridList) - numLen + 1)
		jRange = range(0, len(gridList) - numLen + 1)
	else:
		raise Exception('wrong direction')


	for i in iRange:
		for j in jRange:
			#print range(numLen)
			for k in range(numLen):
				#print k
				val.append(gridList[i+k*ind][j+k])
		
			#val = [gridList[i][j], gridList[i+ind][j+1], gridList[i+2*ind][j+2], gridList[i+3*ind][j+3]]
			mulVal = reduce(lambda x,y: x*y, val)
			val = []
			mulx.append(mulVal)
		
		mulxy.append(max(mulx))

	return mulxy

x = getList()
print(gridMul(x, 4))
