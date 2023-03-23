from kol2btesty import runtests
import heapq
def min_cost( O, C, T, L ):
    
    # tu prosze wpisac wlasna implementacje
    cost_on_parking = {}

    for i in range(len(O)):
        cost_on_parking[O[i]] = C[i] 
    O.sort()
    G = {elem:[] for elem in O}
    A =0 

    G[A] = [] #punkt startowy!
    G[L] = [] #punkt koncowy
    i  = 0 
    while i < len(O) and O[i] <=T:
        G[A].append((O[i],cost_on_parking[O[i]],0)) #0 na koncu oznacza ze nie wykorzystany zostal dodatkowy warunek
        i+=1
    while i < len(O) and O[i] <= 2*T:
        G[A].append((O[i],cost_on_parking[O[i]],1)) #1 na koncu oznacza ze wykorzystany zostal dodatkowy warunek
        i+=1
    if L < T:
        G[A].append((L,0,0))
    elif L < 2*T:
        G[A].append((L,0,1))
    
    for ind,elem in enumerate(O):
        i = ind+1
        while i < len(O) and O[i] -  elem <=T:
            G[elem].append((O[i],cost_on_parking[O[i]],0)) #0 na koncu oznacza ze nie wykorzystany zostal dodatkowy warunek
            i+=1
        while i < len(O) and O[i] - elem <= 2*T:
            G[elem].append((O[i],cost_on_parking[O[i]],1)) #1 na koncu oznacza ze wykorzystany zostal dodatkowy warunek
            i+=1
        if L - elem < T:
            G[elem].append((L,0,0))
        elif L  - elem <= 2*T:
            G[elem].append((L,0,1))
    

    dist = {elem:[float("inf"),float("inf")] for elem in G}
    dist[A][0] = 0
    visited = {elem:[False,False] for elem in G}
    q = [(0,A,0)] #(dist,A,0) # 0 oznacza ze nie wykorzystalismy krawedzi 2T
    # jesli flag == 1 to wykorzystana zostala juz krawedz 2T
    # czyli teraz juz bedziemy musieli zawsze utrzymywac flagę flag == 1 przy dodawaniu wierzcholkow do kolejki
    while q:
        cost,u,flag = heapq.heappop(q)
        if visited[u][flag]:continue
        visited[u][flag] = True
        for v,w,f in G[u]:
            if f == 0: #ten przypadek jest dla dowolnej naszej flagi        
                if flag == 1:
                    if dist[u][1] + w < dist[v][1]:
                        dist[v][1] = dist[u][1] + w
                        heapq.heappush(q,(dist[v][1],v,1)) #dodajemy flag zamiast f gdyz, jesli flag == 1 to 
                    # musimy przekazac flag == 1 tez do kolejki! a jesli flag == 0 no to tutaj tez dajemy flag == 1
                else:
                    if dist[u][0] + w < dist[v][0]:
                        dist[v][0] = dist[u][0] + w
                        heapq.heappush(q,(dist[v][0],v,0))
                    

            elif flag == 0: #jesli f == 1 oraz nie wykorzystalismy jeszcze krawedzi czyli flag == 0, to mozemy ją tutaj wykorzystac
                if dist[u][0] + w < dist[v][1]:
                    dist[v][1] = dist[u][0] + w
                    heapq.heappush(q,(dist[v][1],v,1)) #dodajemy 1 bo wykorzystalismy w tej chwili krawedz! 
            
    return min(dist[L][1], dist[L][0])

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
