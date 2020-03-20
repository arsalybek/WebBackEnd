# first_last6
def first_last6(nums):
    return nums[0] == 6 or nums[len(nums) - 1] == 6


# common_end
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]


# reverse3
def reverse3(nums):
    nums.reverse()
    return nums


# middle_way
def middle_way(a, b):
    array = [a[len(a) / 2], b[len(b) / 2]]
    return array


# same_first_last
def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]


# sum3
def sum3(nums):
    summa = 0
    for i in nums:
        summa += i
    return summa


# max_end3
def max_end3(nums):
    maxi = nums[0]
    if maxi < nums[-1]:
        maxi = nums[-1]
    for i in range(len(nums)):
        nums[i] = maxi
    return nums


# make_ends
def make_ends(nums):
    return [nums[0], nums[-1]]


# make_pi
def make_pi():
    return [3, 1, 4]


# rotate_left3
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]


# sum2
def sum2(nums):
    if len(nums) <= 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    return nums[0] + nums[1]


# has23
def has23(nums):
    for i in range(len(nums)):
        if nums[i] == 3 or nums[i] == 2:
            return True
        return False
