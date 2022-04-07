
# Find minimum number of boat required to travel people . one boat can weigh 2 person mostly whose weight  <=limit

def findBoat(arr,limit):
	
	i =0
	count = 0
	arr.sort()
	j= len(arr)-1

	while i <=j:
		if arr[i] + arr[j] <= limit:
			i +=1

		j -=1
		count +=1
	return count
arr = [3,5,3,4]

limit=5

print(findBoat(arr,limit))