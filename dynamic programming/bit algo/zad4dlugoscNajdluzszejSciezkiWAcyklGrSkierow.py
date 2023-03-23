# Znajdz długość najdłuższej ścieżki w grafie acyklicznym skierowanym.

#rozw: algorytm dfs z zapamietywaniem wyniku w tablicy dp
#niech Graph - lista sąsiedztwa
#O(V + E)
def longest_path_graph(Graph):
    dp = [-1 for i in range(len(Graph)+1)]
    visited = {}
    
    def dfs(u):  
        visited[u] = True
        
        if dp[u] != -1: 
            return dp[u]
        if not len(Graph[u]):
            dp[u] =0
            
        for v in Graph[u]:
            dp[u]  = max(dp[u], 1 + dfs(v))
    
        return dp[u] 
        

    for i in range(len(Graph)):
        if i not in visited:
            dfs(i)
    
    return max(dp)

Graph = [[1],[4,5,6],[1],[2],[8],[9],[10,7],[],[11],[],[],[]]

print(longest_path_graph(Graph))