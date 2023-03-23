# You are given an integer array nums. 
# You want to maximize the number of points you get by 
# performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

# Example 1:

# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# Example 2:

# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.


class Solution:
    def deleteAndEarn(self, nums) -> int:
        nums.sort()
        ans = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                ans.append(nums[i])
        
        dp = [0 for i in range(nums[-1]+1)]
        for elem in nums: dp[elem] +=1

        prevP = ans[0]*dp[ans[0]]
        if len(ans) < 2: return prevP
        prev = max(ans[0]*dp[ans[0]], ans[1]*dp[ans[1]]) if ans[1] - ans[0] == 1 else ans[0]*dp[ans[0]] + ans[1]*dp[ans[1]]

        for i in range(2,len(ans)):
            if ans[i] - ans[i-1] == 1:
                prev,prevP = max(prevP + ans[i]*dp[ans[i]], prev), prev
            else:
                prevP = prev
                prev +=  ans[i]*dp[ans[i]]
        return prev

    def deleteAndEarn(self, nums) -> int: #simpler and more optimal solution
        max_val = max(nums)
        dp = [0] * ( max_val + 1 )
        for i in nums :
            dp[i] += i
        for i in range(2,len(dp)):
            dp[i] = max(dp[i-1],dp[i] + dp[i-2])
            
        return dp[max_val]
        

