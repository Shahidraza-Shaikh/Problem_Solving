
num = int(input())
k = int(input())
nums = list(range(1,num+1))

result = []

for i in range(num):

	if abs(i-num) > k :

		for j in range(num):

			if abs(i-num) >=k :

				result.append(nums[i:j])
			else:
				break
	else:
		break

print(nums)
print(result)

