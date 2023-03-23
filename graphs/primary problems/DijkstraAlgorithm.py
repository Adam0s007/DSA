from queue import PriorityQueue

"""
Lista sąsiedztwa z wagami:
G = [[], [], ...],
G[i] = [(u1, wi), (u2, w2), ...]   <-> i-ty wierzchołek ma krawędź do wierzchołka u1 z wagą w1, ...
"""
A=[(0, 1, 4),(0, 7, 8 ),(1, 2, 8 ),(1, 7, 11),(2, 3, 7),(2, 8, 2),(2, 5, 4),(3, 4, 9),(3, 5, 14),(4, 5, 10),(5, 6, 2),(6, 7, 1),(6, 8, 6),(7, 8, 7)]

graph = [[] for i in range(15)]
for x in A:
    graph[x[0]].append([x[1],x[2]])


def dijkstra(G, s):
    n = len(G)
    distance = [float("inf") for _ in range(n)]  # tablica odległości od {s}
    parent = [-1 for _ in range(n)]  # tablica 'rodziców'
    queue = PriorityQueue()
    queue.put((0, s))
    distance[s] = 0
    #parent[s] = s
    visited = [False for _ in range(n)]  # tablica wskazująca czy dany wierzchołek został już przetworzony 
    while not queue.empty():
        value, current = queue.get() #value not used
        #print(queue.qsize())
        if not visited[current]:
            visited[current] = True
            for v, w in G[current]:
                if distance[current] + w < distance[v]: #relaxation
                    distance[v] = distance[current] + w
                    parent[v] = current
                    queue.put((distance[v], v))
    print(distance)
dijkstra(graph,0)
G = [[(1,2),(2,4)],[(3,7),(2,1)],[(4,3)],[(5,1)],[(5,5),(3,2)],[]] #edge,weight
G = [[[1,28],[5,10]],[[0,28],[6,14],[2,16]],[[1,16],[3,12]],[[2,12],[6,18],[4,22]],[[5,25],[6,24],[3,22]],[[4,25],[0,10]],[[1,14],[4,24],[3,18]]]
dijkstra(G,0)
