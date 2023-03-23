class Node:
    def __init__(self,key,parent):
        self.key = key
        self.parent = parent
        self.left = None 
        self.right = None


def minValueNode(node):
	current = node
	# loop down to find the leftmost leaf
	while(current.left is not None):
		current = current.left
	return current

def maxValueNode(node):
	current = node
	# loop down to find the leftmost leaf
	while(current.right is not None):
		current = current.right
	return current

