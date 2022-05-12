
n = int(input())


array = list(map(int,input().split(" ")))


minn = min(array)
maxx = max(array)

min_idx = float("-inf")
max_idx = float("-inf")

result = float("inf")

idx= 0

while idx < n :

	if array[idx] ==minn:
		min_idx = idx 

	if array[idx] == maxx :
		max_idx = idx 

	if min_idx !=-99 and max_idx != -99:

		result = min(result,abs(min_idx-max_idx)+1)

	idx +=1

print(result)

