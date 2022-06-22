
#Question  https://www.codingninjas.com/codestudio/problem-details/frog-jump_3621012

#### Brute Force Approach

'''
def FrogJump(n,heights):

	if n == 0:
		return 0

	first_step = FrogJump(n-1,heights) + abs(heights[n] - heights[n-1])

	second_step = int(1e9) + 7

	if n > 1 :

		second_step = FrogJump(n-2,heights) + abs(heights[n]- heights[n-2])

	return min(first_step,second_step)
'''


# Optimal approach using DP

def FrogJump(n,heights,dp):

	if n==0:
		return 0

	if dp[n] != -1:
		return dp[n]

	first_step = FrogJump(n-1,heights,dp) + abs(heights[n] - heights[n-1])

	second_step = int(1e9) + 7

	if n > 1 :

		second_step = FrogJump(n-2,heights,dp) +  abs(heights[n] -  heights[n-2])

	dp[n] = min(first_step,second_step)

	return dp[n]


heights =[7,5,5,8,4,9,1,1,10]

n = len(heights)-1

dp = [-1] * (n+1)
result = FrogJump(n,heights,dp)

print(result)