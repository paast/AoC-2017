
# AoC Day 9-1 & 9-2

input = open("9", "r").read()

garbo=skip = False
sum1=sum2=lay = 0

for char in input:
	if (skip): skip = False; continue
	if (not garbo):
		if (char == "{"): lay += 1
		elif (char == "}"): sum1 += lay; lay -= 1
		elif(char == "<"): garbo = True
	else:
		if (char == "!"): skip = True
		elif (char == ">"): garbo = False
		else: sum2 += 1

print("Group sum:", sum1)
print("Garbo sum:", sum2)
