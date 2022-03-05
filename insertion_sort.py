
def insertion_sort(arr):

	for i in range(1,len(arr)):

		key = arr[i]
		j= i-1

		while j >=0 and arr[j] >= key:
			arr[j+1] = arr[j]


			j-=1

		arr[j+1] = key



arr = [5,4,6,3,3,3,-2,-1,0,-5,102]

insertion_sort(arr)
print(arr)

