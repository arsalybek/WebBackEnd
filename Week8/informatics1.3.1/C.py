from math import*
a = int(input())
b = int(input())

for x in range(a, b + 1):
	y = floor(sqrt(x))
	if y * y == x:
		print(x)
