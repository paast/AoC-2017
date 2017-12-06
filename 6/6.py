
# AoC Day 6-1 && 6-2

input = tuple([int(x) for x in open("6.txt", "r").read().split()])

um = {}
it = 0

while (input not in um):
	um[input] = it
	m = input.index(max(input))
	temp = list(input)
	temp[m] = 0
	for x in range(input[m]):
		temp[(m + 1 + x) % len(temp)] += 1
	input = tuple(temp)
	it += 1

print('\nTotal Cycles:', it)
print('\nLoop Cycles:', it - um[input])









