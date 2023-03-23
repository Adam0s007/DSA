# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

# Example 1:

# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:


# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# Example 3:

# Input: matrix = [[1]]
# Output: 1

class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        ROWS,COLS = len(matrix),len(matrix[0])
        dp = [[0 for i in range(COLS)] for j in range(ROWS)]
        def dfs(r,c,prevVal):
            if (r < 0 or r == ROWS or
            c < 0 or c == COLS or
            matrix[r][c] <= prevVal): #wtedy od razu mozemy zwracać 0 bo to nie jest ta dlugosc!
                return 0
            if dp[r][c]:
                return dp[r][c]
            res = 1
            res = max(res,1 + dfs(r+1,c,matrix[r][c])) #prevem staje sie obecna wartosc 
            res = max(res,1 + dfs(r-1,c,matrix[r][c]))
            res = max(res,1 + dfs(r,c-1,matrix[r][c]))
            res = max(res,1 + dfs(r,c+1,matrix[r][c]))
            dp[r][c] = res
            return res
        
        maksim = 0
        for r in range(ROWS):
            for c in range(COLS):
                maksim = max(maksim,dfs(r,c,-1)) #-1 zeby pierwszy if sie nie wykonywal od razu w funkcji dfs!
        return maksim
