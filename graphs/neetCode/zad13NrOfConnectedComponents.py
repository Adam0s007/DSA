# Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
# (each edge is a pair of nodes), write a function to find 
# the number of connected components in an undirected graph.
# Example 1:
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#      0          3
#      |          |
#      1 --- 2    4 
# Output: 2

# Example 2:
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#      0           4
#      |           |
#      1 --- 2 --- 3
# Output:  1

# Note:
# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] and 
# thus will not appear together in edges.

class Solution:
    def countComponents(self,n:int,edges: list[list[int]]) -> int:
        class Node:
            def __init__(self,value):
                self.parent = self
                self.value = value
                self.rank = 0
        
        def make(x):
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
        
        S = [make(i) for i in range(n)]
        res = n #za kazdym razem jak bedą powstawac nowe zbiory, to bedziemy redukować 
        # liczbę połączonych komponentów
        for n1,n2 in edges:
            if find(S[n1]) != find(S[n2]):
                res -=1
                union(S[n1],S[n2])
        return res

