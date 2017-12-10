
# AoC Day 10-1

skip = reset = 0
hash = list(range(256))

for len in open("10.txt").readline().split(','):
	len = int(len)
	hash = hash[:len][::-1] + hash[len:]
	shift = (len + skip) % 256
	hash = hash[shift:] + hash[:shift]
	reset += shift
	skip += 1

reset = 256 - (reset % 256)
hash = hash[reset:] + hash[:reset]
print("Pre-hash Product: " + str(hash[0] * hash[1]))


# AoC Day 10-2

skip = reset = 0
hash = list(range(256))
input = [int(x) for x in open("10.txt", "rb").read()][:-2] + [17, 31, 73, 47, 23]

for i in range(64):
	for len in input:
		hash = hash[:len][::-1] + hash[len:]
		shift = (len + skip) % 256
		hash = hash[shift:] + hash[:shift]
		reset += shift
		skip += 1

reset = 256 - (reset % 256)
hash = hash[reset:] + hash[:reset]

dense = [0]*16

for i in range(16):
	sum = hash[16 * i]
	for j in range(1, 16):
		sum ^= hash[(16 * i) + j]
	dense[i] = sum

print("Dense Hash: " + ''.join(["{0:0{1}x}".format(x, 2) for x in dense]))
