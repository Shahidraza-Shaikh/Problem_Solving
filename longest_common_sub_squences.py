

##.....###.....######## Top Down Approach for finding longest common sub sequence


# Brute Force Method 

def longestSubSeq(m,n,str1,str2):

	if m == 0 or n == 0:
		return 0

	if str1[m-1] == str2[n-1]:
		return 1 + longestSubSeq(m-1,n-1,str1,str2)
	else:

		return max(longestSubSeq(m,n-1,str1,str2),longestSubSeq(m-1,n,str1,str2))

str1 = "ABCAB"
str2 = "AECB"
m = len(str1)
n = len(str2)

result = longestSubSeq(m,n,str1,str2)

print(result)