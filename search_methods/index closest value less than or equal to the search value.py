def binary_search(array, target,start_index):
    """
    Binary search for the closest value less than or equal to the search value
    :param array: The given sorted list
    :param target: Value to be found in the array
    :param startIndex: Initialized with 0
    :param endIndex: Initialized with 2**32
    :return: Returns the index closest value less than or equal to the search value
    """
    left = 0
    right = len(array)

    while left < right:
        mid = (left + right) // 2
        if array[mid] < target + 1:
            left = mid + 1
        else:
            right = mid         
    # if we want always lower value => without that while we have lower or equal value
    # while left-1 >=0 and array[left-1] == array[start_index]:
    #     left -=1
    return left - 1


#SIMPLER!
#binary search #pos of highest value lower or equal to our target!!!
def binarySearchFloor(values,target):
        l,r = 0,len(values)-1
        res = -1
        while l <= r:
            m = (l+r)//2
            if values[m] <= target:
                res = m
                l = m + 1  
            else:
                r = m - 1
        return res

T = [1,2,4,4,4,5,6,7,12,13,15,16,21,25,24]
for i in range(max(T)):
    print(binary_search(T,i,0),end=", ")
print()

for i in range(max(T)):
    print(binarySearchFloor(T,i),end=", ")
