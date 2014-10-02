#Project Euler, Problem 17
#complicated solution to f all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

x = {}

firstTwenty =  ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

answer = ''

for num in range(1, 1001):
	numStr = str(num)
	tmpStr = ''

	#print numStr
	#print numStr[0]

	if len(numStr) == 4:
		tmpStr = firstTwenty[int(numStr[0])]
		tmpStr = tmpStr + 'thousand'

		if numStr[-3:] != '000':
			tmpStr = tmpStr + 'and'

	if len(numStr) >= 3:
		index = 0 if len(numStr) == 3 else 1
		#print len(numStr)
		#print index

		if numStr[-3:] != '000':
			tmpStr = tmpStr + firstTwenty[int(numStr[index])]
			#print numStr[1:3]
			if numStr[1:3] != '00' or len(numStr) == 3:
				tmpStr = tmpStr + 'hundred'

		if numStr[-2:] != '00' and numStr[1:3] != '00':
			tmpStr = tmpStr + 'and'

	if int(numStr[-2:]) < 20:
		#print numStr[-2:]
		#print len(firstTwenty)
		tmpStr = tmpStr + firstTwenty[int(numStr[-2:])]

	if 	int(numStr[-2:]) >= 20:
		tmpStr = tmpStr + str(tens[int(numStr[-2])])

		if numStr[-1] != '0':
			tmpStr = tmpStr + firstTwenty[int(numStr[-1])]

		# str(firstTwenty[int(numStr)[-1]]]) 

	answer = answer + tmpStr


print answer

print len(answer)