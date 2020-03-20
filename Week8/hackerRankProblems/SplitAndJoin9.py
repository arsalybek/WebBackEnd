a = input()
s = [s(sub) for sub in a.split()]
res = ''
for x in s:
    res += x + "-"

print(res[:len(res) - 1])

# line = input()
# words = line.split(' ')
# print('-'.join(words))