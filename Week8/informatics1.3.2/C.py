a = int(input())
i = 1
print(str(1) + " ", end='')
while i < a + 1:
    if 2*i < a + 1:
        print(str(2*i) + " ", end='')
    i *= 2
