
# Question https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261


# Brute force for finding Max Sum of an Non Adjacent element

'''
def MaxSumNonAdj(nums,n):

	if n == 0 :
		return nums[n]

	if n  < 0 :
		return 0

	f1 = nums[n] + MaxSumNonAdj(nums,n-2)

	f2 = 0 + MaxSumNonAdj(nums,n-1)

	return max(f1,f2)

'''

# Optimized solution

def MaxSumNonAdj(nums,n,dp):

	if n == 0 :
		return nums[n]

	if n  < 0 :
		return 0
	if dp[n] != -1 :
		return dp[n]

	f1 = nums[n] + MaxSumNonAdj(nums,n-2,dp)

	f2 = 0 + MaxSumNonAdj(nums,n-1,dp)

	dp[n] = max(f1,f2)

	return dp[n]

nums = [1,2,3,1,3,5,8,1,9]


n = len(nums) - 1

dp = [-1] * (n+1)

res = MaxSumNonAdj(nums,n,dp)

print(res)