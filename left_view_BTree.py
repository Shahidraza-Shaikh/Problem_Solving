class Node: #Creating Node

	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None


root = Node(10)

root.left = Node(5)
root.right = Node(4)

root.left.left = Node(6)

root.left.left.left = Node(2)
hashmap = {0:-1,1:-1,2:-1,3:-1}

def left_view(root,hashmap,level):

	if root is None :
		return

	if hashmap[level] == -1:
		hashmap[level] = root.data

	left_view(root.left,hashmap,level+1)
	left_view(root.right,hashmap,level+1)

left_view(root,hashmap,0)
print(hashmap)
