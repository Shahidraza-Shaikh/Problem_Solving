
class Node:

	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None


root1 = Node(4)

root1.left = Node(9)

root1.right = Node(2)

root1.left.right = Node(6)
root1.left.left = Node(5)

root2 = Node(4)

root2.left = Node(9)

root2.right = Node(2)

root2.left.right = Node(6)
root2.left.left = Node(5)

# root2.right.left = Node(10)
# root2.right.left = Node(15)


nodes1 = []
nodes2 = []

def leafSimilarTree(root,nodes):

	if root is None:
		return

	if root.left ==None and root.right == None:
		nodes.append(root.data)
	if root.left != None:

		leafSimilarTree(root.left,nodes)
	if root.right !=None:
		leafSimilarTree(root.right,nodes)

	return nodes
v1 = leafSimilarTree(root1,nodes1)

v2 = leafSimilarTree(root2,nodes2)

print(v1,v2)