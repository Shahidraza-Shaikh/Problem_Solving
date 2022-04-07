
d = int(input('value of d '))

# using slicing

# def leftArrRotation(arr,d):

# 	arr1 = arr[:d]
# 	arr2 = arr[d:]

# 	return arr2 + arr1

# print(arrRotation([1,2,3,4,5,6,7,8],d))

# Using Algotrithm
arr = [1,2,3,4,5,6,7,8]

# 1st reverse [2,1,3,4,5,6,7,8]
# 2nd reverse [2,1,8,7,6,5,4,3]
# 3rd reverse [3,4,5,6,7,8,1,2] 

def reverseArray(arr,start,end):

	while start < end:
		temp = arr[start]
		arr[start], arr[end] = arr[end] , temp

		start +=1
		end -=1

def leftArrRotation(arr,d):

	d = d % len(arr)
	reverseArray(arr,0,d-1)
	reverseArray(arr,d,len(arr)-1)
	reverseArray(arr,0,len(arr)-1)

leftArrRotation(arr,d)
print(arr)

