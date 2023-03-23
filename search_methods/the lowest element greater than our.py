def ceilIndex(A,l,r,key): #binary search - wyszukaj najmniejszy element ktory jest wiekszy od rozpatrywanego!!!! 
    while (r-l > 1 ):
        m = l + (r-l) // 2
        if A[m] >= key:
            r = m
        else:
            l = m
    return r



# three Binary search function to find the index of the smallest number in result that is greater than or equal to the target

def binarySearchCeil(res, target):
# If the left and right pointers meet, we have found the smallest number that is greater than the target
    r = len(res)-1
    l = 0
    while l <= r:
        if l == r: return l
        # Find the mid pointer
        m = (r - l) // 2 + l
        # If the number at the mid pointer is equal to the target, we have found a number that is equal to the target
        if res[m] == target: return m
        # Else if the number at the mid poitner is less than the target, we search the right side
        elif res[m] < target: l = m + 1   
        # Else, we search the left side including the number at mid pointer because it is one of the possible solution since it is greater than the target
        else: r = m


#better and simpler solution!
def searchInsert(nums,target) -> int:
    
    if target > nums[-1]: return len(nums)-1 #tu wyjatek
    elif target < nums[0]: return 0
    l,r = 0,len(nums)-1
    res = 0
    while l <= r:
        m = (l+r)//2
        if nums[m] >= target:
            res = m
            r = m - 1
        else:
            l = m + 1
    return res
    
def fasterBinarySeachCeil(nums,target):
    l,r = 0,len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] > target:
            r = m - 1
        elif nums[m] == target: return m
        else:
            l = m + 1
    return l




