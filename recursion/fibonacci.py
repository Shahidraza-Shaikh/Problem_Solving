

def fibo(n,dp):

	if n <=1:
		return n

	if dp[n] != -1 :
		return dp[n]
	first = fibo(n-1,dp)

	second = fibo(n-2,dp)

	dp[n] = first + second

	return dp[n]

n = 8

dp = [-1 for i in range(n+1)]

res = fibo(n,dp)

print(res)

# 0 1 1 2 3 5 8 13 21