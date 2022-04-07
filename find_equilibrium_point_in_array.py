

arr = [1,2,3,4,-1]
total = sum(arr)
summ = []
def equilibirium(arr):
	total =0
	for i in range(len(arr)):
		total +=arr[i]

		summ.append(total)

	for j in range(1,len(arr)):

		lsum = summ[j] - arr[j]  # find left and right sum in optimal way using above for loop
		rsum = total - summ[j]
		# lsum = sum(arr[0:j])
		# rsum = sum(arr[j+1:])
		# print(lsum,rsum)
		if lsum == rsum :
			return j,arr[j]

	# print(temp)


print(equilibirium(arr))