t = int(input())

for _ in range(t):

	num = int(input())

	grid1 = input()
	grid2 = input()

	Flag = True


	for i in range(num):

		if grid1[i] == grid2[i] or (grid1[i]=='G' and grid2[i]=='B') or (grid1[i]=='B' and grid2[i]=='G'):

			continue
		else:

			Flag =False

	if Flag:
		print("YES")
	else:
		print("NO")

