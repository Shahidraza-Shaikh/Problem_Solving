

def climbStare(n,dp):

	if n==0 :
		return 1

	if n <0 :
		return 0

	if dp[n] != -1 :
		return dp[n]

	oneStep = climbStare(n-1,dp)

	twoStep = climbStare(n-2,dp)

	dp[n] = oneStep + twoStep

	return dp[n]

n = 3

dp = [-1 for i in range(n+1)]

res = climbStare(n,dp)

print(res)