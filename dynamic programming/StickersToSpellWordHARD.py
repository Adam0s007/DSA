# We are given n different types of stickers. Each sticker has a lowercase English word on it.

# You would like to spell out the given string target by cutting individual
#  letters from your collection of stickers and rearranging them. 
# You can use each sticker more than once if you want, and you have infinite quantities of each sticker.
# Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.
# Note: In all test cases, all words were chosen randomly from the 1000 
# most common US English words, and target was chosen as a concatenation of two random words.

# Example 1:

# Input: stickers = ["with","example","science"], target = "thehat"
# Output: 3
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the target "thehat".
# Also, this is the minimum number of stickers necessary to form the target string.
# Example 2:

# Input: stickers = ["notice","possible"], target = "basicbasic"
# Output: -1
# Explanation:
# We cannot form the target "basicbasic" from cutting letters from the given stickers.


class Solution:
    def minStickers(self, stickers, target) -> int:
        stickerCount = []
        for i, s in enumerate(stickers):
            stickerCount.append({})
            for c in s:
                stickerCount[i][c] = 1 + stickerCount[i].get(c, 0)
        
        dp = {}
        def dfs(t, stick):
            if t in dp:
                return dp[t]
            res = 1 if stick else 0
            remainT = ""
            for c in t:
                if c in stick and stick[c] > 0:
                    stick[c] -= 1
                else:
                    remainT += c
            used = float("inf")
            if remainT:
                for s in stickerCount:
                    if remainT[0] not in s:
                        continue
                    used = min(used, dfs(remainT, s.copy()))
                res += used
                dp[remainT] = used
            return res
                    
            
        res = dfs(target, {})
        return res if res != float("inf") else -1