

arr =[5,1,7]
target_amt = 18

# Brute Force approach of O(m^n) complexity 
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


# Optimal approach 

dp = [-1 for i in range(target_amt+1)]

def minCoin(target_amt,arr,dp):

	if target_amt == 0:
		return 0

	maxSum = float('inf')
	for i in range(len(arr)):

		if target_amt - arr[i] >=0 :

			ans = 0

			if maxSum != ans and maxSum +1 <ans:
				



