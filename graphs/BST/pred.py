class Node:
    def __init__(self, key,parent=None):
        self.left = None
        self.right = None
        self.val = key
        self.parent = parent


def maxValue(node):
	current = node
	# loop down to find the leftmost leaf
	while(current.right is not None):
		current = current.right
	return current

def pred_parent(node):
    if node.parent is None: return None
    if node.parent.right == node: return node.parent
    return pred_parent(node.parent)

def pred(curr):
    print(curr.val,end=" -> ")
    if curr.left is not None: return maxValue(curr.left)
    return pred_parent(curr)


root = Node(7)
root.left = Node(4,root)
root.right = Node(12,root)
root.left.left = Node(2,root.left)
root.left.right = Node(6,root.left)
root.left.left.left = Node(1,root.left.left) 

root.right.right = Node(13,root.right)
root.right.left = Node(9,root.right)
root.right.left.left = Node(8,root.right.left)
root.right.left.right = Node(10,root.right.left)
root.right.left.right.right = Node(11,root.right.left.right)

print(pred(root).val)
print(pred(root.left).val)
print(pred(root.right).val)
print(pred(root.left.left).val)
print(pred(root.left.right).val)
print(pred(root.left.left.left))
print(pred(root.right.right).val)
print(pred(root.right.left).val)
print(pred(root.right.left.left).val)
print(pred(root.right.left.right).val)
print(pred(root.right.left.right.right).val)
