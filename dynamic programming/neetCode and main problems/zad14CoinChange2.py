# You are given an integer array coins representing 
# coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.


# Example 1:

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:

# Input: amount = 10, coins = [10]
# Output: 1

class Solution:
    def change(self, amount: int, coins) -> int:
        #O(n*m) - memory & time complexity
        dp = [[0] * (len(coins)+1) for i in range(amount +1)]
        dp[0] = [1] * (len(coins)+1)

        for a in range(1,amount+1):
            for i in range(len(coins)-1,-1,-1):
                dp[a][i] = dp[a][i+1]
                if a - coins[i] >=0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]
    
    
    #O(n) space complexity:
    def change2(self, amount: int, coins) -> int:
        #O(n) memory &  O(n*m) time complexity
        dp = [0] * (amount +1)
        dp[0] = 1 # gdy amount = 0 to jest 1 mozliwosc uzyskania takiej kombinacji

        for i in range(len(coins)-1,-1,-1):
            nextDP = [0]*(amount+1)
            nextDP[0] = 1 # gdy amount = 0 to jest 1 mozliwosc uzyskania takiej kombinacji

            for a in range(1,amount+1):
                nextDP[a] = dp[a] #bierzemy pod uwagę pozostale monety bez uwzgledniania naszej aktualnej!
                if a - coins[i] >=0:
                    nextDP[a] += nextDP[a - coins[i]] #bierzemy pod uwage sumowanie do wartosci pod indeksem a - coins[i]  
            dp = nextDP
        return dp[amount]