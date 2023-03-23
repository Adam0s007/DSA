# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, 
# with one additional edge added. The added edge has two different vertices chosen from 1 to n, 
# and was not an edge that already existed. 
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] 
# indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes.
#  If there are multiple answers, return the answer that occurs last in the input.

 

# Example 1:


# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:


# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        class Node:
            def __init__(self,value):
                self.parent = self
                self.value = value
                self.rank = 0
        
        def make_set(x):
            return Node(x)


        def find_set(x):
            if x.parent != x:
                x.parent = find_set(x.parent)
            return x.parent


        def union(x, y):
            x = find_set(x)
            y = find_set(y)
            if x == y: return
            if x.rank > y.rank: y.parent = x
            else: 
                x.parent = y
                if x.rank == y.rank:
                    y.rank +=1
        
        S = [make_set(i) for i in range(len(edges)+1)]
        ans = [] #zwrocimy ostatni
        for n1,n2 in edges:
            if find_set(S[n1]) != find_set(S[n2]):
                union(S[n1],S[n2])
            else: ans.append([n1,n2])
        return ans[-1]
        