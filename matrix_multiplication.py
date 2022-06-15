mat1 = [[1,2],
       [3,4]]

mat2 = [[5,4],
        [6,7],]

res = [[0,0],[0,0]]

# [[17,18],
# [39,40]]

for i in range(len(mat1)):

	for j in range(len(mat1[0])):
		# print(mat1[i][j],mat2[i][j])
		# res[i][j] = mat1[i][j] * mat2[i][j]

		for k in range(len(mat2)):
			res[i][j] += mat1[i][k] * mat2[k][j]

print(res) 

