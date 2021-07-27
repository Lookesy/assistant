class TreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None




tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

#Прямой обход
def pre_order(node):
	if node:
		print(node.value)
		pre_order(node.left)
		pre_order(node.right)

print("Прямой")
pre_order(tree)

#Обратный обход
def post_order(node):
	if node:
		post_order(node.left)
		post_order(node.right)
		print(node.value)

print("Обратный")
post_order(tree)

#Центрированный
def in_order(node):
	if node:
		in_order(node.left)
		print(node.value)
		in_order(node.right)

print("Центрированный")
in_order(tree)