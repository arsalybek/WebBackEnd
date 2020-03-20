a = int(input())
array = [int(i) for i in input().split()]
i = 0
cnt = 0
for x in array:
	if x > 0:
		cnt += 1
	i += 1
print(cnt)