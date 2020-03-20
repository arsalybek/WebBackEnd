def minimum(numbers):
    mini = numbers[0]
    for i in range(len(numbers)):
        if mini > numbers[i]:
            mini = numbers[i]
    return mini

array = [int(i) for i in input().split()]
print(minimum(array))
