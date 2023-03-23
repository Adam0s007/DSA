# You are given n balloons, indexed from 0 to n - 1. 
# Each balloon is painted with a number on it represented by an array nums.
#  You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
# If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

 

# Example 1:

# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# Example 2:

# Input: nums = [1,5]
# Output: 10

class Solution():
    def maxCoins(self, nums):
        nums = [1] + nums + [1]  # add the dummy head and tail, both are left till end and DO NOT burst them.
        dp = [[0] * len(nums) for _ in nums]  
        def search(l, r):
            if r - l < 2: return 0
            if dp[l][r] > 0: return dp[l][r] 
            for k in range(l + 1, r):
                dp[l][r] = max(dp[l][r], search(l, k) + search(k, r) + nums[l] * nums[k] * nums[r])
            return dp[l][r]
        return search(0, len(nums) - 1)

#better solution
class Solution:
    def maxCoins(self, nums):
        nums, N = [1] + nums + [1], len(nums) + 2 #array with 1,1 balloons at the end and length as N
        dp = [[0] * N for _ in range(N)] # table full of zeros
        
        for left in range(N - 3, -1, -1):
            for right in range(left + 2, N):
                dp[left][right] = max(nums[left]*nums[i]*nums[right] + dp[left][i] + dp[i][right] for i in range(left + 1, right))
        
        return dp[0][N-1]