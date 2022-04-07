

def bubble_sort(arr):
	lenn = len(arr)

	for i in range(lenn):

		for j in range(lenn-1):

			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [465,5,4,3,6,-1,-5,0]
bubble_sort(arr)
print(arr)