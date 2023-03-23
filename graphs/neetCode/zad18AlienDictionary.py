# There is a new alien language which uses the latin alphabet. 
# However, the order among letters are unknown to you. 
# You receive a list of non-empty words from the dictionary, 
# where words are sorted lexicographically by the rules of this new language. 
# Derive the order of letters in this language.


# You may assume all letters are in lowercase.
# The dictionary is invalid, if string a is prefix of string b and b is appear before a.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return the smallest in normal lexicographical order.
# The letters in one string are of the same rank by default and are sorted in Human dictionary order.
# Example
# Example 1:

# Input：["wrt","wrf","er","ett","rftt"]
# Output："wertf"
# Explanation：
# from "wrt"and"wrf" ,we can get 't'<'f'
# from "wrt"and"er" ,we can get 'w'<'e'
# from "er"and"ett" ,we can get 'r'<'t'
# from "ett"and"rftt" ,we can get 'e'<'r'
# So return "wertf"
# Example 2:

# Input：["z","x"]
# Output："zx"
# Explanation：
# from "z" and "x"，we can get 'z' < 'x'
# So return "zx"


from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w}
        
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
            
        visit = {} #false=visited, true=current path
        res = []
        def dfs(c):
            if c in visit: #loop
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei): return True
                    
            visit[c] = False
            res.append(c)
            
        for c in adj:
            if dfs(c): return ""
        res.reverse()
        return "".join(res)
