a = int(input())
x = 1
while True:
	if x == a:
		print("YES")
		break
	if x > a:
		print("NO")
		break
	else:
		x *= 2
