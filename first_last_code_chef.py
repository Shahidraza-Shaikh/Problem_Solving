t = int(input())

for _ in range(t):
	N = int(input())
	arr = list(map(int,input().split(' ')))
	maxx = 0
	for i in range(N-1):

		if arr[0] + arr[-1] > maxx:

			maxx = arr[0] + arr[-1]

		arr = [arr[-1]] + arr[:-1]
	print(maxx)

