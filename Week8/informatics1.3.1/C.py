from math import*

a = int(input())
b = int(input())

for x in range(a, b+1):
    if sqrt(pow(x, 2)) == x and pow(x, 2) < b+1:
        print(str(floor(pow(x, 2))) + " ", end='')
#wrong task
