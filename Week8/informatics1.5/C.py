def xOr(n, m):
    return (n+m) % 2


a, b = input().split()
a = int(a)
b = int(b)
print(xOr(a, b))
