
'''
def genSubSeq(arr,i,s,summ,temp_arr):

	if i >=len(arr):

		if s == summ:
			print(temp_arr)

		return 

	temp_arr.append(arr[i])

	s +=arr[i]
	genSubSeq(arr,i+1,s,summ,temp_arr)

	s -=arr[i]

	temp_arr.pop()

	genSubSeq(arr,i+1,s,summ,temp_arr)

'''


# If you want to stop recursion on first output 
# summ = 4

# [1, 2, 1] when this array print that is first the recursion stops
# [1, 3]
# [1, 3]
# [4]
# Below solution

'''
def genSubSeq(arr,i,s,summ,temp_arr):

	if i >= len(arr):

		if s == summ :
			print(temp_arr)

			return True
		else:
			return False

	s +=arr[i]
	temp_arr.append(arr[i])

	if genSubSeq(arr,i+1,s,summ,temp_arr) : return True

	s -= arr[i]
	temp_arr.pop()
	if genSubSeq(arr,i+1,s,summ,temp_arr) : return True

	return False

'''

# return only Count that how many time a subsequence found having sum= K

def genSubSeq(arr,i,s,summ):

	if i >= len(arr):

		if s == summ :
			return 1
		else:
			return 0

	s +=arr[i]
	temp_arr.append(arr[i])

	left = genSubSeq(arr,i+1,s,summ)

	s -= arr[i]
	right = genSubSeq(arr,i+1,s,summ)

	return left + right

arr = [1,2,1,3,4]

summ = 11
temp_arr = []
count = genSubSeq(arr,0,0,summ)

print(count)




