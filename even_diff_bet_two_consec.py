

def even_diff(arr):
	count =0
	pre = []
	for i in range(1,len(arr)-1):

		# if abs(arr[i] - arr[i+1]) & 1 ==1 :
		# 	pre.append(arr[i+1])
		# 	print(pre)
		# 	if pre[0] == arr[i]:
		# 		count +=1
		# 	elif pre[0] !=arr[i]:
		# 		count +=1
		# 	pre.pop(0)

		if abs(arr[i-1]-arr[i])&1 and abs(arr[i]-arr[i+1])&1:
			count +=1
			continue
		else:
			count +=1



	return count

arr = [2,4,3,6,8,5,3]

res = even_diff(arr)

print(res)