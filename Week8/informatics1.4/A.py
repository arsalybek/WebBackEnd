a = int(input())
array = [int(i) for i in input().split()]
i = 0
for x in array:
	if i % 2 == 0:
		print(x)
	i += 1