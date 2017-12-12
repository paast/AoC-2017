
# AoC Day 11

# a = b = c = 0

# for d in open("11.txt").read().strip().split(","):
# 	if (d == 'n'): b += 1
# 	elif (d == 'ne'): c += 1
# 	elif (d == 'se'): a -= 1
# 	elif (d == 's'): b -= 1
# 	elif (d == 'sw'): c -= 1
# 	elif (d == 'nw'): a += 1

# print(a, b, c)

def dist(x):
	b = x['n'] - x['s']
	a = x['nw'] - x['se'] + b
	c = x['ne'] - x['sw'] + b
	if ((a < 0) == (c < 0)):
		return (max(abs(a), abs(c)))
	else:
		return (abs(a) + abs(c))

dirs = {'n':0,'ne':0,'nw':0,'s':0,'sw':0,'se':0}
dists = []

for d in open("11.txt").read().strip().split(","):
	dirs[d] += 1
	dists.append(dist(dirs))

print(dist(dirs), max(dists))

