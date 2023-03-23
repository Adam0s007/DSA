from zad8testy import runtests
import math
#Adam Biśta
# Generujemy wszystkie mozliwe krawedzie. Jest to tablica zawierajaca [w,u,v] w - odleglosci, u,v - wierzcholki
# sortujemy niemalejaco krawedzie wzgl odleglosci 
# generujemy drzewa rozpinające o V-1 krawiedziach korzystając z funkcji przydatnych do tworzenia zbiorów, 
# (stosowane w algorytmie Kruskala).
# przy kazdym generowaniu sprawdzamy minimalny dystans miedzy najkrotszą a najdluzszą krawedzią
# Optymalizacja: nie trzeba generowac ST dla tych samych najkrótszych krawędzi, wystarczy dla jednej, a reszte pomijamy.
# time complexity: O(E^2) (sortowanie jest w ElogE)

class Node:
    def __init__(self,value):
        self.parent = self
        self.value = value
        self.rank = 0


def makeSet(x):
    return Node(x)


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    if x.rank > y.rank: y.parent = x
    else: 
        x.parent = y
        if x.rank == y.rank:
            y.rank +=1


def highway( A ):
    edges = []
    for i in range(len(A)):
        x1,y1 = A[i]
        for j in range(i+1,len(A)):
            x2,y2 =A[j]
            d = math.ceil(((x1 - x2)**2 + (y1 - y2)**2)**(0.5))
            edges.append([d,i,j])
    edges.sort(key=lambda x: x[0]) 
    min_distance = float("inf")
    prev_distance = None 
    for e in range(len(edges)-len(A)+2): 
        iter = 0 
        x = 0 
        if prev_distance == None or prev_distance < edges[e][0]: 
            prev_distance = edges[e][0]
            S = [makeSet(i) for i in range(len(A))] 
            while iter < len(A)-1:
                if e+x < len(edges):
                    if find(S[edges[e+x][1]]) != find(S[edges[e+x][2]]):
                        union(S[edges[e+x][1]],S[edges[e+x][2]]) 
                        iter +=1  
                    if iter < len(A)-1:
                        x+=1 
                else: 
                    break    
            else: 
                min_distance = min(min_distance,edges[e+x][0] - edges[e][0])
            
    return min_distance 
        


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )