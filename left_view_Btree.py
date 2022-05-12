class Node:
	"""docstring for Node"""
	def __init__(self, data):

		self.data = data
		self.left = None
		self.right = None


root = Node(10)

root.left = Node(5)
root.right = Node(3)

root.right.left = Node(1)
root.right.left.left = Node(8)

hashMap = {0:-1,1:-1,2:-1,3:-1}

def left_View(root,hashMap,level):
	
	if root is None:
		return 

	if hashMap[level] == -1:
		hashMap[level] = root.data

	left_View(root.left,hashMap,level+1)
	left_View(root.right,hashMap,level+1)

left_View(root,hashMap,0)
print(hashMap)