
from egzP1btesty import runtests 
from queue import PriorityQueue
import heapq


def turysta( G, D, L ):
    vertices = 0

    for i in range (len(G)):
        if G[i][1] > vertices:
            vertices = G[i][1]


    graph = [[] for _ in range (vertices + 1)]
    for i in range (len(G)):
        graph[G[i][0]].append([G[i][1], G[i][2]]) # dodaję wierzchołek i wagę krawędzi
        graph[G[i][1]].append([G[i][0], G[i][2]])

    
    distance = [[10**9 for _ in range (vertices + 1)] for _ in range (5)] # wiersze to liczba odwiedzonych już wierzchołków, kolumny wierzchołki
    # łącznie muszę odwiedzić 5 wierzchołków, zaczynam z counterem = 5
    # odwiedzam wierzchołek D, więc liczba odwiedzonych 5 - 1 = 4
    # moja odpowiedz do ans[0][L] -> dojdę z licznikiem = 0 do wierzchołka L
    
    distance[4][D] = 0
    visited = [[False for _ in range (vertices + 1)] for _ in range (6)]
    Q = PriorityQueue()
    Q.put((0,D, 4)) #wkładam do kolejki wierzchołek D oraz to, ile wierzchołków jeszcze mam odwiedzić

    while not Q.empty():
        tup = Q.get()  
        cost = tup[0]
        wierzcholek = tup[1]
        counter = tup[2]

        if visited[counter][wierzcholek] == True:
            continue
        visited[counter][wierzcholek] = True

        for i in range (len(graph[wierzcholek])):
            if counter - 1 >= 0 and distance[counter-1][graph[wierzcholek][i][0]] > distance[counter][wierzcholek] + graph[wierzcholek][i][1]:
                distance[counter-1][graph[wierzcholek][i][0]] = distance[counter][wierzcholek] + graph[wierzcholek][i][1]
                Q.put((distance[counter-1][graph[wierzcholek][i][0]],graph[wierzcholek][i][0], counter-1))

    
    return distance[0][L]









    







        
# G = [
# (0, 1, 9), (0, 2, 1),
# (1, 2, 2), (1, 3, 8),
# (1, 4, 3), (2, 4, 7),
# (2, 5, 1), (3, 4, 7),
# (4, 5, 6), (3, 6, 8),
# (4, 6, 1), (5, 6, 1)
# ]
# D = 0
# L = 6
# print(turysta(G, D, L))


runtests ( turysta )