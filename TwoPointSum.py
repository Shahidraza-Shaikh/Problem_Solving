
def twoSum(nums,k):
	i =0 
	j = len(nums) -1

	while i <j:

		x = nums[i] + nums[j]

		if x < k:

			i+=1

		elif x > k:
			 j-=1
		else:

			return i,j

arr = [3,1,2,4,-3,1]
k = 0
res = twoSum(arr,k)
print(res)