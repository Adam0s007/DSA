# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint
#  stopping you from robbing each of them is that adjacent houses 
# have security systems connected and it will automatically contact 
# the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.


class Solution:
    def rob(self, nums):
        rob1,rob2 = 0,0
        
        #[rob1,rob2,n,n+1,...] 
        for elem in nums:
            rob2,rob1 = max(elem + rob1,rob2),rob2
        return rob2
    def rob(self,nums):
        if len(nums) < 2:
            return nums[0]
        prevPrev = nums[0]
        prev = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            prev,prevPrev = max(nums[i] + prevPrev, prev),prev
        return prev

ans = Solution()
t = [1,2,3,1]
print(ans.rob(t))