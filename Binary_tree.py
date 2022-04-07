
class Node:

	def __init__(self,data):

		self.data  = data
		self.left = None
		self.right =None


root = Node(10)

root.left = Node(4)
root.right = Node(4)
root.left.lrft = Node(2)
root.left.right = Node(5)


print(root.left.data)