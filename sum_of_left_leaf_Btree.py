
class Node:

	def __init__(self,data):

		self.data  = data
		self.left = None
		self.right =None


root = Node(10)

root.left = Node(4)
root.right = Node(2)
root.left.left = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.left.right.left = Node(5)
root.right.left = Node(4)

current_Sum =[0]

# Reccursive method

def sum_of_left_leaf(root,current_Sum,is_leaf):
	if root is None:
		return 

	if root.left == None and root.right == None and is_leaf:

		current_Sum[0] += root.data
		# print(root.data)
		# return current_Sum	
	# print(current_Sum)
	sum_of_left_leaf(root.left,current_Sum,True)
	sum_of_left_leaf(root.right,current_Sum,False)
	# return current_Sum

sum_of_left_leaf(root,current_Sum,False)
print(current_Sum[0])


# Iterative method 

# def leaf_leaf_sum(root):

# 	stack = []
# 	stack.append(root)

# 	summ = 0

# 	while len(stack) > 0:

# 		new_node = stack.pop()

# 		if new_node.left.left == None and new_node.right == None:

# 			summ = 0

