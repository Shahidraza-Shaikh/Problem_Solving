
A = [-1,18,13,18,-2,-16,7,-1,-213,11]

temp = []
temp.append(A[0])

for i in range(1,len(A)):

	if temp[-1] < 0 and A[i]> 0:

		temp.append(A[i])
	elif temp[-1] > 0 and A[i] < 0:

		temp.append(A[i])
	else:

		temp[-1] = max(temp[-1],A[i])

print(sum(temp))

