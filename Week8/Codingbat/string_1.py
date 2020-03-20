# hello_name
def hello_name(name):
    return "Hello " + name + "!"


# make_out_word
def make_out_word(out, word):
    return out[:2] + word + out[2:]


# first_half
def first_half(s):
    return s[:len(s) // 2]


# non_start
def non_start(a, b):
    return a[1:] + b[1:]


# make_abba
def make_abba(a, b):
    return a + b + b + a


# extra_end
def extra_end(s):
    res = s[len(s) - 2:len(s)]
    return res + res + res


# without_end
def without_end(s):
    return s[1:len(s) - 1]


# left2
def left2(s):
    return s[2:len(s)] + s[:2]


# make_tags
def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"


# first_two
def first_two(s):
    if len(s) < 2:
        return s
    return s[:2]


# combo_string
def combo_string(a, b):
    if len(b) < len(a):
        return b + a + b
    return a + b + a
