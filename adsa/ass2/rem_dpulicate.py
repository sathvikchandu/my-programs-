class newNode:
	def __init__(self, data):
		self.unique = data
		self.cnt = 1
		self.l = None
		self.r = None
def in_order(root):
    if root != None:
        in_order(root.l)
        print(root.unique)
        in_order(root.r)

def pre_order(root):
    if root != None:
        print(root.unique)
        pre_order(root.l)
        pre_order(root.r)

def post_order(root):
    if root != None:
        post_order(root.l)
        post_order(root.r)
        print(root.unique)

def addval(node, unique):
    if node == None:
        k = newNode(unique)
        return k
    if unique == node.unique:
        (node.cnt) += 1
        return node
    if unique < node.unique:
        node.l = addval(node.l, unique)
    else:
        node.r = addval(node.r, unique)
    return node
def minValueNode(node):
    current = node
    while current.l != None:
        current = current.l
    return current
root = None
root = addval(root, 20)
root = addval(root, 123)
root = addval(root, 3244)
root = addval(root, 123)
root = addval(root, 1231)
print("no dupliactes are added")
print()
print('in_order traversal of the given tree')
print(in_order(root))
print()

print('pre_order traversal of the given tree')
print(pre_order(root))
print()

print('post_order traversal of the given tree')
print(post_order(root))
