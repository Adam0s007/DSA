# Komunikacja miejska w Pewnym Mieście jest dość dziwnie zorganizowana. 
# Za przejechanie każdego odcinka między dwiema stacjami obowiązuje osobna opłata. 
# Od tej kwoty jest jednak odejmowany całkowity koszt poniesiony od początku 
# podróży ( jeśli jest ujemny, po prostu nic się nie płaci). 

# Np. na trasie 1-2-3-4 opłaty wynoszą kolejno: 60+20+0,
# a na trasie 1-4-5 będzie to 120+30 

# Mając dane: 
# - graf połączeń w dowolnej reprezentacji (nieskierowany, ważony)
# - numry stacji początkowej i docelowej.

# Oblicz minimalny koszt przejechania tej trasy.
from queue import PriorityQueue
def minim_koszt(G,s,t):
    parent = [-1 for i in range(len(G))]
    sums =  [float("inf") for i in range(len(G))]
    visited = [False for i in range(len(G))]
    q = PriorityQueue()
    sums[s] = 0
    q.put((0,s))
    while not q.empty():
        sum,u = q.get()
        if visited[u]: continue 
        visited[u] = True
        for v,w in G[u]: 
            if not visited[v]: 
                #uwaga tutaj zadziala tez sums[u] = max(sums[u],w)
                cost = w - sums[u] if w - sums[u] > 0 else 0 
                if cost + sums[u] < sums[v]:
                    sums[v] = cost + sums[u]
                    parent[v] = u
                    q.put((sums[v],v))

    return sums[t]






G = [[(1,60),(3,120)],[(0,60),(2,80)],[(1,80),(4,70)],[(0,120),(4,150)],[(2,70),(3,150)]]

print(minim_koszt(G,0,4))