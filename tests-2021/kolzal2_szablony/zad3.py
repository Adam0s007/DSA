from zad3testy import runtests
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
        


    
runtests( paths )


