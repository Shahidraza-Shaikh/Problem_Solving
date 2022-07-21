class Node:

	def __init__(self,data):

		self.left = None
		self.right = None
		self.data = data



root = Node(10)
root.left = Node(20)

root.right = Node(25)

root.left.left = Node(30)
root.left.right = Node(40)

root.right.left = Node(35)
root.right.right = Node(33)


# Pre-Order Traversal 

def preOrder(root,ans):

	if root == None:
		return 

	ans.append(root.data)

	preOrder(root.left,ans)
	preOrder(root.right,ans)

ans = []
preOrder(root,ans)
print(ans)
