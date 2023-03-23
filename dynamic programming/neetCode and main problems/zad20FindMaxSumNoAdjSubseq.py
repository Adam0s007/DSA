# Find the maximum sum of a subsequence with no adjacent elements
# Given an integer array, find the maximum sum of subsequence where the subsequence contains no element at adjacent positions.

# Please note that the problem specifically targets subsequences that need not be contiguous, i.e., subsequences are not required to occupy consecutive positions within the original sequences.

 
# For example,

# Input:  { 1, 2, 9, 4, 5, 0, 4, 11, 6 }
# Output: The maximum sum is 26
 
# The maximum sum is formed by subsequence { 1, 9, 5, 11 }


# Constant space DP-solution to calculate the maximum sum in a given
# list with no adjacent elements considered
def findMaxSumSubsequence(nums):
    # base case
    if not nums: return 0
 
    # base case
    if len(nums) == 1: return nums[0]
 
    # store maximum sum until index `i-2`
    prevOfPrev = nums[0]
    # stores maximum sum until index `i-1`
    prev = max(nums[0], nums[1])
 
    # start from index 2
    for i in range(2, len(nums)):
        prev,prevOfPrev = max(nums[i], max(prev, prevOfPrev + nums[i])),prev #for negative nums: max(nums[i],max(...))
    # return maximum sum
    return prev
 
 
if __name__ == '__main__':
 
    nums = [1, 2, 9, 4, 5, 0, 4, 11, 6]
    print('The maximum sum is', findMaxSumSubsequence(nums))