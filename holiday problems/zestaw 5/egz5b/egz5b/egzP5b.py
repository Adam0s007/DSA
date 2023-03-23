from egzP5btesty import runtests 




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
                low[u] = min(low[u],disc[v])
        if parent[u] == -1 and children > 1:
            ap[u] = True

    for i in range(len(G)):
        if not visited[i]:
            articPoint(i)
    return [i for i in range(len(ap)) if ap[i]]

def koleje ( B ):
    maksim = 0
    for p,k in B:
        maksim = max(maksim,p,k)
    G = [[] for i in range(maksim+1)]
    for p,k in B:
        G[p].append(k)
        G[k].append(p)
    
    return len(Ap(G))

runtests ( koleje, all_tests=True )