# sleep_in
def sleep_in(weekday, vacation):
    if not weekday and (not vacation or vacation):
        return True
    if weekday and not vacation:
        return False
    else:
        return True


# diff21
def diff21(n):
    if n > 21:
        return 2 * (abs(n - 21))
    return abs(21 - n)


# near_hundred
def near_hundred(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False


# missing_char
def missing_char(s, n):
    res = ""
    for i in range(len(s)):
        if i == n:
            continue
        else:
            res += s[i]
    return res


# monkey trouble
def monkey_trouble(a_smile, b_smile):
    return not (a_smile ^ b_smile)


# parrot_trouble
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


# pos_neg
def pos_neg(a, b, negative):
    if negative and a < 0 and b < 0:
        return True
    elif not negative and ((a < 0 and b > 0) or (a > 0 and b < 0)):
        return True
    else:
        return False


# front_back
def front_back(s):
    if len(s) < 2:
        return s
    else:
        return s[-1] + s[1:-1] + s[0]


# sum_double
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b


# makes10
def makes10(a, b):
    if (a == 10 or b == 10) or a + b == 10:
        return True
    else:
        return False


# not_string
def not_string(s):
    if s.find('not') == 0:
        return s
    else:
        return "not" + " " + s


# front3
def front3(s):
    if s < 3:
        return s
    else:
        return s[0:3] + s[0:3] + s[0:3]
