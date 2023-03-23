from zad2testy import runtests

# Dane jest drzewo BST zbudowane z węzłów: 

# class BNode:
#     def __init__(self,value):
#         self.left = None
#         self.right = None 
#         self.parent = None 
#         self.value = value
# Klucze w tym drzewie znajdują się w polach value i są liczbami całkowitymi.
# Mogą zatem mieć wartości zarówno dodatnie, jak i ujemne. Proszę napisać funkcję, która 
# zwraca wartość będącą minimalną możliwą sumą kluczy zbioru wierzchołków oddzielających wszystkie liście
# od korzenia w taki sposób, że na każdej ścieżce od korzenia do liścia znajduje się
# dokładnie jeden wierzchołek z tego zbioru. Zakładamy że korzeń danego drzewa nie jest 
# bezpośrednio połączony z żadnym liściem (ścieżka od korzenia do każdego liścia prowadzi
# przez przynajmniej jeden dodatkowy węzeł). Jako liść jest rozumiany węzeł W typu BNode taki, że W.left = W.right = None

# Rozwiązanie należy zaimplementować w postaci funkcji:
# def cutthetree(T):
#     ...
# która przyjmuje korzeń danego drzewa BST i zwraca wartość rozwiązania.
# Nie wolno zmieniać definicji class BNode

class BNode:
    def __init__(self,value):
        self.left = None
        self.right = None 
        self.parent = None 
        self.value = value


def isLisc(node):
    return (not node.right and not node.left)

def cutthetree(T):
    def dfs(root):          #1)                                  #2)
        if (root.left and isLisc(root.left)) or (root.right and isLisc(root.right)): #ostatnia mozliwa wartosc dla 1) root.left lub 2) root.right
            return root.value
        
        res = root.value 
        #trzeba sprawdzac gdzie jestesmy w stanie dojsc
        if not root.left and root.right: 
            res = min(res, dfs(root.right))
        elif not root.right and root.left:
            res = min(res, dfs(root.left))
        else:
            res = min(res, dfs(root.left) + dfs(root.right))
        return res
    ans = dfs(T.left) + dfs(T.right) #nie mozemy zaczac od roota! jesli suma wartosci ponizej roota bedzie wieksza od root.value to zwroci root.value a to blad
    return ans

# root = BNode(0)
# root.left = BNode(5)
# root.left.left = BNode(-3)
# root.left.right = BNode(-1)


# root.left.left.left = BNode(0)
# root.left.left.right = BNode(0)


# root.left.right.left = BNode(0)
# root.left.right.right = BNode(0)

# root.right = BNode(2)
# root.right.left = BNode(-1)
# root.right.right = BNode(4)
# root.right.left.left = BNode(6)

# root.right.left.left.left = BNode(0)
# root.right.left.left.right = BNode(0)

# root.right.right.left = BNode(0)
# root.right.right.right = BNode(0)

# print(cutthetree(root))


runtests(cutthetree)
