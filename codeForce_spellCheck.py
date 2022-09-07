t = int(input())

for _ in range(t):

	num = int(input())

	name = input()

	if len(name)==5 and ''.join(sorted(name))=="Timru":

		print("YES")
	else:
		print("NO")