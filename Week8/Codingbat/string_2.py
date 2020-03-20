# double_char
def double_char(s):
    res = ""
    for i in range(len(s)):
        res += s[i] + s[i]
    return res


# count_code
def count_code(s):
    cnt = 0
    for i in range(len(s) - 3):
        if s[i:i + 2] == "co" and s[i + 3] == "e":
            cnt += 1
    return cnt


# count_hi
def count_hi(s):
    cnt = 0
    for i in range(len(s) - 1):
        if s[i:i + 2] == "hi":
            cnt += 1
    return cnt


# end_others
def end_other(a, b):
    a = a.upper()
    b = b.upper()
    if a.endswith(b) or b.endswith(a):
        return True
    return False


# cat_dog
def cat_dog(s):
    if s.count("cat") == s.count("dog"):
        return True
    return False


# xyz_there
def xyz_there(s):
    for i in range(len(s) - 2):
        if s[i:i + 3] == "xyz":
            if s[i - 1] != ".":
                return True
    return False
