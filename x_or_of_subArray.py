

def subarray(arr,n):
	ar=[]

	for i in range(n+1):

		for j in range(i):
			if len(arr[j:i])>1 : 
				ar.append(arr[j:i])

	return ar

ar = [1,2,3,4]
Q = 2
query = [[1,2],[3,8]]
x_or_arr = []
for i in range(Q):
	q1,q2 = query[i]

	ar[q1-1] = q2 
	print('modified_arr',ar)

	arr = subarray(ar,len(ar))
	print("sub array",arr)
	x_or_out_sum =0
	for a in arr:
		x_or_in_sum =0

		for j in a:
			x_or_in_sum = x_or_in_sum ^ j

		x_or_out_sum = x_or_out_sum ^ x_or_in_sum
		x_or_in_sum =0
	x_or_arr.append(x_or_out_sum)
print("X-OR of sub array",x_or_arr)

subarray(ar,len(ar))

# output : -

# modified_arr [2, 2, 3, 4]
# sub array [[2, 2], [2, 2, 3], [2, 3], [2, 2, 3, 4], [2, 3, 4], [3, 4]]
# modified_arr [2, 2, 8, 4]
# sub array [[2, 2], [2, 2, 8], [2, 8], [2, 2, 8, 4], [2, 8, 4], [8, 4]]
# X-OR of sub array [7, 12]
