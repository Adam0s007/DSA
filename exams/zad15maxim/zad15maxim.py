
from collections import deque
from zad15testy import runtests
class Node:
    def __init__(self,key):
        self.left = None  
        self.right = None 
        self.parent = None 
        self.key = key 

def maxim(root,X):
    q = deque()
    licznik = 1
    q.append(root)
    ans = {}
    while q:
        m = len(q)
        for i in range(m):
            node = q.popleft()
            ans[licznik] = node 
            licznik+=1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    maksim = -1
    for index in X:
        maksim = max(maksim, ans.get(index,0).key)
    return maksim



# root = Node(5)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(1)
# root.left.right = Node(0)
# root.right.left = Node(8)
# root.right.right = Node(15)

# print(bfs(root,[3,6,4]))

runtests( maxim )