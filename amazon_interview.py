

def code(arr):

	if len(arr)==2 :
		return arr

	temp = []

	for i in range(len(arr)-1):

		if arr[i] + arr[i+1] <= 9 :
			temp.append(arr[i]+arr[i+1])
		else:
			temp.append((arr[i] + arr[i+1])//10)

	return code(temp)

arr = [5,2,8,7]

print(code(arr))