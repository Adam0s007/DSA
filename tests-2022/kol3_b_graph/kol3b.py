from kol3btesty import runtests
import heapq

#wystarczy zrobic dodatkowy wierzcholek, polaczona krawedzią z kazdego innego wierzcholka, są one nieskierowane te krawędzie
# ich koszty to wartosci wylotu z lotnisk!
def airports( G, A, s, t ):
    
    G.append([]) #dodatkowy wierzcholek, ktory bedzie mial polaczenie z kazdym innym wierzcholkiem 
    for i in range(len(G)-1):
        G[i].append((len(G)-1,A[i])) #pierwsza krawedz do wierzcholka v jest rowna startowi z lotniska z wierzcholka i
        G[len(G)-1].append((i,A[i])) #druga krawedz z wierzcholka v jest rowna przyleceniu na lotnisko o wierzcholku i
    
    dist = [float("inf") for i in range(len(G))]
    visited = [False for i in range(len(G))]
    dist[s] = 0
    q = [[0,s]]

    while q:
        cost,u = heapq.heappop(q)
        if visited[u]: continue 
        visited[u] = True
        for v,w in G[u]:
            if visited[v]: continue
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w  
                heapq.heappush(q,[dist[v],v])
                
    
    return dist[t]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )