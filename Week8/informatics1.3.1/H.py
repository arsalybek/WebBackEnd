a = int(input())

for x in range(a + 1):
    if x == 0:
        continue
    if a % x == 0:
        print(str(x) + " ", end='')