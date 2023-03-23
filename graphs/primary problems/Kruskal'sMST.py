"""
Reprezentacja macierzowa grafu.
G[i][j] = 7 <-> pomiędzy wierzchołkami i oraz j jest krawędź o wadze 7.
"""

class Node:
    def __init__(self,value):
        self.parent = self
        self.value = value
        self.rank = 0


def kruskal(G):
    n = len(G)
    E = []
    for i in range(n):
        for j in range(i+1, n):
            if G[i][j] != float("inf"):  # lub np MAX = 10 ** 10
                E.append((G[i][j], i, j))

    E = sorted(E,key=lambda x: x[0])
    S = [make_set(i) for i in range(n)]
    T = []
    for _, p, q in E:
        if find_set(S[p]) != find_set(S[q]):
            T.append((p, q))
            union_sets(S[p], S[q])


def make_set(x):
    return Node(x)


def find_set(x):
    if x.parent != x:
        x.parent = find_set(x.parent)
    return x.parent


def union_sets(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y: return
    if x.rank > y.rank: y.parent = x
    else: 
        x.parent = y
        if x.rank == y.rank:
            y.rank +=1
