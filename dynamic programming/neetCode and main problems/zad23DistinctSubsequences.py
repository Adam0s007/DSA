# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# A string's subsequence is a new string formed from the original string by deleting some 
# (can be none) of the characters without disturbing the remaining characters' relative positions. 
# (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# The test cases are generated so that the answer fits on a 32-bit signed integer.

# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# rabbbit
# rabbbit
# rabbbit
# Example 2:

# Input: s = "babgbag", t = "bag"
# Output: 5
# there are 5 ways you can generate "bag" from S.


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        n = len(s)
        dp = [[0 for i in range(m+1)] for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 1    

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1] == t[j-1]: #poniewaz w tablicy dp zerowe indeksy są zarezerowwane dla "" a reszta to stringi!
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][m]
ans = Solution()
print(ans.numDistinct("ba","b"))


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        for i in range(len(s)+1):
            dp[(i,0)] = 1
        for j in range(1,len(t)+1):
            dp[(0,j)] = 0
            
        def dfs(i,j):
            if (i,j) in dp: return dp[(i,j)]
            
            ans = dfs(i-1,j)
            if s[i-1] == t[j-1]: ans += dfs(i-1,j-1)
            dp[(i,j)] = ans
            return dp[(i,j)]
        
        return dfs(len(s),len(t))