# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
# An island is a 4-directionally connected group of 1's not connected to any other 1's. 
# There are exactly two islands in grid.
# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
from collections import deque

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        N = len(grid)
        direct = [[0,1],[0,-1],[1,0],[-1,0]]

        def invalid(r,c):
            return r < 0 or c < 0 or r == N or c == N
        visit = set()
        def dfs(r,c):
            if invalid(r,c) or not grid[r][c] or (r,c) in visit:
                return
            visit.add((r,c))
            for dr,dc in direct:
                dfs(r+dr,c+dc)
        
        def bfs():
            res,q = 0, deque(visit) #dzieki dfs jest juz wypelniona!
            while q:
                length = len(q)
                for i in range(length): #tworzymy "warstwe" niezmienna mimo zmian w q bo for to taki generator!
                    #dlatego for i in range(len(q)) tez zadziala! ale length to bardziej czytelne
                    r,c = q.popleft()
                    for dr, dc in direct:
                        curR, curC = r+ dr, c + dc 
                        if invalid(curR,curC) or (curR,curC) in visit:
                            continue
                        if grid[curR][curC]: return res
                        q.append([curR,curC])
                        visit.add((curR,curC))
                res +=1

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c) #filling the islands
                    return bfs()

        