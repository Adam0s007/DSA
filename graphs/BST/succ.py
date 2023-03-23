class Node:
    def __init__(self, key,parent=None):
        self.left = None
        self.right = None
        self.val = key
        self.parent = parent


def minValue(node):
	current = node
	# loop down to find the leftmost leaf
	while(current.left is not None):
		current = current.left
	return current

def succ_parent(node):
    if node.parent is None: return None
    if node.parent.left == node: return node.parent
    return succ_parent(node.parent)

def succ(curr):
    print(curr.val,end=" -> ")
    if curr.right is not None: return minValue(curr.right)
    return succ_parent(curr)
    
    #1)gdy curr - ma prawe dziecko:
    # idziemy do jego prawego dziecka, a z tego prawego szukamy najbardziej po lewo wysunietego liscia! (minimum dla tego Nodea)

    #2) gdy curr - nie ma prawego dziecka:
    # idziemy do gory od tego liscia na lewo caly czas dopoki nie napotkamy parenta bedacego na prawo od ostatniego nodea bedacego po lewo
    

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

print(succ(root).val)
print(succ(root.left).val)
print(succ(root.right).val)
print(succ(root.left.left).val)
print(succ(root.left.right).val)
print(succ(root.left.left.left).val)
print(succ(root.right.right))
print(succ(root.right.left).val)
print(succ(root.right.left.left).val)
print(succ(root.right.left.right).val)
print(succ(root.right.left.right.right).val)
