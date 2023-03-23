# Średnicą drzewa nazywamy odległość między jego najbardziej
# oddalonymi od siebie wierzchołkami. Napisz algorytm, który
# przyjmując na wejściu drzewo (niekoniecznie binarne!) w postaci 
# listy krawędzi zwróci jego średnicę.


#rozwiazanie:
# startujemy bfsem z jednego miejsca i szukamy najwiekszego dystansu.
# z miejsca o najwiekszym (jesli nie ma jednego najwiekszego tylko np kilka to dowolny z nich)
# dystansie jeszcze raz puszczamy tego samego bfsa i wtedy znajdziemy maksymalną odległość
# czyli średnicę
from queue import SimpleQueue

def diameterOfTree(G):
    maksim = 0
    for i in range(len(G)):
        for x in G[i]:
            maksim = max(maksim,x)
    
    Graph = [[] for i in range(maksim+1)]

    for i in range(len(G)):
        Graph[G[i][0]].append(G[i][1])
        Graph[G[i][1]].append(G[i][0])

    def bfs(u):
        d = [0 for i in range(len(Graph))]
        visited = [False for i in range(len(Graph))]
        q = SimpleQueue()
        q.put(u)
        #visited[u] = True
        maksim = [0,0]
        while not q.empty():
            u = q.get()
            #if visited[u]: continue #ale to nigdy nie zajdzie
            visited[u] = True
            for v in Graph[u]:
                if visited[v]: continue
                d[v] = d[u] + 1                
                if maksim[0] < d[v]: 
                    maksim[0] = d[v]
                    maksim[1] = v
                q.put(v)
        return maksim

    tupl = bfs(0)
    #print(tupl)
    return (bfs(tupl[1]))[0]

        
G = [[0,5],[1,5],[3,5],[6,0],[7,0],[9,6],[8,7],[10,7],[11,10],[2,1],[12,1],[23,2],[14,2],[13,2],[21,14],[22,14],[20,15],[13,15],[3,16],[17,16],[18,16],[19,16]]

print(diameterOfTree(G))

            
