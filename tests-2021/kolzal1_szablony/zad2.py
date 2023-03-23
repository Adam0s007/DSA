from zad2testy import runtests



#rozwiazanie:
#najpierw najlepiej jest przeksztalcic graf macierzowy na postac listy sasiedztwa 
#pozniej zaimplementować funkcję articulation Points
# dla kazdego znalezionego punktu w articulation points dfsem znajdujemy niespojne grafy

def Ap(G):
    visited = [False] * len(G)
    disc = [float("inf") for i in range(len(G))] 
    low = [float("inf") for i in range(len(G))] 
    parent = [-1] * len(G)
    ap = [False] * len(G)
    counter = [0]

    def articPoint(u):
        visited[u] = True
        disc[u] = counter[0]
        low[u] = counter[0]
        children = 0
        counter[0] +=1
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                children +=1
                articPoint(v)
                low[u] = min(low[u],low[v]) 
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u],disc[v]) #krawędź wsteczna
        if parent[u] == -1 and children > 1:
            ap[u] = True
    

    for i in range(len(G)):
        if not visited[i]:
            articPoint(i)

    return [i for i in range(len(ap)) if ap[i]] #[1,4,6,7,9]




def breaking(G):
    # tu prosze wpisac wlasna implementacje
    #zrobmy reprezentacje listową:
    graph= [[] for i in range(len(G))]
    for i in range(len(G)):
        for j in range(i+1,len(G)):
            if G[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
        
    invalid_edges = {}
    visited = {}
    ap  = Ap(graph)
    
    def dfs(u):
        visited[u] =True
        for v in graph[u]:
            if v not in visited and (u,v) not in invalid_edges and (v,u) not in invalid_edges: 
                dfs(v)
    
    maxComponents = 1 #jeden spojny caly graf
    bestVertice = None
    for u in ap:
        invalid_edges = {}
        visited = {}
        for v in graph[u]: 
            invalid_edges[(u,v)] = True 
        counter = 0
        for i in range(len(graph)):
            if i not in visited and i != u:
                dfs(i)
                counter+=1
        if counter > maxComponents:
            maxComponents = counter
            bestVertice = u
            
    return bestVertice


runtests( breaking )