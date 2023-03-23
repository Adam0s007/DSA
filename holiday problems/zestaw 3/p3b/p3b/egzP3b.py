from egzP3btesty import runtests 
from queue import PriorityQueue
import heapq
def lufthansa ( G ):
    #tutaj proszę wpisać własną implementację 
    ilosc_lotow_obecna = [0]
    visited = {}
    edges = {}
    #najpierw obliczymy ilosc lotow 
    for u in range(len(G)): #O(n + m)
        for v,w in G[u]:
            if (u,v) in visited or (v,u) in visited:continue
            edges[(u,v,w)] = False #0 na koncu oznacza 
            ilosc_lotow_obecna[0] += (w) 
            visited[(u,v)] = True
    #Prim algorithm 
    visit = set()
    def Prims(G):
        N = len(G)
        total_cost = 0
        # [cost,(point,parent[point])]
        minH = [[0,(0,-1)]]
        while len(visit) < N:
            cost,tup = heapq.heappop(minH)
            u,parentU = tup
            if u in visit:continue
            if parentU != -1: 
                if (parentU,u) in visited: edges[(parentU,u,-1*cost)] = True
                else: edges[(u,parentU,-1*cost)] = True
            total_cost += (-1*cost)
            visit.add(u)
            for nei,neiCost in G[u]:
                if nei not in visit:
                    heapq.heappush(minH, [-1*neiCost,(nei,u)])
        return total_cost
    newConnections = Prims(G)
    # print(ilosc_lotow_obecna[0])
    # print(edges)
    # print(newConnections)
    bestVal = 0
    for key,value in edges.items():
        if value == False: bestVal = max(bestVal,key[2])

    return ilosc_lotow_obecna[0] - newConnections - bestVal


runtests ( lufthansa, all_tests=True )

# G = [
# [(1, 15), (2, 5), (3, 10) ],
# [(0, 15), (2, 8), (4, 5), (5, 12)],
# [(0, 5), (1, 8), (3, 5), (4, 6) ],
# [(0, 10), (2, 5), (4, 2), (5, 11)],
# [(1, 5), (2, 6), (3, 2), (5, 2) ],
# [(1, 12), (4, 2), (3, 11) ]
# ]
# print(lufthansa(G))