#Simple Prim's Algorithm

#zawsze wybieraj najmniejsze koszty krawedzi z heapu!
#zawsze sprawdzaj czy dany wierzcholek juz nie zostal przetworzony
#w pętli: zawsze odrzucaj wierzcholek, ktory byl juz przetwarzany aby uniknac nagromadzenia niepotrzebnych rzeczy w priority queue
import heapq
def Prims(G):
    N = len(G)
    total_cost = 0
    visit = set()
    
    edges = []
    # [cost,(point,parent[point])]
    minH = [[0,(0,-1)]]
    while len(visit) < N:
        cost,tup = heapq.heappop(minH)
        u,parentU = tup
        if u in visit:
            continue
        if parentU != -1: edges.append([parentU,u])
        total_cost += cost
        visit.add(u)
        for nei,neiCost in G[u]:
            if nei not in visit:
                heapq.heappush(minH, [neiCost,(nei,u)])
    return total_cost,edges


G = [[[1,28],[5,10]],[[0,28],[6,14],[2,16]],[[1,16],[3,12]],[[2,12],[6,18],[4,22]],[[5,25],[6,24],[3,22]],[[4,25],[0,10]],[[1,14],[4,24],[3,18]]]
print(Prims(G))