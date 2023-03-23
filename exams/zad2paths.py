# Dany jest nieskierowany graf G = (V,E) oraz dwa wierzchołki s i t. Proszę zaimplementować    
# funkcję: 
# def paths(G,s,t): ... 
# która zwraca liczbę krawędzi e takich, że e występuje na pewnej najkrótszej ścieżce z s do t.
# Graf dany jest jako lista sąsiedztwa postaci [(v0,w0),(v1,w1),...] gdzie vi to nr wierzcholka,
# wi to waga krawedzi prowadzącej do wierzchołka vi. Wagi krawędzi są dodatnie.
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
# użytego algorytmu.

#rozwiazanie:
# robimy dwie dijkstry i dwie tablice zwiazane z odleglosciami (jedno powiazane z minim odl z s a druga z t)
# jesli wierzcholek lezy na najkrotszej sciezce, to:
# 1) dist1[u] + dist2[u] == dist1[t] zalozenie: dist1 to odleglosci minimalne do t z wierzcholka s

# jesli krawedz lezy na najkrotszej sciezce, to:
# zachodzi warunek 1) dla jego dwóch wierzchołków ( te sumy są równe)
# 2) dist1[u] + w == dist1[v] zakladajac ze dist1 to odleglosci minimalne do t z wierzcholka s 
# oraz w to waga krawedzi (oznacza to ze krawedz zostala wykorzystana)
# widzimy ze krawedz nalezaca do najkrotszej sciezki to taka, w ktorej jej waga zostala wykorzystana do
# obliczania najkrotszych odleglosci!

#dodatkowa korzysc: zaleznie od implementacji dfsa, mozemy liczyc counterem dwukrotnie poprawne krawedzie, ale
# warunek 2) zapobiega dublowaniu
from queue import PriorityQueue
def paths(G,s,t):
    """tu prosze wpisac wlasna implementacje"""
    def dijkstra(G,s,t):
        dist = [float("inf") for i in range(len(G))]
        visited = [False for i in range(len(G))]
        q = PriorityQueue()
        parent = [-1 for i in range(len(G))]
        q.put((0,s))
        dist[s] = 0
        while not q.empty():
            cost,u = q.get()
            if visited[u]: continue
            for v,w in G[u]: 
                if visited[v]: continue
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    q.put((dist[v],v))
        return dist
    dist1 = dijkstra(G,s,t)
    dist2 = dijkstra(G,t,s) 
    #mamy odleglosci z obydwoch miejsc!
    #teraz robimy zwyklego dfsa!
    if dist1[t] == float("inf") or dist2[s] == float("inf"): return 0 
    # print(dist1)
    # print(dist2)
    visited = [False for i in range(len(G))]
    counter = [0]
    #visited[s] = True
    def dfs(G,u):
        visited[u] = True
        for v,w in G[u]:  
            sumV = dist1[v] + dist2[v]
            sumU = dist1[u] + dist2[u]
            odl = dist1[t]
            if sumV == sumU == odl and \
            (dist1[u] + w == dist1[v]) and \
            (dist2[v] + w == dist2[u]):
                counter[0] +=1
            if visited[v]: continue
            dfs(G,v)        
    dfs(G,s)
    return counter[0]
        


    



G = [[(1,3),(2,2),(3,1)],[(0,3),(2,3),(7,4)],[(0,2),(1,3),(6,4)],[(0,1),(4,1)],[(3,1),(5,1)],[(6,4),(4,1),(10,8)],
[(2,4),(7,4),(9,2),(5,4)],[(1,4),(6,4),(8,4)],[(7,4),(10,4)],[(6,2),(10,3)],[(8,4),(9,3),(5,8)]]
s = 0
t = 10
print(paths(G,s,t))