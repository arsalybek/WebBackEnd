a = int(input())
array = [int(i) for i in input().split()]
found = False
for i in range(1,len(array) - 1):
    if array[i] * array[i + 1] > 0:
        found = True
        break
if found:
    print("YES")
else:
    print("NO")
