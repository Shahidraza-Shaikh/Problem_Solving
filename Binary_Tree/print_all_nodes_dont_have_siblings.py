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


def Dont_have_sib(root):

	if root == None:
		return

	if root.left == None and root.right == None:

		return

	if root.left != None :

		Dont_have_sib(root.left)

	if root.right != None :

		Dont_have_sib(root.right)