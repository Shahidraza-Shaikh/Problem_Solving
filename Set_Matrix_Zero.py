


matrix = [[1,1,1],[1,0,1],[1,1,1]]

for i in range(len(matrix)):

	for j in range(len(matrix[0])):

		if matrix[i][j] == 0:

			idx = i-1

			while idx>=0:
				print(idx)

				if matrix[idx][j] != 0:

					matrix[idx][j] = 0
				idx -=1

			idx = i +1

			while idx < len(matrix) :

				if matrix[idx][j] != 0 :
					matrix[idx][j] = 0

				idx +=1

			idx = j-1

			while idx >= j:

				if matrix[i][idx] != 0:
					matrix[i][idx] = 0

				idx -=1

			idx = j+1

			while idx < len(matrix[0]):

				if matrix[i][idx] != 0:

					matrix[i][idx] = 0

				j +=1

print(matrix)


