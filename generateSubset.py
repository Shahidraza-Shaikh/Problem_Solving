arr = [1,2,3]
# [],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]
res = []
x = len(arr)
for i in range(2**x): # 2**x ~= to 1<<x

	print([ arr[j] for j in range(x) if i&(2**j)])


# print(res)