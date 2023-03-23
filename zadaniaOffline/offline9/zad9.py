

from zad9testy import runtests
from queue import SimpleQueue


from collections import deque
#bruteforce nieco bo sprawdzamy wszystkie mozliwe pary wierzcholkow ford fulkerson
# jedyna rzecz, ktora nas ratuje to taka ze odpalamy forda fulkersona na liscie sasiedztwa

def bfs(graph, s, t, parent):
    visited = [False]*(len(graph))
    queue = deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for v,w in graph[u].items():
            if visited[v] == False and w > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True
                
    return False

def maxflow(graph,source):
     
    maksim = 0
    for u,v,w in graph:
        maksim = max(maksim,u,v)
    
    visited2 = {}
    maksimValue = 0
    for i in range(maksim+1):
        for j in range(maksim+1):
            if i != j and j != source and i != source and (i,j) not in visited2 and (j,i) not in visited2:
                visited2[(i,j)] = True
                max_flow = 0
                G = [{} for i in range(maksim+2)]
                for u,v,w in graph: #macierz krawedziowa
                        G[u][v] = w
                        G[v][u] = 0
                
                G[i][maksim+1] = float("inf")
                G[maksim+1][i] = 0
                G[j][maksim+1] = float("inf")
                G[maksim+1][j] = 0

                sink = maksim+1
                parent = [-1]*(maksim+2)
                while bfs(G,source, sink, parent) :
                    path_flow = float("Inf")
                    v = sink
                    #znajdowanie najmniejszego przeplywu na danej sciezce
                    while(v !=  source):
                        path_flow = min(path_flow, G[parent[v]][v])
                        v = parent[v]
                    max_flow +=  path_flow
                    v = sink
                    #usuwanie / dodawanie najmniejszego przeplywu miedzy krawedziami na danej sciezce
                    while(v !=  source):
                        u = parent[v]
                        G[u][v] = G[u].get(v) - path_flow
                        G[v][u] = G[v].get(u) + path_flow #residual edge!!! czyli taka odwrotna! pozwala na cofanie sie!
                        v = parent[v]
                maksimValue = max(maksimValue,max_flow)

    return maksimValue




# inf = 10**9
# G = [(0,1,7),(0,3,3),(1,3,4),(1,4,6),(2,0,9),(2,3,7),(2,5,9),
# (3,4,9),(3,6,2),(5,3,3),(5,6,4),(6,4,8)]
# s = 2


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)
