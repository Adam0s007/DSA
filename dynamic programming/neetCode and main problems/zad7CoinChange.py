# 322. Coin Change
# Medium

# 10692

# 261

# Add to List

# Share
# You are given an integer array coins representing coins of different denominations and an integer amount 
# representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.


# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

class Solution:
    #O(amount * len(coins) )
    def coinChange(self, coins, amount: int) -> int:
        dp = [amount + 1]*(amount+1)
        dp[0] = 0 #dp[k] = m => minimum "m" number of coins to get to "k"
        
        for a in range(1,amount+1):
            for c in coins:
                if a - c >=0: #for exampe a == 7 & c == 3: dp[7-3] == dp[4] (in dp[4] we contains minim nr of coins to get to 4) but we have to add 1 coin "c" == 3 to get to 7!!
                    dp[a] = min(dp[a],1+ dp[a-c])  #1 + dp[a-c] because we are using dp[a-c] coins and coin "c" in addition! so "dp[a-c] + 1" coins
        return dp[amount] if dp[amount] != amount + 1 else -1

ans = Solution()
c = [1,2,3,4]
print(ans.coinChange(c,12))
