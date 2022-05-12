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

# Find combinations of array
# Output :-

# if n = 4 and k=2
# [1,2,3,4]  nCr i.e 4C2 == n!/k!(n-k)!

# [[1,2],
#  [1,3],
#  [1,4],
#  [2,3],
#  [2,4],
#  [3,4]
# ]
