# Python3 program to sort an array
# using bucket sort
def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up    
    return b    


       
def bucketSort(x):
    arr = []
    slot_num = 10 # 10 means 10 slots, each
                  # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])
         
    # Put array elements in different buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)
     
    # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])
         
    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x
 
#another version



def Insertion(T):
    n = len(T)
    j = n-2
    x = T[n-1]
    while j >= 0 and T[j] > x:
        T[j+1] = T[j]
        j -= 1
    T[j+1] = x
def bucketsort(T):
    n = len(T)
    highest = max(T)
    Bucket_arr = [[] for _ in range(n)]
    for i in range(n):
        indeks = int((T[i]/highest)*n)
        if indeks == n: indeks -= 1
        Bucket_arr[indeks].append(T[i])
        Insertion(Bucket_arr[indeks])
    iter = 0
    for i in range(len(Bucket_arr)):
        for elem in Bucket_arr[i]:
            T[iter] = elem
            iter +=1
    return T
# Driver Code
# x = [0.897, 0.565, 0.656,
#      0.1234, 0.665, 0.3434]
# print("Sorted Array is")
# print(bucketSort(x))
 
# This code is contributed by
# Oneil Hsiao

def insertionSort(A):
    for i in range(1,len(A)):
        curr = A[i]
        j = i-1
        while j>=0 and curr < A[j]:
            A[j+1] = A[j]
            j-=1
        A[j+1] = A[j]


def betterBucketSort(T):
    if not T: return None
    maks = max(T)
    minim = min(T)
    ranges = len(T)
    buckets = [[] for _ in range(ranges)]

    r = (maks-minim)/ranges
    if r == 0: return T
    for elem in T:
        index = int((elem - minim)/r)
        if index == ranges: index -=1
        buckets[index].append(elem)
    print(buckets)
    for i in range(ranges):
        if buckets[i]: insertionSort(buckets[i])
                        #we can also use mergeSort because  this is stable sort!
    k=0
    for i in range(ranges):
        for j in range(len(buckets[i])):
            T[k] = buckets[i][j]
            k+=1
    return T

from random import randint
t = [float(randint(-100,100)) for i in range(10)]
T  = [3,7,8,2,5,2,1,9,4]
betterBucketSort(T)
betterBucketSort(t)
print(t)
