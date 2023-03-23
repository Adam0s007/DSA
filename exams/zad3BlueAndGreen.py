# Dany jest ważony graf nieskierowany reprezentowany przez macierz T o rozmiarach 
# n x n (dla kazdych i,j zachodzi T[i][j] = T[j][i]); wartość T[i][j] > 0 oznacza, 
# że istnieje krawędź między wierzcholkiem i a  wierzcholkiem j z wagą T[i][j]. 
# Dana jest także liczba rzeczywista d. Każdy wierzchołek w G ma jeden z kolorów: zielony 
# lub niebieski. Zaproponuj algorytm, który wyznacza największą liczbę naturalną E, taką, że 
# w grafie istnieje E par wierzchołków (p,q) e V x V spełniających następujące warunki:
# 1. q jest zielony zaś p jest niebieski
# 2. Odległości między p i q (liczona jako suma wag krawędzi najkrótszej ścieżki) jest 
# nie mniejsza niż d
# 3. każdy wierzchołek występuje w co najwyżej jednej parze

# Rozwiązanie należy zaimplementować w postacji funkcji:
# def BlueAndGreen(T,K,D): ...
# która przyjmuje:
# T: graf reprezentowany przez kwadratową macierz sąsiedztwa, gdzie 0 ozn brak krawedzi, a liczba
# większa od 0 przedstawia odległość pomiędzy wierzchołkami.
# K: listę przedstawiającą kolory wierzchołków.
# D: odległość o której mowa w warunku 2 opisu zadania.

# Funkcja powinna zwrócić liczbę E omawianą w treści zadania.


#rozwiazanie: 
# 1) floyd warshall
# 2)Nowy graf: 
# - odl >= d
# - rozne kolory

# Ford Fulkerson - edmond Karp:

# zrodlo: (z niego krawedzie wychodzace do wszystkich wierzcholkow niebieskich wagi 1)
# B       G  (miedzy wierzcholkami moze byc wiele krawedzi ale wszystkie o wadze 1!)
# B       G  
# B       G
# B       G 
# B       G
#         G
#         G 

# z wierzcholkow zielonych krawedzie ida do ujscia o wadze 1
# w ten sposob zliczymy wszystkie te krawedzie!
# maksymalny przeplyw da wynik

from queue import SimpleQueue
def FloydWarshall(T,K,D):
    for k in range(len(T)):
        for i in range(len(T)):
            for j in range(len(T)):
                if T[i][k] + T[k][j] != 0 and T[i][j] > T[i][k] + T[k][j]:
                    T[i][j] = T[i][k] + T[k][j]
                if T[i][j] == 0 and T[i][k] + T[k][j] > 0:
                    T[i][j] = T[i][k] + T[k][j]
    
    for i in range(len(T)):
        for j in range(len(T)):
            if K[i] == 'B' and K[j] == 'G' and T[i][j] >= D: continue
            T[i][j] = 0

    for i in range(len(T)):
        for j in range(len(T)):
            print(T[i][j],end=" ")
        print()
    return T

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
        v = sink
        #znajdowanie najmniejszego przeplywu na danej sciezce
        while(v !=  source):
            path_flow = min (path_flow, graph[parent[v]][v])
            v = parent[v]
        max_flow +=  path_flow
        v = sink
        #usuwanie / dodawanie najmniejszego przeplywu miedzy krawedziami na danej sciezce
        while(v !=  source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow #residual edge!!! czyli taka odwrotna! pozwala na cofanie sie!
            v = parent[v]
    return max_flow

def BlueAndGreen(T,K,D):
    T = FloydWarshall(T,K,D)

    #teraz tworzymy nowy graf z s - source, t - sink
    G = [[0 for i in range(len(T)+2)] for j in range(len(T)+2)]
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j] != 0:
                G[i][j] = 1
                G[-2][i] = 1
                G[j][-1] = 1
    print()
    for i in range(len(G)):
        for j in range(len(G)):
            print(G[i][j],end=" ")
        print()

    return edmund_karp(G,len(G)-2,len(G)-1)


T = [ [0,1,1,0,1],
    [1,0,0,1,0],
    [1,0,0,0,1],
    [0,1,0,0,1],
    [1,0,1,1,0]
]
K = ['B','B','G','G','B']
D = 2

print(BlueAndGreen(T,K,D))