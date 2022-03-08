temp = []
ans = []
def combinations(n,l,k):

	if k ==0 :
		print(temp)
		ans.append(temp)
		return 


	for i in range(l,n+1):

		temp.append(i)

		combinations(n,i+1,k-1)

		temp.pop()

num = int(input())
k = int(input())
combinations(num,1,k)
print(ans)


