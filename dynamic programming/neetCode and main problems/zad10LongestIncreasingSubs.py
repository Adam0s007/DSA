# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or 
# no elements without changing the order of the remaining elements. For example, 
# [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

class Solution:
    def lengthOfLIS(self, nums) -> int:
        LIS = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i],1+ LIS[j])
        return max(LIS)
#     indexes = [0 ,1,2,3,4,5, 6 , 7]
# Input: nums = [10,9,2,5,3,7,101,18]
#          dp = [1 ,1,1,2,2,3, 4 , 4]



# We have already discussed an O(n2) time complexity solution of LIS here, which uses dynamic programming. In this post, an O(n.log(n)) time, non-DP solution, is discussed.

 
# Let S[i] be defined as the smallest integer that ends an increasing sequence of length i. Now iterate through every integer X of the input set and do the following:

# If X is more than the last element in S, then append X at the end of S. This essentially means we have found a new largest LIS.
# Otherwise, find the smallest element in S, which is more than or equal to X, and replace it with X. Because S is sorted at any time, the element can be found using binary search in log(N) time.
# Let’s illustrate this with the help of an example. Following are the steps followed by the algorithm for an integer array {2, 6, 3, 4, 1, 2, 9, 5, 8}:

# Initialize to an empty set S = {}
# Inserting 2 —- S = {2} – New largest LIS
# Inserting 6 —- S = {2, 6} – New largest LIS
# Inserting 3 —- S = {2, 3} – Replaced 6 with 3
# Inserting 4 —- S = {2, 3, 4} – New largest LIS
# Inserting 1 —- S = {1, 3, 4} – Replaced 2 with 1
# Inserting 2 —- S = {1, 2, 4} – Replaced 3 with 2
# Inserting 9 —- S = {1, 2, 4, 9} – New largest LIS
# Inserting 5 —- S = {1, 2, 4, 5} – Replaced 9 with 5
# Inserting 8 —- S = {1, 2, 4, 5, 8} – New largest LIS

# So, the length of the LIS is 5 (the size of S). 
# Please note that here S[i] is defined as the smallest integer 
# that ends an increasing sequence of length i. Therefore, S does not represent an actual sequence,
#  but S’s size represents the LIS length.

# dlugosc tablicy S jest rozwiazaniem natomiast jej liczby nie są!!!
class Solution:
    #tutaj sprawdzamy najmniejszy element dla targeta (wiekszy lub rowny jemu)
    def binarySearchCeil(self,res, target):
        r = len(res)-1
        l = 0
        while l <= r:
            if l == r: return l
            m = (r - l) // 2 + l
            if res[m] == target: return m
            elif res[m] < target: l = m + 1   
            else: r = m
    
    def lengthOfLIS(self, nums) -> int:
        ans = [nums.pop(0)]         # use this list to track increasing
        for num in nums:            # add current number into the list
            if num > ans[-1]:
                ans.append(num)
            else: # w przeciwnym wypadku szukamy  pozycję najmniejszego elementu, ktory jest wiekszy lub rowny targetowi i tam zmieniamy na target
                ans[self.binarySearchCeil(ans, num)] = num    
        return len(ans)
