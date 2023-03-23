# Given an array of distinct integers nums and a target integer target, 
# return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:

# Input: nums = [9], target = 3
# Output: 0

class Solution:
    def combinationSum4(self, nums, target) -> int: #rozni sie od coin change 2 tym, że tu rozne ulozenia tych samych rzeczy dają rozne efekty
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for i in range(1,target+1):
            print(dp)
            for elem in nums:
                if i - elem >= 0:
                    dp[i] += dp[i-elem]
        return dp[target]
ans = Solution()
nums = [1,2]
print(ans.combinationSum4(nums,4))