discSizes = [7, 13, 3, 5, 17, 19, 11]
initialStates = [0, 0, 2, 2, 0, 7, 0]

t0=0
remainders = [(n + t0 + i) % s for n, i, s in zip(range(1, 8), initialStates, discSizes)]

while sum(remainders) > 0:
	t0 += 1
	remainders = [(n + t0 + i) % s for n, i, s in zip(range(1, 8), initialStates, discSizes)]
	#print t0, remainders

print t0