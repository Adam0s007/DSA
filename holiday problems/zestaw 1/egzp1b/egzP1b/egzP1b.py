from egzP1btesty import runtests 
import heapq
def turysta( G, D, L ):
    maksim = 0
    for x,y,w in G:
        maksim = max(maksim,x,y)
    graph = [[] for i in range(maksim+1)]
    for x,y,w in G:
        graph[x].append((y,w))
        graph[y].append((x,w)) 
    dist = [[float("inf") for j in range(5)] for i in range(maksim+1)]
    visited = [[False for j in range(5)] for i in range(maksim+1)] 
    dist[D][4] = 0  
    q = [(0,4,D)]
    while q:
        cost,counter,u = heapq.heappop(q)
        if visited[u][counter]: continue
        visited[u][counter] = True 
        for v,w in graph[u]:
            if counter - 1 >= 0 and dist[v][counter-1] > dist[u][counter] + w:
                dist[v][counter-1] = dist[u][counter] + w
                heapq.heappush(q,(dist[v][counter-1],counter-1,v))
    return dist[L][0]

runtests ( turysta )