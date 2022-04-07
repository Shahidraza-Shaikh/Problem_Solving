# # Python3 program to check a number
# # is a Happy number or not

# # Utility method to return
# # sum of square of digit of n
# def numSquareSum(n):
# 	squareSum = 0;
# 	while(n):
# 		squareSum += (n % 10) * (n % 10);
# 		n = int(n / 10);
# 	return squareSum;

# def isHappynumber(n):

# 	slow = n;
# 	fast = n;
# 	while(True):
		
# 		slow = numSquareSum(slow);

# 		fast = numSquareSum(numSquareSum(fast));
# 		if(slow != fast):
# 			continue;
# 		else:
# 			break;

# 	return (slow == 1);

# n = int(input());
# if (isHappynumber(n)):
# 	print(n , "is a Happy number");
# else:
# 	print(n , "is not a Happy number");

# # This code is contributed by mits


# Python3 program to find Minimum
# number of jumps to reach end

# Returns minimum number of jumps
# to reach arr[h] from arr[l]
def minJumps(arr, l, h):

	# Base case: when source and
	# destination are same
	if (h == l):
		return 0

	# when nothing is reachable
	# from the given source
	if (arr[l] == 0):
		return float('inf')

	# Traverse through all the points
	# reachable from arr[l]. Recursively
	# get the minimum number of jumps
	# needed to reach arr[h] from
	# these reachable points.
	min = float('inf')
	for i in range(l + 1, h + 1):
		if (i < l + arr[l] + 1):
			jumps = minJumps(arr, i, h)
			if (jumps != float('inf') and
					jumps + 1 < min):
				min = jumps + 1

	return min

# Driver program to test above function
arr = [2,2,2,9]
n = len(arr)
print('Minimum number of jumps to reach',
	'end is', minJumps(arr, 0, n-1))

# This code is contributed by Soumen Ghosh
