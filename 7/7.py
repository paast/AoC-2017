
# AoC Day 7-1 && Day 7-2

class Node:
	total_weight = 0

	def __init__(self, info):
		self.name = info[0]
		self.weight = int(info[1][1:-1])
		if (len(info) > 2):
			self.children = info[3:]
			self.weighted = False
		else:
			self.children = None
			self.weighted = True
			self.total_weight = self.weight

	def getWeight(self, map):
		sum = self.weight
		if (self.weighted is False):
			for child in self.children:
				sum += map[child].getWeight(map)
			self.weighted = True
		else:
			return self.total_weight
		self.total_weight = sum
		return sum

	def __str__(self):
		return("<" + self.name + ">")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def oOO(list, map):
	ocm = {}
	rlm = {}
	for child in list:
		wt = child.total_weight
		name = child.name
		if (wt not in ocm): ocm[wt] = 0
		ocm[wt] += 1
		rlm [wt] = name
	if (len(ocm) > 1): 
		mx = max(ocm, key=lambda x: ocm[x])
		mn = min(ocm, key=lambda x: ocm[x])
		return (rlm[mn], abs(mx - mn))
	else: return (False, -1)
	

input = [line.replace(',', '').split() for line in open("7.txt", "r")]
nodes = {x[0]: Node(x) for x in input}

for node in nodes:
	nodes[node].getWeight(nodes)

root = max(nodes, key=lambda x: nodes[x].total_weight)

iroot = root
d = -1
while (True):
	new, diff = oOO([nodes[x] for x in nodes[iroot].children], nodes)
	if (new == False):
		break
	iroot = new
	d = diff

print("Root node // size: " +  root + " // " + str(nodes[root].total_weight))
print("Node to adjust // proper value: " + iroot + " // " + str(nodes[iroot].weight - d))

	











