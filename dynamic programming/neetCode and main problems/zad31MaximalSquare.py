# Given an m x n binary matrix filled with 0's and 1's, 
# find the largest square containing only 1's and return its area.

class Solution:
    def maximalSquare(self, matrix):
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]    
        maksimEdge =0
        for j in range(len(matrix[0])):
            dp[-1][j] = 1 if matrix[-1][j] == "1" else 0
            maksimEdge = max(maksimEdge,dp[-1][j])
        for i in range(len(matrix)):
            dp[i][-1] = 1 if matrix[i][j] == "1" else 0
            maksimEdge = max(maksimEdge,dp[i][-1])
        for i in range(len(matrix)-2,-1,-1):
            for j in range(len(matrix[0])-2,-1,-1):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    dp[i][j] = min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1]) + 1 if matrix[i][j+1] == "1" and matrix[i+1][j] == "1" and matrix[i+1][j+1] == "1" else dp[i][j]
                    maksimEdge = max(maksimEdge,dp[i][j])
        return maksimEdge**2

matrix = [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]

ans = Solution()
print(ans.maximalSquare(matrix))