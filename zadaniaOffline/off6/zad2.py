from zad2testy import runtests

import queue

def makePath(t,parent):
    ans = []
    def rek(t):
        if t != None:
            rek(parent[t])
            ans.append(t)
    rek(t)
    return ans

def bfs(leader,s,t,G,visited,distance):
    visited[s] = False 
    Q = queue.SimpleQueue()
    Q.put(s)
    f = 0
    while not Q.empty() and f == 0: 
        u = Q.get()
        for v in G[u]:
            if u == leader[0] and v == leader[1]:
                #visited[v] = False
                continue
            if visited[v]:
                visited[v] = False
                distance[v] = distance[u] + 1
                if v != t: Q.put(v)
                else: 
                    f = 1
                    break
    if f == 0: return float("inf")
    return distance[t]

def enlarge(G, s,t): 
    visited = [False for i in range(len(G))]
    distance = [0 for i in range(len(G))]
    parent = [None for i in range(len(G))]
    visited[s] = True
    Q = queue.SimpleQueue()
    Q.put(s)
    path = [] 
    isCycled = [False for i in range(len(G))]
    f = 0
    while not Q.empty(): 
        u = Q.get()
        for v in G[u]:
            if visited[v] and v != parent[u] and not isCycled[v]:
                isCycled[v] = True
            elif not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u 
                if v != t: Q.put(v)
                else: f = 1
    if f == 0: return None
    path = makePath(t,parent)
    oldDistance = distance[t]
    leader = None
    stop = True
    iter = 0 
    while iter < len(path) and stop: 
        u = path[iter]
        if u == t:
            leader = (parent[u],u)
            break
        elif isCycled[u]:  
            for v in G[u]:
                if distance[v] == distance[parent[u]] and v != parent[u]:  
                    iter+=1
                    leader = (u,path[iter])
                    stop = False
                    break
            else: 
                leader = (parent[u],u)
                break     
        else:
            iter +=1
    distance_new = bfs(leader,s,t,G,visited,distance)
    if distance_new > oldDistance: return leader
    return None 

runtests( enlarge ) 
