from zad8testy import runtests
import math
from queue import PriorityQueue
class Node:
    def __init__(self,value):
        self.parent = self
        self.value = value
        self.rank = 0


def make_set(x: int):
    return Node(x)


def find_set(x):
    if x.parent != x:
        x.parent = find_set(x.parent)
    return x.parent


def union_sets(x: int, y: int):
    x = find_set(x)
    y = find_set(y)
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
            d = int(((x1 - x2)**2 + (y1 - y2)**2)**(0.5))
            edges.append([d,i,j])
    #do tej pory jest O(V^2)
    edges.sort(key=lambda x: x[0]) #jesli to zrobie to bedzie V^2(logV^2)
    #print(edges)
    #heap = PriorityQueue()
    #teraz sprawdzamy z osobna kazde V-1 krawedzi! (sprawdzamy ich min_distance oraz czy wgl kazda trojka stworzy spanning_tree)
    #tu zrobimy najkrotszą różnicę
    min_distance = float("inf")
    prev_distance = None #bedziemy tu zapisywać ostatni dystans
    S = [make_set(i) for i in range(len(A))]
    for e in range(len(edges)-len(A)+2): #wszystkie mozliwe krawedzie - rozpatrywane do stworzenia ST
        iter = 0
        x = 0
        if prev_distance == None or prev_distance < edges[e][0]:
            prev_distance = edges[e][0]
            for i in range(len(S)):S[i].parent = S[i]
            while iter < len(A)-1:
                if e+x < len(edges):
                    if find_set(S[edges[e+x][1]]) != find_set(S[edges[e+x][2]]):
                        union_sets(S[edges[e+x][1]],S[edges[e+x][2]]) 
                        iter +=1
                    if iter < len(A)-1:
                        x+=1
                else: 
                    break    
            else: 
                min_distance = min(min_distance,edges[e+x][0] - edges[e][0])
            
    return min_distance 
        


A = [(10, 10), (15, 25), (20, 20), (30, 40)]
highway(A)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )