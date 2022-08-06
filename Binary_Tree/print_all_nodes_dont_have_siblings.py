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


def Dont_have_sib(root,res):

	if root == None:
		return

	if root.left == None and root.right == None:

		return

	if root.left != None and root.right != None:

		Dont_have_sib(root.left,res)
		Dont_have_sib(root.right,res)

	if root.left != None :
		res.append(root.left.data)
		Dont_have_sib(root.left,res)

	if root.right != None :

		# print(root.right.data)
		Dont_have_sib(root.right,res)

res = []
Dont_have_sib(root1,res)

print(res)
