
# AoC Day 3-1

import math

n = 361527
c = int(math.sqrt(n))
if (c % 2 == 0): c -= 1
r = n - (c * c)

# Works by finding largest odd-square corner (c), calculating
# the overflow (r), and then finding the distance based on above.

test = abs((r % (c + 1)) - ((c + 1) // 2)) + (c // 2)
# Handles case of perfect (odd) square (e.g. 25)
test = (test + 1) if (r != 0) else (test - 1)

print(test)


# AoC Day 3-2

def move(coord, d):
	if (d == 0): return (coord[0] + 1, coord[1])
	elif (d == 1): return (coord[0], coord[1] + 1)
	elif (d == 2): return (coord[0] - 1, coord[1])
	elif (d == 3): return (coord[0], coord[1] - 1)

def sum(coord):
	sum = 0
	for x in (-1, 0, 1):
		for y in (-1, 0, 1):
			if (x == 0 and y == 0): pass
			temp = (coord[0] + x, coord[1] + y)
			if (temp in map): sum += map[temp]
	return sum



n = 361527
map = {(0, 0): 1}

d = 3
coord = (0,0)
while (map[coord] < n):
	nextd = (d + 1 ) % 4
	while (True):
		coord = move(coord, d)
		map[coord] = sum(coord)
		if (move(coord, nextd) not in map or map[coord] >= n):
			break
	d = nextd

print(map[coord])

