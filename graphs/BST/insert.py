
# Python program to demonstrate
# insert operation in binary search tree
 
# A utility class that represents
# an individual node in a BST
 
 
class Node:
    def __init__(self, key,parent=None):
        self.left = None
        self.right = None
        self.val = key
        self.parent = parent
 
# A utility function to insert
# a new node with the given key
 
 
def insert(root, key,parent=None):
    if root is None:
        return Node(key,parent)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key,root)
        else:
            root.left = insert(root.left, key,root)
    return root
 
# A utility function to do inorder tree traversal
 
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 
 
# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
 
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
 
# Print inoder traversal of the BST
inorder(r)

#z dodakowym polem size oznaczajacym rozmiar poddrzewa!
class Node:
    def __init__(self, key,parent=None):
        self.left = None
        self.right = None
        self.val = key
        self.parent = parent
        self.size = 1



def insert(root, key,parent=None):
    if root is None:
        return Node(key,parent)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.size +=1
            root.right = insert(root.right, key,root)
        else:
            root.size +=1
            root.left = insert(root.left, key,root)
    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val,"size: ",root.size)
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val,"size: ",root.size)
 
def preOrder(root):
    if root:
        print(root.val,"size: ",root.size)
        preOrder(root.left)
        preOrder(root.right)
 

# root = None
# root = insert(root,7)
# insert(root,4)
# insert(root,12)
# insert(root,2)
# insert(root,6)
# insert(root,1)
# insert(root,13)
# insert(root,9)
# insert(root,8)
# insert(root,10)
# insert(root,11)

# inOrder(root)
# print("")
# preOrder(root)
# print("")
# postOrder(root)


# root2 = None
# root2 = insert(root2,5)
# insert(root2,4)
# insert(root2,7)
# insert(root2,4.5)
# insert(root2,3)
# insert(root2,1)
# insert(root2,3.5)
# insert(root2,6)
# insert(root2,9)
# insert(root2,8)
# insert(root2,11)
# print()

root3 = None
root3 = insert(root3,8)
insert(root3,3)
insert(root3,2)
insert(root3,5)
insert(root3,1)
insert(root3,0)
insert(root3,9)
insert(root3,10)
insert(root3,11)
insert(root3,12)

