# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        time,fresh = 0,0
        ROWS,COLS = len(grid),len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append([r,c])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions: #potrzebna jest ta petla bo zawsze wykona sie tą samą
                # ilosc razy, nawet gdy q zostanie zaktualizowane, to
                # tutaj petla wykona się niezalezną ilosc razy od aktualnej q.
                #potrzebne to bo res to taki nasz "distance" a petla stanowi niejaką "falę"
                    row,col = dr + r, dc + c
                    #if in bounds and fresh, make it rotten
                    if (row < 0 or row == len(grid)
                    or col < 0 or col == len(grid[0]) 
                    or grid[row][col] != 1): continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -=1
            time += 1
        return time if fresh == 0 else -1