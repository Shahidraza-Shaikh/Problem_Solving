t = int(input())

for _ in range(t):

	X,Y = map(int,input().split(' '))

	if Y <= X +200 and Y>=X:
		print("YES")
	else:
		print("NO")