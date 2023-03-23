
from zad1testy import runtests
# Drzewo BST T reprezentowane przez obiekty klasy Node:
# class Node:
#     def __init__(self):
#         self.left = None 
#         self.right = None
#         self.parent = None
#         self.value = None

# Proszę zaimplementować funkcję ConvertTree(T)
# która przekształca drzewo T na drzewo o minimalnej wysokości,
# w którym węzły spełniają warunek:
# największy element na danym poziomie jest mniejszy od najmniejszego elementu
# na kolejnym poziomie. Funkcja zwraca korzeń nowego drzewa. Poziomy numerujemy od korzenia do liści.

# Funkcja powinna być możliwie jak najsszybsza oraz - kryt. drugiego rzędu - używac jak najmniej pamięci.
# (poza pamięcią już wykorzystaną na reprezentację drzewa). Proszę oszacować
# złożoność czasową oraz pamięciową użytego algorytmu.


#rozwiazanie:
#robimy inorder na drzewie
#drzewo bst nie ma takich samych wartosci!
#wykorzystamy tę własność i wiedząc ze kazdy poziom jest potęgą dwójki, bedziemy wyciagać potegi dwojki elementow!

def ConvertTree(p):
    nodes = []
    def inorder(root):
        if not root: return
        inorder(root.right)
        nodes.append(root) #niech bedzie kolejnosc malejaca! potem bedziemy popować elementy!
        inorder(root.left)
    
    inorder(p)

    for node in nodes:
        node.right = None
        node.left = None
        node.parent =None

    #root to zawsze 1 element
    # root ma zawsze max 2 dzieci
    # te dzieci mają max 4 dzieci
    # nastepne mają max 8 dzieci
    # itd.
    if not len(nodes): return None
    p = nodes.pop() #popujemy roota

    iter = 2
    parents = [p]
    while nodes:
        children = []
        for i in range(min(iter,len(nodes))): #nie wiemy ile jest elementow w tablicy nodes bo popujemy
            children.append(nodes.pop())
        #mając tablicę parentow i dzieci musimy teraz dobrze polaczyc je
        iter_p = 0
        if len(children) > 1:
            for i in range(1,len(children),2):
                parents[iter_p].left = children[i-1]
                children[i-1].parent = parents[iter_p]
                parents[iter_p].right = children[i]
                children[i].parent = parents[iter_p]
                iter_p +=1
            if len(children)% 2 == 1:
                parents[iter_p].left = children[-1]
                children[-1].parent = parents[iter_p]
        else:
            parents[iter_p].left = children[0]
            children[0].parent = parents[iter_p]
        iter *=2
        parents = children
    return p


runtests( ConvertTree )