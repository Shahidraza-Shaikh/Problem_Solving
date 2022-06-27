

def subsequence(arr,idx,temp_arr):

	if idx >=len(arr) :

		if len(temp_arr) != 0 :

			print(temp_arr)
			# pass		

		if len(temp_arr) == 0:
			print(temp_arr)
		return 

	temp_arr.append(arr[idx])

	subsequence(arr,idx+1,temp_arr)

	temp_arr.pop(-1)


	subsequence(arr,idx+1,temp_arr)


arr = [1,2,3]
temp_arr = []

subsequence(arr,0,temp_arr)



