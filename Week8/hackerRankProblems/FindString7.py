main = input()
sub = input()
main_len = len(main)
sub_len = len(sub)
cnt = 0
for i in range(main_len):
    if main[i:i + sub_len] == sub:
        cnt += 1
print(cnt)
