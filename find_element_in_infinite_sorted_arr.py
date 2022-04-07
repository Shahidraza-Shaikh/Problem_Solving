

def binary_seach(arr,l,h,x):
	if l<=h:

		mid = (l+h)//2

		if arr[mid] == x:
			return mid
		if arr[mid] > x :

			return binary_seach(arr,l,mid-1,x)
		return binary_seach(arr,mid+1,h,x)
	return -1


def find_element(arr,x):

	l,h,val = 0 ,1, arr[0]

	while val < x :
		l = h
		h = 2*h
		# print(h)
		val = arr[h]

	return binary_seach(arr,l,h,x)

arr = [1,2,3,4,5,6,7,8,9,10,11]
x = 10
print(find_element(arr,x))