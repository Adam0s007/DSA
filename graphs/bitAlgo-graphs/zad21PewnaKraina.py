# # Pewna kraina sklada sie z wysp pomiedzy ktorymi istnieją połączenia lotnicze, promowe 
# # oraz mosty. Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. 
# # Koszt przelotu z wyspy na wyspę wynosi 8B. koszt przeprawy promowej wynosi 5B. 
# # Za przejście mostem trzeba wnieść opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, 
# # która na kolejnych wyspach zmienia środek transportu na inny oraz minimalizuje koszt podróży. 
# # Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy 
# # oznacza brak bezpośredniego  połączenia. Proszę zaimplementować funkcję islands(G,A,B)
# # zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca 
# # warunki zadania nie istnieej, funkcja powinna zwrócić wartość None.

# G = [ [0,5,1,8,0,0,0],
#     [5,0,0,1,0,8,0],
#     [1,0,0,8,0,0,8],
#     [8,1,8,0,5,0,1],
#     [0,0,0,5,0,1,0],
#     [0,8,0,0,1,0,5],
#     [0,0,8,1,0,5,0]]
# ]

#funkcja islands(G1,5,2) powinna zwrócić wartość 13.
from queue import PriorityQueue
def islands(G,a,b):
    visited=  [False for i in range(len(G)+1)]
    q = PriorityQueue()
    transport = -1 #to są 3 stany (-1 - brak transportu, 5,3,1)
    distance = [float("inf") for i in range(len(G)+1)]
    distance[a] = 0
    q.put((0,(a,transport)))
    while not q.empty():
        cost, tupl = q.get()
        u,trans = tupl
        if visited[u]: continue
        visited[u] = True
        for v in range(len(G[u])): 
            if visited[v] or trans == G[u][v] or G[u][v] == 0: continue
            if distance[u] + G[u][v] < distance[v]: 
                distance[v] = distance[u] + G[u][v]
                q.put((distance[v],(v,G[u][v])))
                if v == b: return distance[b]
    return None


G =[[0,5,1,8,0,0,0],
    [5,0,0,1,0,8,0],
    [1,0,0,8,0,0,8],
    [8,1,8,0,5,0,1],
    [0,0,0,5,0,1,0],
    [0,8,0,0,1,0,5],
    [0,0,8,1,0,5,0]
    ]

print(islands(G,5,2))