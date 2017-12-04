
# AoC Day 4-1

sum = 0

for line in open("4.txt", "r"):
	s = set({})
	r = 0
	for word in line.split():
		if (word in s):
			r = 1
			break
		else:
			s.add(word)
	if (r == 0):
		sum += 1

print(sum)
		

# AoC Day 4-2

sum = 0

for line in open("4.txt", "r"):
	s = set({})
	r = 0
	for word in line.split():
		word = ''.join(sorted(word))
		if (word in s):
			r = 1
			break
		else:
			s.add(word)
	if (r == 0):
		sum += 1

print(sum)







