with open('input.txt', 'r') as f:
	chars = f.read()
	floor = 0
	for i, char in enumerate(chars):
		if char == '(':
			floor += 1
		if char == ')':
			floor -= 1
		if floor < 0:
			break
print(i+1)
