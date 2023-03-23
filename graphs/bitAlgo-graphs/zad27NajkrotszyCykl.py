# Dany jest graf ważony z dodatnimi wagami. Należy podać algorytm, ktory zwróci długość
# najkrótszego cyklu w grafie. Należy podać rozwiązania dla grafów rzadkich i gęstych. 
# Algorytm powinien stwierdzić, jeśli graf nie ma cyklu.

#rozw:
#możnaby usuwac po kolei krawędzie z grafu i dla kazdego takiego usuniecia robic dijkstre

#albo zrobic tak jak ja:
#znalezc cykliczne wierzcholki
# dla kazdej z nich robic dijkstre, ale zmodyfikowaną:
# jesli dziecko u, ozn. jako v, zostalo juz przetworzone,
# tzn jego visited == True (wiec ma juz minimalną odleglosc), 
# to wtedy zwracamy dist[u] + w + dist[v] gdzie w to waga krawedzi miedzy u i v

from queue import PriorityQueue

def dijkstra_to_one_point(G,s): #dziala tylko dla wierzcholkow bedących w cyklu!
    visited = [False for i in range(len(G))]
    parent = [-1 for i in range(len(G))]
    dist = [float("inf") for i in range(len(G))]
    q = PriorityQueue()
    dist[s] = 0
    q.put((0,s))    
    flag = 1
    while not q.empty():
        cost,u = q.get()
        visited[u] = True 
        for v,w in G[u]: 
            if not visited[v]:
                if dist[u] + w < dist[v] or dist[v] == 0: #dist[v] == 0 tylko gdy jest to wierzch startowy
                    parent[v] = u
                    dist[v] = dist[u] + w 
                    q.put((dist[v],v))
            elif parent[u] != v: #jesli znajdziemy pierwszy cykl to ozn ze jest najkrotszy! pole visited ozn ze wierzcholki zostaly przetworzone!
                return dist[v] + w + dist[u]
    return float("inf")


def najkrotszy_cykl(G):
    visited = [False for i in range(len(G))]
    parent = [-1 for i in range(len(G))]
    dist = [float("inf") for i in range(len(G))]
    q = PriorityQueue()
    cycled = [False for i in range(len(G))]

    #wykonujemy dfs'a by sprawdzic punkty cykliczne
    def dfs(u):
        visited[u] = True
        nr_of_edges = len(G[u])
        for v,w in G[u]:
            if visited[v] == False:
                nr_of_edges -=1
                parent[v] = u
                dfs(v)
            elif parent[u] != v:
                cycled[v] = True
    
    for u in range(len(G)):
        if not visited[u]:
            dfs(u) 
    
    minim = float("inf")
    for u in range(len(cycled)):
        if cycled[u]:
            minim = min(minim,dijkstra_to_one_point(G,u))
    return minim
    


    print(cycled)            


G = [[(4,3),(1,2)],
[(0,2),(2,4)],
[(1,4),(3,3),(10,3)],
[(4,1),(2,3),(7,2)],
[(3,1),(0,3),(5,5)],
[(4,5),(6,2)],
[(5,2),(7,1)],
[(6,1),(3,2),(9,3),(8,1)],
[(7,1)],
[(7,3),(10,1)],
[(9,1),(2,3)]]

print(najkrotszy_cykl(G))
