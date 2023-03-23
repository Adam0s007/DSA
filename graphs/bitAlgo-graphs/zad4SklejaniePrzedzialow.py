# Dany jest ciąg przedziałów postaci [ai,bi]. Dwa przedziały można skeić, jeśli 
# mają dokładnie jeden punkt wspólny. Podaj algorytm, który sprawdza, czy da się uzyskać
# przedział [a,b] poprzez skejanie odcinków.

#rozwiazanie: tworzymy graf skierowany w ktroym punktami będą z przedzialow bierzemy ai oraz bi np 1. wierzcholek to ai a inny to b1,
# bedą połączone krawędziami oznaczającymi przedzial jakiś
#puszczamy dfs/bfs od wierzcholka a i sprawdzamy czy dojdzie on do b


def sklej(G,p):
    #szukamy maks:
    maks = p[1]
    for i in range(len(G)):
        maks = max(maks,G[i][1])

    Graph = [[] for i in range(maks)]
    for i in range(len(G)):
        Graph[G[i][0]].append(G[i][1])
    print(Graph)
    ai = p[0]
    bi = p[1]
    visited = [False for i in range(maks)]

    def dfs(u):
        if u == bi: return True
        if visited[u]: return False
        visited[u] = True
        for v in Graph[u]:
            if dfs(v): return True
        return False
    return dfs(ai)










G = [[1,2],[3,8],[1,3],[5,9],[1,4],[2,4],[3,5],[6,8],[5,8],[5,11]]
p = [3,12]
print(sklej(G,p))