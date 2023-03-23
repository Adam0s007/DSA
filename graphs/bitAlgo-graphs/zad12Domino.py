# Mamy pewien układ klocków domino. Otrzymujemy go w postaci listy par [a,b]: Jeżeli 
# przewrócimy klocek a, to klocek b też się przewróci. Chcemy znaleźć minimalną liczbę klocków, 
# które trzeba przewrócić ręcznie, aby wszystkie domina były przewrócone.


#Rozwiazaniem bedzie zastosowanie algorytmu na strongly connected components.
#szukamy ilosc silnie spojnych skladowych, one bedą odpowiedzią do zadania.



def domino(G):
    maks = 0
    for x,y in G:
        maks = max(maks,x,y)
    Graph = [[] for i in range(maks+1)]
    verified = [False for i in range(maks+1)] #dane wierzcholki muszą byc w tym grafie! nie ma zmiluj sie!
    for x,y in G:
        Graph[x].append(y)
        verified[x] = True
        verified[y] = True
    visited = [False for i in range(len(Graph))]
    
    stack = []
    counter = 0
    
    def topological_sort(u,Graph):
        visited[u] = True
        for v in Graph[u]:
            if not visited[v]:
                topological_sort(v,Graph)
        stack.append(u)

    def transpose(G):
        inverted_Graph = [[] for i in range(maks+1)]
        for i in range(len(G)):
            if verified[i] == False: continue
            for elem in G[i]:
                inverted_Graph[elem].append(i)
        return inverted_Graph
    
    #damy na koniec tą versię dfsa
    
    def dfs(u,Graph): 
        visited[u] = True
        for v in Graph[u]:
            if not visited[v]:
                dfs(v,Graph)

    for i in range(len(G)):
        if verified[i] == False: continue
        if not visited[i]:
            topological_sort(i,Graph)
    
    inverted_Graph = transpose(Graph)
    print(Graph)
    print(inverted_Graph)
    counter = 0
    print(stack)
    visited = [False for i in range(len(Graph))]
    while stack:
        u = stack.pop()
        if not visited[u]:
            dfs(u,inverted_Graph)
            counter +=1
    return counter
    
G = [[1,2],[3,4],[5,6],[7,7],[6,5],[10,11],[2,3],[4,1],[5,11]]
print(domino(G))


    
    
