a = int(input())
array = [int(i) for i in input().split()]
cnt = 0
for i in range(len(array) - 1):
	if array[i + 1] > array[i]:
		cnt += 1
print(cnt)