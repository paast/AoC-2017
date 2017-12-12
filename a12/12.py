
# AoC Day 12

input = open("12.txt")
map = {}
net = set({})

for line in input:
	line = line.replace(',', '').split()
	map[line[0]] = line[2:]

def fill(n):
	links = map[n]
	for link in links:
		if (link not in net):
			net.add(link)
			fill(link)

fill('0')

print("Size of program-0 network:", len(net))

net = set({})
nnet = 0

for key in map:
	if (key not in net):
		fill(key)
		nnet += 1

print("Number of network", nnet)





