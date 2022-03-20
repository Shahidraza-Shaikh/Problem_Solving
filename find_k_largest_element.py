
def left_Child(i):
	return i*2 +1


def right_child(i):
	return i*2 +2


def heapify(arr,i,n):

	left = left_Child(i)

	right = left_Child(i)

	largest = i

	if left < n and arr[left] > arr[largest]:

		largest = left
	if right < n and arr[right] > arr[largest]:
		largest = right 

	if i != largest :

		arr[i] ,arr[largest] = arr[largest],arr[i]

		heapify(arr,largest,n)



arr = [12,11,13,5,6,7]
print(arr)
n = len(arr)
# heapify(arr,1,n)
# print(arr)
for i in range(n//2-1,-1,-1):
	heapify(arr,i,n)
print(arr)
k = 3
res = []
i = 0
for j in range(n-1,0,-1):

	# if i == k :
	# 	break

	arr[j],arr[0] = arr[0],arr[j]
	# res.append(arr[j])
	heapify(arr,0,j)

	# i +=1

print(arr)




