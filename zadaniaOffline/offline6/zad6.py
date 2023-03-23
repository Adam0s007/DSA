#Adam Biśta
#O(E+V): robimy bfsa ktory bedzie nam warstwami (falą) dochodził do ostatniego wierzcholka (bez zadnego ifa odnosnie tego wierzcholka!)
# tworzymy tablicę parentów, kazdy wierzcholek moze miec wielu parentow!!!
# zeby to powyzsze stwierdzenie dzialalo to if not visited[v]: tutaj robimy parenta z v do u oraz dodajemy do kolejki v
# a przed tą pętlą for v in G[u] sprawdzamy czy dany wierzcholek juz jest w polu visited

#pozniej idziemy od ostatniego wierzcholka do pierwszego stosujac rowniez falowego bfsa, tym przy KAZDEJ fali
# for i in range(q.size()) musimy sprawdzic czy istnieje jakas krawedz ktora posiada NAJMNIEJSZY JEDEN DYSTANS!
# UWAGA MUSI BYC JEDEN NAJMNIEJSZY!
# jesli takowy istnieje no to zwracamy tą krawędź
 
#memory complexity: O(V)
from zad6testy import runtests
#from collections import deque

from collections import deque
def longer(G, s,t): 
    visited = [False for i in range(len(G))]
    dist = [0 for i in range(len(G))]
    parent = [[] for i in range(len(G))]
    q = deque()
    q.append(s)
    counter = 0
    
    while q:
        for i in range(len(q)):
            u = q.popleft()
            if visited[u]:continue
            visited[u]= True
            dist[u] = counter
            for v in G[u]:
                if not visited[v]:
                    q.append(v)
                    parent[v].append(u)
        counter+=1
    
    #teraz sie cofamy
    visited = [False for i in range(len(G))]
    
    q.append(t)
    while q:
        czyMozna = False #zmienimy na False jesli znajdziemy wierzcholek o takim samym najmniejszym dystansie
        najmniejszy = float("inf")
        wierzcholek = None
        rodzicWierzch = None
        #musi przejsc fala!
        for i in range(len(q)):
            u = q.popleft()
            if visited[u]:continue
            visited[u] = True
            for v in parent[u]:
                if not visited[v]:
                    if dist[v] < najmniejszy:
                        najmniejszy = dist[v]
                        wierzcholek = v
                        rodzicWierzch = u
                        czyMozna = True
                    elif dist[v] == najmniejszy: #znalezlismy ten sam dystans dla wierzcholka - nie wiemy ktorą krawędź usunac
                                          # wiec nie mozemy usunac zadnej krawedzi
                        czyMozna = False
                    q.append(v)
        if czyMozna: #wtedy nigdy nie wykona sie elif
            return (wierzcholek,rodzicWierzch)
            
    return None 


printG9 = [[1, 2], [0, 2, 3], [0,1, 7], [1,5,4], [ 3, 6, 7], [3,7], [4, 7], [2,5,4,6]]
print(longer(printG9, 0, 4)) # None
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )