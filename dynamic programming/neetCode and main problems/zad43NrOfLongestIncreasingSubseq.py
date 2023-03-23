# Given an integer array nums, return the number of longest increasing subsequences.
# Notice that the sequence has to be strictly increasing.

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

class Solution:
    def findNumberOfLIS(self, nums) -> int:
        dp = [[1,1] for i in range(len(nums))]
        lenLIS,res =0,0
        for i in range(len(nums)-1,-1,-1):
            maxLen,maxCnt = 1,1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    length,count = dp[j]
                    if length + 1 > maxLen:
                        maxLen,maxCnt = length+1,count
                    elif length + 1 == maxLen:
                        maxCnt += count
            if maxLen > lenLIS:
                lenLIS,res = maxLen,maxCnt
            elif maxLen == lenLIS:
                res += maxCnt
            dp[i] = [maxLen,maxCnt]
        return res