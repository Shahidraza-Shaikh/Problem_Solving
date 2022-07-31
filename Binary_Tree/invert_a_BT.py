class Node:

	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None


root1 = Node(3)

root1.left = Node(5)

root1.right = Node(1)
root1.left.left = Node(6)
root1.left.left.right = Node(1)

root1.left.right = Node(2)
root1.left.right.left = Node(4)


def Invert_BT(root):

	if root != None:
		return root

	root2 = Node(root.data)

	root2.left = Invert_BT(root.left)

	root2.right = Invert_BT(root.right)

	return root2

print(Invert_BT(root1).left.left.data)