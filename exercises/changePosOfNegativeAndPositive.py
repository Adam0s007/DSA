# Given an array of positive and negative integers, segregate them in linear time and constant space. 
# The output should print all negative numbers, followed by all positive numbers.
# For example,
# Input:  [9, -3, 5, -2, -8, -6, 1, 3]
# Output: [-3, -2, -8, -6, 5, 9, 1, 3]

def swap(a, i, j):
 
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
 
 
def partition(a):
    pIndex = 0

    # each time we find a negative number, `pIndex` is incremented,
    # and that element would be placed before the pivot
    for i in range(len(a)):
        if a[i] < 0:        # pivot is 0
            swap(a, i, pIndex)
            pIndex = pIndex + 1



a = [9, -3, 5, -2, -8, -6, 1, 3]
partition(a)
print(a)

