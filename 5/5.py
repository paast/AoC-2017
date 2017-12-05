
# AoC Day 5-1

input = [int(x) for x in open("5.txt", "r")]

pos = 0
i = 0
while (-1 < pos < len(input)):
	move = input[pos]
	input[pos] += 1
	pos += move
	i += 1

print(i)


# AoC Day 5-2

input = [int(x) for x in open("5.txt", "r")]

pos = 0
i = 0
while (-1 < pos < len(input)):
	move = input[pos]
	if (input[pos] < 3):
		input[pos] += 1
	else:
		input[pos] -= 1
	pos += move
	i += 1

print(i)
