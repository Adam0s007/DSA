# Otrzymujemy na wejściu w postaci listy krawędzi skierowany graf acykliczny DAG 
# (DAG - Directed Acyclic Graph) oraz parę wierzchołków s i t. Naszym zadaniem jest
# obliczyć, ile jest możliwych ścieżek między s i t


G = [[1,2,3],[4],[5],[7,6],[12],[8],[8],[9],[9],[10,11],[11],[],[11]]


def DAG(G,s,t): 
    dp = [0 for i in range(len(G))]
    def dfs(G,s,t):
        if s == t: return 1
        if len(G[s]) == 0: return 0
        if dp[s]: return dp[s]
        counter = 0 
        for v in G[s]: 
            counter += dfs(G,v,t)
        dp[s] = counter
        return counter
    return dfs(G,s,t)

print(DAG(G,0,11))
