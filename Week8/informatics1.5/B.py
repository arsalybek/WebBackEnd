def to_power(n, m):
    power = 1
    for i in range(m):
        power *= n
    return power
a, b = input().split()
a = float(a)
b = int(b)
print(to_power(a, b))



