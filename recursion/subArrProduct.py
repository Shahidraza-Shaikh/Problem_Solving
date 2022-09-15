def genSubSeq(arr,i,temp_arr):

	if i >=len(arr):

		# if s == summ:
		print(temp_arr)

		return 

	temp_arr.append(arr[i])

	# s *=arr[i]
	genSubSeq(arr,i+1,temp_arr)

	# s //=arr[i]

	temp_arr.pop()

	genSubSeq(arr,i+1,temp_arr)

arr = [1,0,1]

temp = []
genSubSeq(arr,0,temp)

