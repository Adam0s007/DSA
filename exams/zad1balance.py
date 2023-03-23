# Dane jest drzewo T zawierające n wierzchołków. Każda krawędź e drzewa 
# ma wagę w(e) e N oraz unikalny indentyfikator id(e) e N. Wagą drzewa jest suma 
# wag jego krawędzi. Proszę napisać funkcję: def balance(T), ktora 
# zwraca identyfikator takiej krawędzi e drzewa, że usunięcie e dzieli drzewo na takie dwa, 
# których różnica wag jest minimalna. Proszę oszacować złożoność czasową i pamięciową użytego algorytmu.
from zad1testy import runtests

#uwaga w poleceniu mamy podanego roota! wiec git
# class Node:
#     def __init__(self): #stwórz węzeł drzewa
#         self.edges = [] # lista węzłów do których są krawędzie
#         self.weights = [] #lista wag krawędzi
#         self.ids = []  # lista identyfikatorów krawędzi

#     def addEdge(self,x,w,id): #dodaj krawędz z tego węzła do węzła "x" 
#         self.edges.append(x) # o wadze "w" i identyfikatorze "id"
#         self.weights.append(w)
#         self.ids.append(id)
#mamy do czynienia z drzewem!
# 

def balance(T):
    #pole visited jest zbedne, ponieważ nigdy nie osiągniemy cykli, drzewa są acykliczne
    distances = {}
    # u - to u nas Node ktorym jest poczatkowo T
    def dfs(u):#inny sposob na liczenie wszystkich wag (w drzewie tylko dziala)
        for i in range(len(u.edges)):
            distances[u] = distances.get(u,0) + (u.weights[i] + dfs(u.edges[i]))
        return distances.get(u,0)
    S = 0
    
    
    dfs(T) # T to nasz root! (podane w poleceniu)
    for key,val in distances.items():
        S = max(S,val)
    

    best_id = [0]
    minim_roznica = [float("inf")]
    def dfs2(u):
        for i in range(len(u.edges)):
                #SB -> suma dystansow w zakorzenionym fragmencie (odrebny zbior!)
                #S - SB - w -> drugi podzbiór wierzchołków!
                #roznica: abs(S - SB - w - SB) = abs(S - 2SB - w)
            roznica = abs(S - 2*distances.get(u.edges[i],0) - u.weights[i])
            if minim_roznica[0] > roznica:
                    #print(u,v,roznica)
                minim_roznica[0] = roznica
                best_id[0] = u.ids[i]
            dfs2(u.edges[i])
    dfs2(T)
    return best_id[0]


runtests( balance )
