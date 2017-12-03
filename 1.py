
# AoC Day 1-1

cap = [int(x) for x in open("1.txt", "r").read()]
sum = 0

for i, c in enumerate(cap):
	if (c == cap[(i + 1) % len(cap)]): sum += c

print(sum)


# AoC Day 1-2

cap = [int(x) for x in open("1.txt", "r").read()]
l = len(cap)
sum = 0

for i, c in enumerate(cap):
	if (c == cap[(i + int(l / 2)) % l]): sum += c

print(sum)
