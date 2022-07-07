# Questions :- https://leetcode.com/problems/combination-sum/

def combination(idx,arr,target,comb):

	# if len(comb)

	if idx == len(arr):

		if target==0:

			print(comb)
			# return

		# print("not pick")
		return

	if target>=arr[idx] :

		comb.append(arr[idx])

		combination(idx,arr,target-arr[idx],comb)

		comb.pop()

	combination(idx+1,arr,target,comb)


arr = [5,1,7]
target = 18
comb = [ ]
combination(0,arr,target,comb)
