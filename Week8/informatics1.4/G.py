a = int(input())
array = [int(i) for i in input().split()]
array.reverse()
for i in range(len(array)):
    print(str(array[i]) + " ", end='')
