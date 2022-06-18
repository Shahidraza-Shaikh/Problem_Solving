

##.....###.....######## Top Down Approach for finding longest common sub sequence


# Brute Force Method 

'''

def longestSubSeq(m,n,str1,str2):

	if m == 0 or n == 0:
		return 0

	if str1[m-1] == str2[n-1]:
		return 1 + longestSubSeq(m-1,n-1,str1,str2)
	else:

		return max(longestSubSeq(m,n-1,str1,str2),longestSubSeq(m-1,n,str1,str2))

str1 = "ABCAB"
str2 = "AECBD"
m = len(str1)
n = len(str2)

result = longestSubSeq(m,n,str1,str2)

print(result)
'''



# Optimized approach using DP

str1 = "AECBD"
str2 = "ABCABD"
m = len(str1)
n = len(str2)


dp = [  [0 for j in range(n+1)] for i in range(m+1)]

for i in range(1,m+1):

	for j in range(1,n+1):

		dp[i][j] = -1

def longestSubSeq(m,n,str1,str2,dp):

	if m == 0 or n == 0:
		return 0
	# print(m,n)
	if dp[m][n] != -1 :
		return dp[m][n]

	if str1[m-1] == str2[n-1]:

		dp[m][n] = 1 + longestSubSeq(m-1,n-1,str1,str2,dp)

		return dp[m][n]

	else:

		dp[m][n] = max(longestSubSeq(m,n-1,str1,str2,dp) , longestSubSeq(m-1,n,str1,str2,dp))

		return dp[m][n]


result = longestSubSeq(m,n,str1,str2,dp)
print(dp)

print(result)
