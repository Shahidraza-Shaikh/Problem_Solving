
class Node:

	def __init__(self,data):

		self.data= data
		self.left = None
		self.right = None


root = Node(1)

root.left = Node(1)
root.right = Node(1)

root.left.left = Node(1)
root.left.right = Node(1)

root.right.right = Node(0)



def IsUnivalued(root,unival):

	if root == None:

		return True
	print(root.data,unival)
	if root.data != unival:
		print("False")

		return False


	# if root.left != None:
	# if root
	return IsUnivalued(root.left,unival) and IsUnivalued(root.right,unival)

	# # if root.right != None :

	# rightNode = 
	# return leftNode and rightNode

print(IsUnivalued(root,root.data))

