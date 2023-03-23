# Dany jest graf ważony G. Ścieżka superfajna, to taka, która jest nie tylko najkrótszą wagowo 
# ścieżką między v i u, ale także ma najmniejszą liczbę krawędzi (inaczej mówiąc szukamy najkrótszych 
# ścieżek w sensie liczby krawędzi wśród najkrótszych ścieżek
#  w sensie wagowym. Podaj algorytm, który dla danego wierzchołka startowego s znajdzie superfajne 
# ścieżki do pozostałych wierzchołków.

#rozw:
# modyfikujemy tylko relaksację, tworzymy tablice podobną do tej w bfs d[] i w niej przechowujemy informacje
# o ilosci krawedzi napotkanych
# w relaksacji priorytetem jest ofc waga, ale jesi wagi są te same to sprawdzamy jeszcze czy d[v] > 1 + d[u]


from queue import PriorityQueue

def traverse_to_s(t,parent):
    while t != -1:
        print(t, end=" , ")
        t = parent[t] 


def modified_dijkstra(G,s):
    parent = [-1 for i in range(len(G))]
    distance = [float("inf") for i in range(len(G))]
    d = [0 for i in range(len(G))]
    visited = [False for i in range(len(G))]
    q = PriorityQueue()
    q.put((0,s))
    distance[s] = 0
    while not q.empty():
        dist, u = q.get()
        if not visited[u]:
            visited[u] = True
            for v,w in G[u]:
                if visited[v]: continue
                if (distance[u] + w < distance[v]) or \
                    (distance[u] + w == distance[v] and d[v] > d[u] + 1):
                    distance[v]  = distance[u] + w
                    parent[v] = u
                    d[v] = 1 + d[u]
                    q.put((distance[v],v))
    for i in range(len(G)-1,0,-1):
        traverse_to_s(i,parent)
        print()
    



G = [[(1,1),(2,2)],[(0,1),(2,3),(3,2)],[(0,2),(1,3),(3,1),(4,3)],[(1,2),(2,1),(4,2),(5,4)],[(2,3),(3,2),(5,1),(6,2)],[(3,4),(4,1),(6,1)],[(4,2),(5,1)]]
modified_dijkstra(G,0)