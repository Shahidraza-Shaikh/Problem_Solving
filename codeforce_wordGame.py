t= int(input())

for _ in range(t):

	num = int(input())

	guy1 = list(map(str,input().split()))
	guy2 = list(map(str,input().split()))
	guy3 = list(map(str,input().split()))

	p1=p2=p3 = 0
	row = 3

	guys = []
	guys.append(guy1)
	guys.append(guy2)

	guys.append(guy3)

	ans = [0]*3
	freq = {}
	for x in range(row):

		for y in range(num):

			if guys[x][y] in freq:

				freq[guys[x][y]] +=1
			else:
				freq[guys[x][y]] = 1






	for x in range(3):

		for y in range(num):


			if freq[guys[x][y]] ==1 :

				ans[x] +=3
			if freq[guys[x][y]] ==2 :

				ans[x] +=1

	print(*ans)





