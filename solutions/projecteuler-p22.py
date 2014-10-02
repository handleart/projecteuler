#Project Euler, Problem 22

#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand 
#first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
#multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
#is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

#What is the total of all the name scores in the file?

#-*- coding: utf-8 -*-

import csv

with open('p022_names.txt', 'rb') as csvfile:
	r = csv.reader(csvfile, delimiter=',')
	row = [row for row in r][0]
	row.sort()

print len(row)

vals = 'abcdefghijklmnopqrstuvwxyz'
score = {}
i = 1

nameScore = []

tmp = 0
tmpTotal = 0

for s in vals:
	score[s] = i
	i += 1

i = 1
for n in row:
	name = n.lower()
	for letter in name:
		tmp = tmp + score[letter]
#		if name == 'colin':
#			print score[letter]
#			print i
	#nameScore.append(tmp * i)
	tmpTotal = tmpTotal + tmp * i
	i += 1
	tmp = 0

#print sum(nameScore)
print tmpTotal