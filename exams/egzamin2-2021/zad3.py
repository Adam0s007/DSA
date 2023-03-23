from zad3testy import runtests
# Dane są lampki o numerach od 0 do n-1. Każda z nich może świecić na zielono, czerwono lub niebiesko
# i ma jeden przełącznik, który zmienia jej kolor ( z zielonego na czerwony, 
# z czerwonego na niebieski i z niebieskiego na zielony). Początkowo wszystkie lampki świecą 
# na zielono. Operacja (a,b) oznacza "wciśnięcie przełącznika na każdej z lampek o numerach od a do b".
# Wykonanych będzie m operacji. Proszę napisać funkcję:
# def lamps(n,L)
# która mając daną liczbę n lampek oraz listę L operacji (wykonywanych w podanej kolejności) zwraca
# ile maksymalnie lampek świeciło się na niebiesko (lampki są liczone na początku i po wykonaniu
# każdej operacji).

#rozwiazanie:
#tworzymy drzewa przedzialowe!
#postac drzewa:
# zawiera Node'y o wartosciach: 
# a - lewy koniec przedzialu, 
# b - prawy koniec przedzialu
# f - wartosc 0,1,2 ozn kolor 0 -> 1 -> 2 -> 0 -> ... zielony -> czerwony -> nieb -> zielony... 

# [0,15] f=0 - poczatek drzewa

#dodajemy operacje np [0,6]:

#  [0,15] f=0
#  /  \
# /    \
#[0,6] [7,15]
# f=1    f=0 

#dodajemy operacje np [3,8]

    #         [0,15] f=0
    #         /  \
    #        /    \
    #      [0,6]  [7,15]
    #       f=1     f=0 
    #      /  \       / \
    #     /    \     /   \
    #   [0,2] [3,6][7,8] [9,15]
    #    f=1   f=2   f=1  f=0

#dodajemy operację np [1,3]
    #         [0,15] f=0
    #         /  \
    #        /    \
    #      [0,6]  [7,15]
    #       f=1     f=0 
    #      /  \       / \
    #     /    \     /   \
    #   [0,2] [3,6][7,8] [9,15]
    #    f=1   f=2   f=1  f=0
    #   / \      \ \
    #  /   \      \ [4,6] f=2
    #[0,0] [1,2]   [3,3]
    # f=1   f=2     f=0
    #    ... gdy wstawimy przedzial [0,1] to wtedy przedzialy ktore nie zostaly zmodyfikowane muszą zostac powielone!

# powyzej zostala przedstawiona funkcja dfs

#niestety nasza funkcja za kazdym razem wywolywana bedzie miala coraz wiekszą wysokość, ale mozna to latwo obejsc
# jedyne do czego musimy sie dostać, to ostatnie elementy czyli liscie
#zalozmy ze root to nasz dziadek, ktory poczatkowo nie ma dzieci. Pierwsze wywolanie dfsa sprawi ze pojawi sie kolejny poziom
# w drzewie (1. operacja).
# idac od drugiego wywolania tworzymy wnuków wzgledem roota. Zapisujemy to w nowej tablicy heirs (dziedzice).
# krokiem kolejnym jest zamiana rodziców z wnukami, czyli teraz dziadek root oddaje do adopcji swoje dzieci 
# a jego wnuki stają się dla niego jak dzieci xD. Gdy wykonujemy te operacje, to od razu dfsem zwracamy ilosc lampek z val ==2.
# moze dojsc do sytuacji, ze dzieci roota przyjmą postać przedziałów [1,1],[2,2],[3,3] itd.. wiec aby temu w pewnym
# stopniu zapobiec, scalami dzieci, ktore mają to samo światełko wlaczone i są obok siebie czyli node1.a +1 == node2.b
#algorytm przechodzi 10 testow O(n+T) gdzie T to dlugosc tablicy max(len(dzieci),len(wnuki)) roota
from collections import deque
class Node:
    def __init__(self,a,b,c):
        self.a = a
        self.b =b
        self.tab = []
        self.val = c

def lamps(n,T):
    root = Node(0,n-1,0)
    heirs = []
    #mając roota i jego dzieci, dodajemy wnuki do tablicy heirs
    # pozniej wnuki roota stają się jego dziecmi
    #mamy tutaj stałą wysokość drzewa wynoszącą 2!
    def dfs(root,a,b):#(logn)
        if not root.tab:  #nasz tak zwany lisc
            new_value = (root.val+1)%3
            blues = 0
            if a == root.a and b == root.b: 
                heirs.append(Node(a,b,new_value))
                if new_value == 2: blues+= (b-a+1)
            elif a == root.a and b != root.b:
                heirs.append(Node(a,b,new_value))
                
                heirs.append(Node(b+1,root.b,root.val)) 
                if new_value == 2: blues += (b-a+1)
                elif root.val == 2: blues +=(root.b-b)
                     
            elif a != root.a and b == root.b: 
                heirs.append(Node(root.a,a-1,root.val))
                heirs.append(Node(a,b,new_value)) 
                if new_value == 2: blues += (b-a+1)
                elif root.val == 2: blues +=(a-root.a)         
            else:
                heirs.append(Node(root.a,a-1,root.val))
                heirs.append(Node(a,b,new_value))
                heirs.append(Node(b+1,root.b,root.val))    
                if new_value == 2: blues += (b-a+1)
                elif root.val == 2: blues += ((a-root.a) + (root.b - b))                          
            return blues
        else:
            values = 0
            for node in root.tab:
                if node.a <= a <= node.b and node.a <= b <= node.b:
                    values += dfs(node,a,b)
                elif node.a > a and node.b < b:
                    values += dfs(node,node.a,node.b)
                elif node.a <= a <= node.b:
                    values += dfs(node,a,node.b)
                elif node.a <= b <= node.b:
                    values += dfs(node,node.a,b) 
                #a co z innymi wartosciami? tez trzeba je spamietac!
                else:
                    heirs.append(Node(node.a,node.b,node.val))
                    if node.val == 2: values += (node.b - node.a + 1)
        return values
       
    
    maxBlues = 0
    for elem in T:
        maxBlues = max(maxBlues,dfs(root,elem[0],elem[1]))
        root.tab = []
        root.tab = heirs
        heirs = [root.tab[0]]
        # print("root.tab: ")
        
        # print("[",heirs[0].a,",",heirs[0].b,"],val=",heirs[0].val,"-",end=" ")
        for node in root.tab[1:]:
            # print("[",node.a,",",node.b,"],val=",node.val,"-",end=" ")
            if node.a == heirs[-1].b + 1 and node.val == heirs[-1].val: heirs[-1].b = node.b
            else: heirs.append(node)
        # print()
        # print("heir nodes: ")
        # for node in heirs:
        #     print("[",node.a,",",node.b,"],val=",node.val,"-",end=" ")
        # print()
        
        # print("------")
        root.tab = heirs
        heirs = []
    return maxBlues
runtests( lamps )
# T = [(0, 4), (2, 6), (1, 6), (2, 5), (7, 9), (1, 7), (1, 7), (1, 7)]
# n = 10
# print(lamps(n,T))
