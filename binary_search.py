

def binary_search(arr,l,h,key):
	if l <=h:
		mid = (l+h)//2


		if arr[mid] == key:

			return mid
		if arr[mid] > key :
			return binary_search(arr,l,mid-1,key)

		return binary_search(arr,mid+1,h,key)
	return -1

arr = [-5,0,4,5,8,9,10,56,89]
key = 454
print(binary_search(arr,0,len(arr)-1,key))