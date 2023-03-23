# W pewnym kraju trwa wojna domowa. W ramach sabotażu rebelianci chcą uniemożliwić komunikację 
# telegraficzną z miasta A do B. Otrzymujemy listę miast i linii telegraficznych między nimi.
# Linie telegraficzne są kierowane. Każda z linii ma przypisany koszt zniszczenia jej. 
# Chcemy wybrać zbiór połączeń do zniszczenia o łącznym minimalnym koszcie. 
# Interesuje nas nie tylko koszt, ale które konkretne linie telegraficzne mamy zniszczyć.

#rozw:
#stosujemy algorytm edmonda karpa na max flow/ min-cut i nas interesuje to min cut

# po wykonaniu algorytmu max flow / min cut  nie damy rady przejsc juz przez niektore krawedzie, przez ktore
# poczatkowo dalismy rade. Znajdujac takie polaczenia zwracamy je oraz koszt!
from queue import SimpleQueue
def BFS(graph, s, t, parent):
    visited = [False]*(len(graph))
    queue = SimpleQueue()
    queue.put(s)
    visited[s] = True
    while not queue.empty():
        u = queue.get()
        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                queue.put(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == t:
                    return True
    return False
def edmund_karp(graph,source, sink):
    parent = [-1]*(len(graph))
    max_flow = 0
    while BFS(graph,source, sink, parent) :
        path_flow = float("Inf")
        s = sink
        while(s !=  source):
            path_flow = min (path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow +=  path_flow
        v = sink
        while(v !=  source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow #residual edge!!! czyli taka odwrotna! pozwala na cofanie sie!
            v = parent[v]
    #return max_flow


def min_cut(G,A,B):
    #tworzymy macierz sasiedztwa gdzie A = s, a B = t
    maksim = 0
    for i in range(len(G)):
        for x,y in G[i]:
            maksim = max(x,y,maksim)

    Graph = [[0 for i in range(maksim+1)] for j in range(maksim+1)]
    GraphCpy =[[0 for i in range(maksim+1)] for j in range(maksim+1)]

    for i in range(len(G)):
        for v,w in G[i]:
            Graph[i][v] = w
            GraphCpy[i][v] = w 
    edmund_karp(Graph,A,B)
    def bfsEnd(s,t):
        visited = [False]*(len(Graph))
        queue = SimpleQueue()
        queue.put(s)
        visited[s] = True
        ans = []
        cost =0
        while not queue.empty():
            u = queue.get()
            for ind, val in enumerate(Graph[u]):
                if visited[ind] == False and val > 0:
                    queue.put(ind)
                    visited[ind] = True
                    if ind == t:
                        return [],0
                elif visited[ind] == False and val == 0 and GraphCpy[u][ind] != 0:
                    ans.append((u,ind,GraphCpy[u][ind]))
                    cost += GraphCpy[u][ind]
        return ans,cost
        
    return bfsEnd(A,B)

    




G = [[(3,1),(2,5),(1,1)],[(6,2)],[(5,2)],[(4,3),(2,4)],[(5,2),(2,1)],[(7,5)],[(7,6)],[]]

print(min_cut(G,0,7))