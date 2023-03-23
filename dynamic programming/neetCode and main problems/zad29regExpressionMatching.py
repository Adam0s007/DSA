# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0 for i in range(len(p)+1)] for j in range(len(p)+1)]
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if (j + 1) < len(p) and p[j + 1] == '*':
                cache[(i, j)] = (dfs(i, j+2) or (match and dfs(i + 1, j)))
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return cache[(i, j)]
        
        return dfs(0, 0)
#another solution:
class Solution:
    def isMatch(self, text, pattern):
        len_t = len(text)
        len_p = len(pattern)
        # create 2 d array to store result in boolean form
        # M[i][j] is true if text[:i] matches pattern[:j] else false
        M = [[False]*(len_p+1) for i in range(len_t+1)]

        # empty string matches empty pattern, hence true
        M[0][0] = True

        # if pattern has pattern = "d*" and text = "" then compute the result for first row
        for j in range(1,len_p+1):
            if pattern[j-1] == "*" and j > 1:
                M[0][j] = M[0][j-2]

        # construct DP based on previous values
        for i in range(1, len_t+1):
            for j in range(1, len_p+1):
                # if there is a char match or pattern has '.' then skip matching char and copy result
                if pattern[j-1] == "." or text[i-1] == pattern[j-1]:
                    M[i][j] = M[i-1][j-1]
                elif pattern[j-1] == "*":  # if char is '*' then
                    if pattern[j-2] == "." or text[i-1] == pattern[j-2]:
                        # no occurance or one occurance or multiple occurance
                        M[i][j] = M[i][j-1] or M[i-1][j] or M[i][j-2]
                    else:
                        M[i][j] = M[i][j-2]  # no occurence
        for k in range(len(M)):
            print(M[k])

        return M[-1][-1]

ans = Solution()
ans.isMatch("aab","c*a*b")