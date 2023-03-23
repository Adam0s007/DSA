
class Solution():
    def canPartition(self, nums):
        suma = sum(nums)
        if suma % 2 != 0: return False
        dp = [False for _ in range(suma + 1)]
        dp[0] = True
        for i in range(len(nums)):
            for j in range(len(dp) - 1, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
            if dp[suma//2]: return True
        return  dp[(suma) // 2]