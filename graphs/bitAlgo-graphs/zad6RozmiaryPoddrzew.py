# Dostajemy na wejściu listę krawędzi drzewa (niekoniecznie binarnego!) oraz wyróżniony
# wierzchołek - korzeń. Każdy wierzchołek tworzy swoje własne poddrzewo. Dla każdego wierzchołka,
# wyznacz ilość wierzchołków w jego poddrzewie


def count_vertices(G,root):
    maksim = 0
    for i in range(len(G)):
        for x in G[i]:
            maksim = max(maksim,x)
    
    Graph = [[] for i in range(maksim+1)]

    for i in range(len(G)):
        Graph[G[i][0]].append(G[i][1])
        Graph[G[i][1]].append(G[i][0])
    #print(Graph)
    visit = [False for i in range(len(Graph))]
    counted = [0 for i in range(len(Graph))]
    def dfs(u):
        count = 0
        visit[u] = True
        for v in Graph[u]:
            if visit[v]: continue
            count = count + 1 + dfs(v)
        counted[u] = count
        return count
    dfs(root)
    #print(counted)
    G.sort(key=lambda x:x[0])
    print(G)
            
#mozna to zrobic tez binary searchem
#ale wtedy w przedziale [ai bi] krawedz jest skierowana! z ai do bi!
G = [[0,5],[1,5],[3,5],[6,0],[7,0],[9,6],[8,7],[10,7],[11,10],[2,1],[12,1],[23,2],[14,2],[13,2],[21,14],[22,14],[20,15],[13,15],[3,16],[17,16],[18,16],[19,16]]
root = 5
count_vertices(G,root)