a = int(input())


def sign(x):
    if x > 0:
        b = 1
    elif x < 0:
        b = -1
    else:
        b = 0
    return b


print(sign(a))
