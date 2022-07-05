

def combination(idx,arr,target,comb,ans):

	if target == 0:
		ans.add(tuple(comb))
		return 

	for i in range(idx,len(arr)):

		if i >idx and arr[i] == arr[i-1]: continue

		if arr[i] > target : break
		comb.append(arr[i])
		combination(i+1,arr,target- arr[i],comb,ans)