
class Node:

	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None


root = Node(1)

root.left = Node(1)

root.right = Node(1)

root.left.right = Node(1)
root.left.left = Node(5)


def univalued_Btree(root,val):

	if root is None:
		return True
	if root.data != val:
		return False
	left = univalued_Btree(root.left,val)
	right = univalued_Btree(root.right,val)

	return left and right

print(univalued_Btree(root,root.data))

