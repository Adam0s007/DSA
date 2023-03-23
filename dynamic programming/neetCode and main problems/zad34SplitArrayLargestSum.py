# Given an array nums which consists of non-negative integers and an integer m, 
# you can split the array into m non-empty continuous subarrays.

# Write an algorithm to minimize the largest sum among these m subarrays.

# Example 1:
# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
# Example 3:

# Input: nums = [1,4,4], m = 3
# Output: 4



class Solution:
    def splitArray(self, nums, m) -> int: #uwaga! Jest to painter partition problem!
        #solution (n^2*m)
        dp = [[0 for i in range(m+1)] for j in range(len(nums))]
        def dfs(i,m): # i - idziemy od itego elementu wykorzystując jeszcze m podtablic
            if m == 1: #jesli mamy jeden zbior (podliste) do wykorzystania no to sumujemy do samego konca od i'tego indeksu!
                return sum(nums[i:])
            if dp[i][m]: return dp[i][m]
            
            res, curSum = float("inf"), 0
            for  j in range(i,len(nums)-m +1): #mając jeszcze do wykorzystania m podlist, to aktualna podlista moze sięgać do len(nums)-m'tego indeksu! 
                curSum += nums[j]
                maxSum = max(curSum,dfs(j+1,m-1)) #albo bierzemy sumę aktualną, albo tworzymy przedzial, i rozpatrujemy kolejny
                #powyzsza forumla: do aktualnej podlisty podrzucamy nums[j] ALBO robimy nową podliste!
                res = min(res,maxSum)
                if curSum > res: break #jesli aktualna suma jest juz wieksza od minimalnej w res to breakujemy
            dp[i][m] = res
            return res
        return dfs(0,m)