# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb

class Solution: # O(n^2)
    def longestPalindrome(self, str:str)->str:
        pal = ""
        for i in range(len(str)):
            l,r = i,i #odd lengths
            found = self.findpal(str,l,r)
            if len(pal) <len(found):
                pal = found
            l,r = i,i+1 #even lengths
            found = self.findpal(str,l,r)
            if len(pal) <len(found):
                pal = found
        return pal
    def findpal(self,s,l,r):
        ls = len(s)
        while l>=0 and r<ls and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]