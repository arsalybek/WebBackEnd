# make_bricks
def make_bricks(small, big, goal):
    if (goal % 5) <= small and (goal - (big * 5)) <= small:
        return True
    return False


# no_teen_sum
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if n == 15 or n == 16:
        return n
    elif 13 <= n <= 19:
        return 0
    return n


# lone_sum

def lone_sum(a, b, c):
    sum1 = 0
    if a != b and a != c:
        sum1 += a
    if b != a and b != c:
        sum1 += b
    if c != a and c != b:
        sum1 += c
    return sum1


# lucky_sum
def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c


# round_sum
def round10(num):
    round1 = num % 10
    if round1 >= 5:
        return num + 10 - round1
    return num - round1


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


# close_far
def close_far(a, b, c):
    a_b = abs(a - b)
    a_c = abs(a - c)
    b_c = abs(b - c)

    if (a_b <= 1 and a_c >= 2 and b_c >= 2) or (a_c <= 1 and a_b >= 2 and b_c >= 2):
        return True
    return False


# make_chocolate
def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        cur = goal - 5 * big
    else:
        cur = goal % 5
    if cur <= small:
        return cur
    return -1
