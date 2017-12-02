
# AoC Day 2-1

input = [[int(x) for x in line.split()] for line in open("2.txt", "r")]
sum = 0

for line in input:
	sum += (max(line) - min(line))

print(sum)


# AoC Day 2-2

import itertools

input = [[int(x) for x in line.split()] for line in open("2.txt", "r")]
sum = 0

for line in input:
	for a, b in itertools.combinations(line, 2):
		if (a % b == 0):
			sum += a // b
			break
		elif (b % a == 0):
			sum += b // a
			break

print(sum)
