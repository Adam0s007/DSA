# Given a m x n grid filled with non-negative numbers,
#  find a path from top left to bottom right, 
# which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.


# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

class Solution:
    def minPathSum(self, grid) -> int:
        rows,cols = len(grid), len(grid[0])
        dp = [[float("inf")]*(cols+1) for r in range(rows+1)]
        dp[rows-1][cols] = 0 #zeby minimum dzialalo!
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                dp[r][c] = grid[r][c] + min(dp[r+1][c],dp[r][c+1])
        return dp[0][0]