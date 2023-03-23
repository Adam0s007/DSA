from kol2atesty import runtests
import heapq
def drivers( P, B ):
    #z kazdego punktu przesiadkowego trzeba zrobic krawedz do 2 nastepnych punktow przesiadkowych
    origin_ind = {}
    for ind,elem in enumerate(P):
        origin_ind[elem[0]] =ind
    
    P.sort(key=lambda x: x[0])
    
    #TRUE - punkt przesiadkowy
    # false = punkt kontrolny
    
    G = [[] for i in range(B+1)]
    #jacek zaczyna! a nam chodzi o to by marian jak najrzadziej jezdzil przez punkty kontrolne.
    # w dijkstrze wagi krawedzi to punkty kontrolne a punkty przesiadkowe to wierzcholki
    # gdy jedzie jacek to nie bierzemy pod uwage wag krawedzi (ich waga == 0) natomiast gdy jedzie 
    # marian to waga istnieje i jest zlozona z wszystkich pktow kontrolnych pomiedzy przesiadkami

    A = 0
    przesiadki =  []
    index_od_przesiadka = []
    for i in range(len(P)):
        if P[i][1] == True:
            przesiadki.append(P[i][0])
            index_od_przesiadka.append(i)

    
    licznik = 0
    for i in range(3):
        G[A].append([przesiadki[i],index_od_przesiadka[i]-licznik])
        licznik+=1


    for ind,ind_of_przesiadka in enumerate(przesiadki):
        licznik = 0
        for i in range(1,4):
            if ind + i < len(przesiadki):
                G[ind_of_przesiadka].append([przesiadki[ind+i],index_od_przesiadka[ind+i] - index_od_przesiadka[ind]-1-licznik])
                licznik+=1
     
    G[przesiadki[-1]].append([B,len(P) - 1 - index_od_przesiadka[-1]])
    G[przesiadki[-2]].append([B,len(P) - 1 - index_od_przesiadka[-2] - 1])
    G[przesiadki[-3]].append([B,len(P) - 1 - index_od_przesiadka[-3] - 2])
    dist = [[float("inf")for i in range(2)] for i in range(len(G))] #bo jacek/Marian
    parent = [[[-1,-1] for i in range(2)] for i in range(len(G))]
    visited = [[False for i in range(2)] for i in range(len(G))]
    #dist[v][1] - Jacek 
    #dist[v][0] = Marian
    
    isJacek = 1
    dist[A][isJacek] = 0
    q = [(dist[A],A,isJacek)]
    ans = []
    while q:
        cost,u,isJacek = heapq.heappop(q)
        if visited[u][isJacek]: continue
        visited[u][isJacek] = True
        for v,w in G[u]:
            if isJacek == 0:
                if dist[v][1] > dist[u][0] + w: 
                    dist[v][1] = dist[u][0] + w 
                    parent[v][1][0] = u 
                    parent[v][1][1] = 0
                    heapq.heappush(q,[dist[v][1],v,1])
            else:
                if dist[v][0] > dist[u][1]:
                    dist[v][0] = dist[u][1]
                    parent[v][0][0] = u 
                    parent[v][0][1] = isJacek
                    heapq.heappush(q,[dist[v][0],v,0])
    
    ans = []
    w = None
    if dist[B][1] > dist[B][0]:
        B,w = parent[B][0]
    else: B,w = parent[B][1]

    while B != 0:
        ans.append(origin_ind[B])
        B,w = parent[B][w]
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )