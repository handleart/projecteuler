#permutation recursive algorithm 
#modifications of ones from stackoverflow


def all_perm(li):
	if len(li) <= 1: 
		yield li
	else:
		tmp = all_perm(li[1:])
		#for e in tmp:
		#	print tmp


		for perm in tmp:
			for i in range(len(li)):
				yield perm[:i] + li[0:1] + perm[i:]




def permutList(l):
	if not l:
		return [[]]

	ret = []

	for element in l:
		tmp = l[:]
		tmp.remove(element)

		ret.extend([[element] + r for r in permutList(tmp)])

	return ret

def permutListStr(l):
	if not l:
		return ['']

	ret = []

	for element in l:
		tmp = l.replace(element, '')

		ret.extend([element + r for r in permutListStr(tmp)])

	return ret

print permutListStr('abc')
