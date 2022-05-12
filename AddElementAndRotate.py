
# Incomplete solution


arr = [1,2,3]

temp = []
temp.append(arr[0])
for i in arr:
	mid = len(arr)//2
	lower_index = arr[:mid]
	print('l',lower_index)
	higher_index = arr[mid+1:]
	print('h',higher_index)
	# temp1 = lower_index
	# temp +=arr[mid]
	temp =  higher_index + [arr[mid]] + lower_index
print(temp)

