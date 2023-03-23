# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int)
#  and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            oldToNew[node] = Node(node.val)
            for nei in node.neighbors:
                oldToNew[node].neighbors.append(dfs(nei))
            
            return oldToNew[node]
        return dfs(node) if node else None

ans = Solution()
ans.cloneGraph([[2,4],[1,3],[2,4],[1,3]])