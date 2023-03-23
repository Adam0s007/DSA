class Node:
    def __init__(self, key,parent=None):
        self.left = None
        self.right = None
        self.val = key
        self.parent = parent


def transplant(root, u, v): # zastępowanie drzewa o korzeniu u poddrzewem o korzeniu v. Ojciec u staje się ojcem v, a v zostaje synem ojca u
    if u.parent == None:
        root = v
    elif u==u.parent.left: # jeśli u jest lewym dzieckiem
        u.parent.left = v #v staje się dzieckiem
    else:
        u.parent.right = v
    
    if v != None: #aktualizuję rodzica v
        v.parent = u.parent