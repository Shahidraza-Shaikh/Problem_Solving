

# Find element in Sorted and rotated array in O(logn)

def binSearch(arr,l,r,k):
	if l <= r:
		mid = (l+r)//2

		if arr[mid] ==  k:
			return mid
		if arr[l] < arr[mid]:
			if k >= arr[l] and k <arr[mid]: #[5,6,7,8,9,10,1,2,3]
											# l          k      r
				return binSearch(arr,l,mid-1,k)
			else:
				return binSearch(arr,mid+1,r,k)

		else:
			
			if k > arr[mid]  and k <= arr[r]:
				return	binSearch(arr,mid+1,r,k)
			else:
				return binSearch(arr,l,mid-1,k)

	return -1



# arr = [5,6,7,8,9,10,1,2,3,4,5]
arr = [1,2,5,8,9]

print(binSearch(arr,0,len(arr)-1,9))