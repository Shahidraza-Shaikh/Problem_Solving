
class Node:

	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None



root = Node(10)

root.left = Node(5)

root.right = Node(4)

root.left.left = Node(3)
root.left.right = Node(2)


def level_order_traversal(root):

	queue = []

	queue.append(root)

	while len(queue) >0 :

		root = queue.pop(0)

		print(root.data,end="-")

		if root.left is not None:
			queue.append(root.left)
		if root.right is not None:
			queue.append(root.right)
			

level_order_traversal(root)