
from typing import Optional





class BSTNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None




def find(root, key):
    while root != None:

        if root.key == key:
            return root
        
        elif root.key > key:
            root = root.left
        
        else:
            root = root.right

    return None




def insert(root, to_insert): #to_insert - element do wstawienia, root - korzeń drzewa
    x=None

    #znalezienie miejsca do wstawienia
    while root != None:
        x = root
        if to_insert.key < root.key:
            root = root.left
        else:
            root = root.right
    to_insert.parent = x  #x to rodzic mojego elementu, który muszę wstawić

    #wstawianie
    if x is None:
        root = to_insert
    elif x.key > to_insert.key:
        x.left = to_insert
    else:
        x.right = to_insert




def find_minimum(root):
    while root.left != None:
        root=root.left
    return root

def find_maximum(root):
    while root.right != None:
        root = root.right
    return root





def transplant(root, u, v): # zastępowanie drzewa o korzeniu u poddrzewem o korzeniu v. Ojciec u staje się ojcem v, a v zostaje synem ojca u
    if u.parent == None:
        root = v
    
    elif u==u.parent.left: # jeśli u jest lewym dzieckiem
        u.parent.left = v #v staje się dzieckiem
    else:
        u.parent.right = v
    
    if v: #aktualizuję rodzica v
        v.parent = u.parent

def delete_element(root, to_delete):
    if to_delete.left == None: #jeśli nie ma lewego dziecka
        transplant(root, to_delete, to_delete.right)

    elif to_delete.right == None: #jeśli nie ma prawego dziecka
        transplant(root, to_delete, to_delete.left)
    else:
        to_swap = find_minimum(to_delete.right) #znajduję następnik usuwanego węzła i go będę wstawiać na miejsce usuniętego

        if to_swap.parent != to_delete: #jeśli to_swap nie jest prawym synem to_delete, to zastępujemy to_swap
            transplant(root, to_swap, to_swap.right) #wszystko co bylo pod to_swap ( mozliwosc tylko z jego prawej strony), zostaje ZAKTUALIZOWANE
            #teraz jego pierwsze prawe dziecko wchodzi na miejsce to_swap
            #teraz to_swap powoli wchodzi na miejsce to_delete. Aktualizujemy jego prawe dziecko, ma byc takie samo jak to_delete
            #oraz aktualizujemy parenta prawego dziecka to_delete
            to_swap.right = to_delete.right 
            to_swap.right.parent = to_swap

        transplant(root, to_delete, to_swap) #zastepujemy juz jawnie to_delete, to_swap'em
        #ponieważ to_swap albo zawiera prawe poddrzewo takie samo jak to_delete, to teraz aktualizujemy jego lewą część analogicznie
        # jak bylo w ifie wyżej
        to_swap.left = to_delete.left
        to_swap.left.parent = to_swap



def successor(x): #następnik
    if x.right != None:
        return find_minimum(x.right)

    y = x.parent
    while y != None and x == y.right: #dopóki rodzic nie jest Nonem i x jest cały czas prawym dzieckiem, idę w górę drzewka
        x = x.parent
        y = y.parent #x.parent.parent
    return y


def predecessor(x): #poprzednik
    if x.left != None:
        return find_maximum(x.left)
    
    y=x.parent
    while y != None and x == y.left:
        x = x.parent
        y = y.parent
    return y



root = BSTNode(10)
print(root.key)

first_kid = root.left = BSTNode(5)
first_kid.parent = root
print(first_kid.key)

second_kid = root.right = BSTNode(15)
second_kid.parent = root
print(second_kid.key)

a = first_kid.left = BSTNode(1)
a.parent = first_kid
print(a.key)

b = second_kid.right = BSTNode(20)
b.parent = second_kid
print(b.key)

c = second_kid.left = BSTNode(12)
c.parent = second_kid
print(c.key)

print("---------------------------")
print(b.parent.key)
print(b.parent.right.key)
print(find(root, 1))

to_insert1 = BSTNode(6)
insert(root, to_insert1)
print(to_insert1.parent.key)

to_insert2 = BSTNode(2)
insert(root, to_insert2)
print(to_insert2.parent.key)

to_delete = second_kid
delete_element(root, to_delete)
print(root.right.key, root.right.right.key, root.right.left.key)

print(successor(root).key)
print(predecessor(b).key)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Find the min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val  = cur.val
            root.right = self.deleteNode(root.right,root.val)
        return root




            

            

