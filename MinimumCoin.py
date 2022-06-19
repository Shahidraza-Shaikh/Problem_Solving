

arr =[5,1,7]

def minCoin(arr,target_amt):

	if target_amt ==0:
		return 0

	ans = float("inf")
	for i in range(len(arr)):
		if target_amt - arr[i] >= 0:

			minSum = minCoin(arr , target_amt-arr[i] )

			if minSum !=ans and  minSum +1 < ans:
				ans = minSum +1
	return ans

res = minCoin(arr,18)

print(res)

# [5,1,7] --  for loop for [5,1,7]

# 							/			
# 						   minCoin(arr,13)
# 						 /
# 						minCoin(arr,8)

					   # /
					   # minCoin(arr,3)




