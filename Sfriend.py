
t = int(input())


def output(paint,row,col):

	numOftree = 0

	for s in range(row):

		for t in range(col):

			if paint[s][t] == "^":numOftree +=1


	if (row ==1 or col == 1) and numOftree:return "imp"

	if numOftree ==0:return "cpos"

	return "pos"

for u in range(1,t+1):

	N,K = map(int,input().split())

	painting = []

	for j in range(N):

		painting.append(list(input()))

	print("Case #{}:".format(u),end="")
	result = output(painting,N,K)

	if result == "cpos":

		print(" Possible")

		for x in range(N):

			for  w in range(K) :

				print(".",end="")
			print()

	elif result == "pos" :
		print(" Possible")

		for a in range(N):

			for b in range(K):

				print("^",end="")

			print()
	else:
		print(" Impossible")



