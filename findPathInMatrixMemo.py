

def findPath(row,col,dictionary={}):
	if (row,col) in dictionary:
		return dictionary[(row,col)]
	if row ==0 or col ==0:
		return 1

	dictionary[(row,col)]	 = findPath(row-1,col,dictionary) + findPath(row,col-1,dictionary)
	return dictionary[row,col]
print(findPath(20,20))