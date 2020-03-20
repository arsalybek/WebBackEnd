a = int(input())
array = [int(i) for i in input().split()]
maxi1 = -10000
maxi2 = -10001
for i in range(len(array)):
    if array[i] > maxi1:
        maxi2 = maxi1
        maxi1 = array[i]
    elif array[i] > maxi2:
        maxi2 = array[i]
print(maxi2)
