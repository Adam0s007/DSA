#Proszę zaimplementować
# a) wstawianie
# b) min/max
# c) succ/pred (poprzednik, nastepnik)
# w drzewie BST


from json import tool


class Node:
    def __init__(self, key, size):
        self.left = None
        self.right = None
        self.key = key
        self.parent = None
        self.size = size




def insert(root, x):
    if root == None:
        return x
    
    while True:
        if root.key == x.key:
            return

        elif x.key > root.key:
            if root.right:
                root=root.right
            else:
                root.right = Node(x)
                x.parent = root
                return
        else:
            if root.left:
                root = root.left
            else:
                root.left = Node(x)
                x.parent = root
                return

def find_maxi(root):
    if root == None:
        return None

    while root != None:
        root = root.right
    return root.key

def find_min(root):
    # if root == None:
    #     return None

    # while root != None:
    #     root = root.left
    # return root

    res = None
    while root != None:
        res = root
        root = root.left
    return res


def nastepnik(root):
    if root.right != None:
        return find_min(root.right)
    while right_child(root):
        root=root.right
    return root.parent


def right_child(node):
    if node.parent == None:
        return False
    return node.parent.right is node






#Mamy drzewo BST, w którym kazdy wezel zawiera rozmiar poddrzewa

    #       (10) 6
    #        /\
    #       /  \
    #   (5)4    (15) 1
    #    /\
    #   /  \ 
    # (1)1   (6)2
    #          \
    #           \
    #            (7)1

# a) znajdź element, który byłby pod indeksem i, gdyby elementy posortować
# b) dla danego węzła znajdź indeks, pod którym by był po posortowaniu    


#b) Jeśli jesteśm prawym dzieckiem, to wszystkie elementy wyzej sa mniejsze od nas, więc będą po lewej stronie po posortowaniu
def left_size(node):
    if node.left:
        return node.left.size
    else:
        return 0

def index(node):
    i=left_size(node)
    while node.parent:
        if node.parent.right == node:
            i+=left_size(node.parent) + 1
        node = node.parent
    return i




# Klocki 
# Obliczyć wysokość. Na kadym klocku znamy kolejność zrzucania


#   |--5-----|  |--4-----|                }
#         |--3-----|        |---6--|      } h=? 
#      |-1---|        |---2----|          }
  
# --|--|--|--|--|--|--|--|--|--|---|-------->
#   0  1  2  3  4  5  6  7  8  9  10


#sprawdzamy tylko wnetrze spadajacego klocka i badamy tylko wysokosc pod tym klockiem. Potem dla końców przedziału dajemy ich maksy
#jeśli są większe nic ten maks pod spadającym klockiem


#początki i końce przedziałow, posortować je i przenumerować
# 1          10**9

#    3     100
#  2   5


# 0 1 2 3  4  5

#tniemy na mniejsze klocuszki i sprawdzamy, jaka jest wysokość w danym przedziale



#n list co najwyzej n-elementowych





#wszystkie punkty.
# bierzemy kolejne klocki, musimy znaleźć dla niego przedział.
# zaczynamy od dołu, kade drzewo wyzej to przedzial,


#   [0,1]    [2,3]
#    / \      /\
#  /    \    /  \
# 0      1   2   3

# dla kazsego przedzialu musimy pamiętać dwie informacje, wysokość najwyzszego fragmentu, za który odpowiada dany węzeł.
# jak spada nowy klocek, musimy wstawiać i powiększać odpowiednio te przedziały




# przechowujemy coś na ksztalt listy - odpozycji 0 do 3 mamy wysokość 1, potem odpozycji 3 do 5 jest 0, potem od 5 do 10 mamy 3, od 10 do 17 2, od 17 do 20 mamy 4.
# wszystko przedziały przechowujemy po kolei w drzewa BST, gdzie początki są naszymi lkuczami wyszukiwania. gdy chcemy zrzucić nowy klocek (np od 2 do 12). MOzemy znaleźc w drzewie BST początek tego, znajdziemy pierwszy przedział, poniewaz
# nachodzi to usuwamy tez przedzial, wedrując następnikiem przechodzimy do konca przedziału wstawianego, usuwając po kolei przedziały i zapamiętujemy maksymalną długość przedziału
#taki rzut z góry na klocki
#kazdy kolcek to element tablicy z trzema elementami - początek, koniec, wysokość