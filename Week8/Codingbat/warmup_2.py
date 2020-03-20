# sing_times
def string_times(s, n):
    part = s
    s = ""
    for i in range(n):
        s += part
    return s


# front_times
def front_times(s, n):
    part = s
    s = ""
    for i in range(n):
        s += part[0:3]
    return s


# string_splosion
def string_splosion(s):
    res = ""
    for i in range(len(s)):
        res += s[:i + 1]
    return res


# array_front9
def array_front9(nums):
    for i in range(len(nums)):
        if nums[i] == 9:
            if i == 0 or i == 1 or i == 2 or i == 3:
                return True
    return False


# last2
def last2(s):
    sub = s[len(s) - 2:len(s)]
    cnt = 0
    for i in range(len(s) - len(sub)):
        if s[i:i + len(sub)] == sub:
            cnt += 1
    print(cnt)


# array123
def array123(nums):
    my_string = ""
    for i in range(len(nums)):
        my_string += str(nums[i])
    if '123' in my_string:
        return True
    else:
        return False


# string_bits
def string_bits(s):
    i = 0
    res = ""
    while len(s) > 0 and i < len(s):
        res += s[i]
        i += 2
    return res


# array_count9
def array_count9(nums):
    cnt = 0
    for i in nums:
        if i == 9:
            cnt += 1
    return cnt


# string_match
def string_match(a, b):
    short = min(len(a), len(b))
    cnt = 0
    for i in range(short - 1):
        a_sub = a[i:i + 2]
        b_sub = b[i:i + 2]
        if a_sub == b_sub:
            cnt = cnt + 1
    return cnt
