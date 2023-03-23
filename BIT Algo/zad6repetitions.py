# Dana jest tablica z n liczbami calkowitymi. Zawiera ona bardzo duzo powtorzen - co wiecej,
# zaledwie O(log(n)) liczb jest unikatowe (reszta to powtorzenia). Napisz algorytm, ktory w czasie
# O(n*log(logn)) posortuje taką tablicę.


#da sie zrobic binary tree, i dodawac nowe rzeczy

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.count = 1

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            root.count+=1
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root,arr):
    if root: 
        inorder(root.left,arr)
        c = root.count
        while c>0:
            arr.append(root.val)
            c-=1
        inorder(root.right,arr)

def inorder1(root):
    if root: 
        inorder1(root.left)
        print(root.val)
        inorder1(root.right)

def binaryTree_sort(tab):
    n = len(tab)
    root = None
    arr  = []
    for i in range(0,n):
        root = insert(root,tab[i])
    inorder(root,arr)
    #print(arr)



from random import randint

T = [randint(0,4) for i in range(100000)]
binaryTree_sort(T)



    
    
    
