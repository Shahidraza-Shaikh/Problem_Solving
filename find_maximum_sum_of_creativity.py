t = int(input())
for i in range(t):
	n = int(input())

	C = list(map(int,input().split()))  #[12,8,18,6,15,4,18,15,3] #[12,10,6,2,14,14,5,1,9] #[12,8,18,6,15,4,18,15,3] #[2,4,1,5]

	H = list(map(int,input().split())) #[16,20,19,17,15,15,19,14,14] #[5,6,7,8,9,5,10,9,12] #[16,20,19,17,15,15,19,14,14] #[1,2,2,1] # [(1,1),(1,5),(2,4),(2,1)]

	k = int(input())

	zipped_arr = list(zip(H,C))

	ziped = sorted(zipped_arr)

	temp = float("-inf")
	res = []

	if len(set(H)) < k :
		print(f"Case {i}:",-1)
		continue
	for a in range(n):

		if ziped[a][0] != temp :

			temp = ziped[a][0]
			res.append(ziped[a][1])
		else:

			if ziped[a][1] > res[-1] :

				res.pop()

				res.append(ziped[a][1])

	print(f"Case #{i}:",sum(sorted(res,reverse=True)[:k]))

