
class Node:
	
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None



root = Node(1)

root.left = Node(4)

root.right = Node(3)

root.left.left=Node(8)
root.right = Node(1)


def find_univalue(root,data):
	if root is None:
		return True
	if root.data != data:
		False

	left = find_univalue(root.left,root.data)
	right = find_univalue(root.left,root.data)


	return  left and right

print(find_univalue(root,root.data))


























