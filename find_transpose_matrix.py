def rev(matrix):
	mat = []
	for i in range(len(matrix[0])):
		temp = []
		for j in range(len(matrix)):
			# print(i,j)
			temp.append(matrix[j][i])
		mat.append(temp)
		temp = []
	return mat

matrix = [[1,2,3],[4,5,6]]

print(rev(matrix))
