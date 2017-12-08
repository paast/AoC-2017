
# AoC Day 8-1

map = {}
maxs = []

for line in open("8.txt", "r"):
	line = line.split()
	tar = line[0]
	if (tar not in map): map[tar] = 0

	num = int(line[2])
	if (line[1] == "dec"): num *= -1

	a = line[4]
	cond = line[5]
	b = int(line[6])

	if (a not in map): map[a] = 0
	if (b not in map): map[b] = 0

	if (cond == ">"):
		if (map[a] > b): map[tar] += num
	elif (cond == "<"):
		if (map[a] < b): map[tar] += num
	elif (cond == ">="):
		if (map[a] >= b): map[tar] += num
	elif (cond == "<="):
		if (map[a] <= b): map[tar] += num
	elif (cond == "=="):
		if (map[a] == b): map[tar] += num
	elif (cond == "!="):
		if (map[a] != b): map[tar] += num

	maxs.append(max(map.values()))


print("Largest final value:", max(map.values()))
print("Largest process value:", max(maxs)) 
