# Bajtocja jest krainą zawierającą N miast, N-1 dwukierunkowych dróg 
# i układ dróg tworzy graf spójny. Mając listę K miast do których musimy dostarczyć 
# przesyłki i mogąc wystartować i zakończyć trasę w dowolnym mieście, podaj minimum dystans,
# który musimy przebyć, żeby zrealizować to zadanie

#jest to MST
#szukamy średnicy.
#usuwamy zbedne galezie nie zawierajace naszych miast waznych.
# szukamy srednicy w naszym nowym grafie 
#za punkt startowy obieramy kraniec srednicy ktory jest miastem oznaczonym.
# idziemy dfsem, jesli mamy do wyboru sciezke bedącą czescią srednicy, a inną scieżkę
# to zawsze wybieramy inną ścieżkę. Wchodząc do wierzcholka distance zwiekszamy o 1, 
# ale przetwarzajac wierzcholek rowniez zwiekszamy o 1 (bo cofamy sie)
# gdy dojdziemy do wierzcholka koncowego srednicy to konczymy program i zwracamy aktualny dystans
from queue import SimpleQueue
def bajtocja(G,k):
    visited = [False for i in range(len(G))]
    #pamietaj zeby uzyc najlepiej dfsa na jednym z wierzcholkow oznaczonych z listy k!
    #zadziala tylko w  przypadku MST
    def dfs(G,u):
        visited[u] = True
        tmp = G[u].copy()
        for v in tmp:
            if not visited[v]:
                if not dfs(G,v): 
                    G[u].pop(G[u].index(v))
                    G[v].pop(G[v].index(u))
    
        if u not in k and len(G[u]) == 1:
            return False
        return True
    
    #bedziemy wyznaczac teraz srednice!
    dfs(G,k[0])
    #teraz trzeba uzyc 2 bfsy do wyznaczenia srednicy!
    distances = [0 for i in range(len(G))]
    def bfs(u):
        parents = [-1 for i in range(len(G))]
        visited = [False for i in range(len(G))]
        q =SimpleQueue()
        q.put(u)
        while not q.empty():
            u = q.get()
            visited[u] = True
            for v in G[u]:
                if not visited[v]:
                    parents[v] = u
                    distances[v] = distances[u] + 1
                    q.put(v)
        
        best_distance_ind =0
        best_distance = 0
        for i in range(len(distances)):
            if best_distance < distances[i]:
                best_distance = distances[i]
                best_distance_ind = i
        return best_distance_ind,parents
    
    ind,parents =  bfs(k[0])
    ind,parents = bfs(ind)
    path = []
    pathBoole = [False for i in range(len(G))]
    while ind != -1:
        path.append(ind)
        pathBoole[ind] = True
        ind = parents[ind]
    
    #print(path)
    visited = [False for i in range(len(G))]
    #bedziemy liczyc minimalna odleglosc by przejsc do wszystkich k miast
    def dfs_modified(u):
        visited[u] = True
        flag = 0
        dist = 0
        tmp = None
        if path[-1] == u: return 0 #jesli nasz wierzcholek jest koncowy to zwroc zero!
        for v in G[u]:
            if not visited[v]:
                if pathBoole[v] == True:  #tylko raz ten if wystąpi!
                    flag = 1 #oznaczamy ze wystepuje wierzcholek na sciezce srednicy
                    tmp = v #tymczasowo zapiszemy sobie ten wierzcholek na potem
                else:
                   dist = dist + 2 + dfs_modified(v) #jesli idziemy do sciezki, ktora nie lezy na naszej srednicy, to przy wracaniu musimy dodac 1
        if flag == 1:
            dist = dist + 1 + dfs_modified(tmp)
        return dist 
    return dfs_modified(path[0])          



    print(G)


G = [[1,2,3],[11,0,8],[0,5,4],[0],[2],[2,6],[5],[8],[9,7,1],[10,8],[9],[12,13,14,1],[11],[11],[11,15],[14,16,17],[15],[15,18],[17]]
k = [9,7,2,6,4,3,15]

print(bajtocja(G,k))