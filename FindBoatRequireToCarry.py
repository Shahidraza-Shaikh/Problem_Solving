

def boatRequire(arr,limit):

	result = []
	count = 0
	for a in range(len(arr)):
		if arr[a] == limit:
			count +=1
		elif arr[a] < limit :
			result.append(arr[a])
		elif arr[a] > limit:

			temp = arr[i] //limit

			count +=temp

			result.append(arr[i]%limit)

	return count+(sum(result)//limit)

ar =  [3,3,5,4]
print(boatRequire(ar,5))