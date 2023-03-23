#  W kafejce internetowej jest K komputerów i A aplikacji
#  na płytkach CD. Na każdym komputerze może być zainstalowana
#  maksymalnie jedna aplikacja. Każda aplikacja ma listę komputerów 
#  na których może działać, a na pozostałych nie może z powodu 
#  wymagań sprzętowych. Jesteś właścicielem kafejki i wiesz, ile klientów
#  (możliwie zero) będzie chciało jutro skorzystać z danej aplikacji. 
#  Zakładamy, że każdy klient zajmuje komputer na cały dzień. 

#  Jaką aplikację powinieneś zainstalować na każdym z komputerów, aby wszyscy
#  klienci mogli korzystać z tej aplikacji, którą chcą? 
#  Jeżeli takie przyporządkowanie nie istnieje, algorytm powinien to stwierdzić

#rozw:
# budujemy graf, gdzie komputery i aplikacje są wierzcholkami. Robimy to przeplywami!
# mamy zrodlo i ujcie
# ze zrodla wychodzą krawedzie do aplikacji, gdzie waga takiej krawedzi oznacza ilosc chetnych 
# klientow na daną aplikację. 
# krawedzie miedzy aplikacjami a komputerami oznaczaja, ze z danej aplikacji da sie skorzystac na danym komputerze
# te krawedzie są o wadze 1 bo jest 1 osoba na 1 komputer.
# komputery łączone są z ujściem o wadze 1.

from queue import SimpleQueue


def BFS(graph, s, t, parent):
    visited = [False]*(len(graph))
    queue = SimpleQueue()
    queue.put(s)
    visited[s] = True
    while not queue.empty():
        u = queue.get()
        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                queue.put(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == t:
                    return True
    return False
def edmund_karp(graph,source, sink):
    parent = [-1]*(len(graph))
    max_flow = 0
    while BFS(graph,source, sink, parent) :
        path_flow = float("Inf")
        s = sink
        while(s !=  source):
            path_flow = min (path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow +=  path_flow
        v = sink
        while(v !=  source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow #residual edge!!! czyli taka odwrotna! pozwala na cofanie sie!
            v = parent[v]
    return max_flow



def kafejka(A,K,C):
    #robimy graf bedacy macierzą sasiedztwa
    # niech s,t -> odp: zrodlo i ujscie 
    #ponieważ K - komputery to tez wierzcholki, to musimy je przenumerowac!
    maks_num = len(A) #4 - nowy wierzcholek nr od 4
    #A = 0...3
    for i in range(len(K)):
        K[i] += maks_num
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] += maks_num
    
    print(A)
    print(K)
    maks_num = K[-1]
    #dodajemy jeszcze zrodlo i ujscie
    maks_num +=2
    G = [[0 for i in range(maks_num+1)] for j in range(maks_num+1)]
    s = maks_num-1
    t = maks_num
    for i in range(len(C)):
        G[s][i] = C[i]
    
    for i in range(len(A)):
        for komp in A[i]:
            G[i][komp] = 1
    for elem in K:
        G[elem][t] = 1
    max_flow = edmund_karp(G,s,t)
    for i in range(len(C)):
        print(G[i][s],"/",C[i]) # patrzymy w odwrotnej kolejnosci na krawedzie

    return True if sum(C) == max_flow else False    


# A - aplikacje
# K - komputery
# C - klienci 

'''A = [[0,3,5],[2,4,5],[1,2,3],[2,3,4,5]] -> [0,3,5] to 1. aplikacja na ktorej dzialaja
 komputery 0,3 i 5 itd.'''
'''K = [0,1,2,3,4,5] -> nr komputerow''' 
'''C = [2,2,1,0] -> z aplikacji 0. chce skorzystac 2 klientow
z aplikacji 1. tez, z apki 1. -> 1 klient, a z 3. apki -> zero klientow'''

A = [[0,3,5],[2,4,5],[1,2,3],[2,3,4,5]] 
K = [0,1,2,3,4,5] 
C = [2,2,1,0]
print(kafejka(A,K,C))


