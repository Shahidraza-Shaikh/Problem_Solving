
def lengthOfLongestSubstring(string):

	di = dict.fromkeys(list(range(255)),-1)
	start = -1
	mx = 0

	for i in range(len(string)):

		if di[string[i]] > start :
			start = di[string[i]] 