
def BinarySearch(mat,low,high,target):
	# print(mat)

	while low <= high :

		mid = (low +high)//2
		# print(mid)

		if target == mat[mid] :

			return mid

		elif target < mat[mid] :

			high = mid -1
		elif target > mat[mid] :

			low = mid +1

arr = [[2,4,5,8],[9,10,11,12],[13,14,15,16]]

target = 4

for row in range(len(arr)):

	res = BinarySearch(arr[row],0,len(arr[row])-1,target)

	if res is not None:
		print("found at row %d and column %d"%(row,res))
		break

if res is None:

	print("element not found")


