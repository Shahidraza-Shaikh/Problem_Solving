

# def stockBySell(arr,n):

# 	start = end = 0
# 	minn=0
# 	result = []
# 	for i in range(n):
# 		temp = arr[i]
# 		for j in range(i+1,n-1):
# 			if abs(temp - arr[j]) > minn :
# 				minn = abs(temp - arr[j])
# 				result.append((i,j))
# 				start = i
# 				end = j

# 				# if
# 			else:
# 				start =i
# 				result.append((i,j))
# 	return start , end+1 , result



arr = [100,180,260,310,40,535,695]
# arr = [23,13,25,29,33,19,34,45,65,67]

# print(stockBySell(arr,len(arr)))

def stockBySell(arr,n):  #Pending

	minSoFar = arr[0]
	maxProfit = arr[0]

	for i in range(n):
		
		if arr[i] < minSoFar:
			minSoFar = arr[i]
		if abs(minSoFar -arr[i]) < maxProfit:
			maxProfit = abs(maxProfit-arr[i])

	return minSoFar , maxProfit

print(stockBySell(arr,len(arr)))

