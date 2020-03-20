# cigar_party
def cigar_party(cigars, is_weekend):
    if 40 <= cigars <= 60 and is_weekend is False:
        return True
    if cigars >= 40 and is_weekend is True:
        return True
    return False


# caught_speeding
def caught_speeding(speed, is_birthday):
    if speed <= 60 and is_birthday is False:
        return 0
    if 61 <= speed <= 80 and is_birthday is False:
        return 1
    if speed <= 65 and is_birthday is True:
        return 0
    if 66 <= speed <= 85 and is_birthday is True:
        return 1
    else:
        return 2


# love6
def love6(a, b):
    if a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6:
        return True
    return False


# date_fashion
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you > 8 or date > 8:
        return 2
    return 1


# sorta_sum
def sorta_sum(a, b):
    if 10 <= a + b <= 19:
        return 20
    return a + b


# in1to10
def in1to10(n, outside_mode):
    if (outside_mode and (1 >= n or n >= 10)) or (not outside_mode and 1 <= n <= 10):
        return True
    return False


# squirrel_play
def squirrel_play(temp, is_summer):
    if (is_summer and 60 <= temp <= 100) or (not is_summer and 60 <= temp <= 90):
        return True
    return False


# alarm_clock
def alarm_clock(day, vacation):
    if 1 <= day <= 5 and not vacation:
        return "7:00"
    elif (0 == day or day == 6) and vacation:
        return "off"
    elif (1 <= day <= 5 and vacation) or (0 <= day <= 6 and not vacation):
        return "10:00"


# near_ten
def near_ten(num):
    return (num + 2) % 10 <= 4
