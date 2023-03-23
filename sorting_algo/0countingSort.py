
'''
 `A` ——> the input list of integers to be sorted
 `k` ——> a number such that all integers are in range `0…k-1`
'''
 #time complecixty: O(n+k)
 #memory complexity: O(n+k)
def countsort(A, k):
    # create an integer list of size `n` to store the sorted list
    output = [0] * len(A)
    # create an integer list of size `k + 1`, initialized by all zero
    freq = [0] * (k + 1)
    # using the value of each item in the input list as an index,
    # store each integer's count in `freq[]`
    for n in A:
        freq[n] = freq[n] + 1

    # calculate the starting index for each integer
    total = 0
    
    for i in range(k + 1):
        oldCount = freq[i]
        freq[i] = total
        total += oldCount
    
    # copy to the output list, preserving the order of inputs with equal keys
    for i in A:
        output[freq[i]] = i 
        freq[i] = freq[i] + 1 #aby w to samo miejsce nie przypisac nowej wartosci!
    # copy the output list back to the input list
    for i in range(len(A)):
        A[i] = output[i]
 

 

RANGE = 100
# without new array!
def customSort(A):
    freq = [0] * (RANGE+1)
    for i in A:
        freq[i] = freq[i] + 1
    k = 0
    for i in range(RANGE):
        while freq[i] > 0:
            A[k] = i
            freq[i] = freq[i] - 1
            k = k + 1


def countingSort(arr, RANGE): #stable!!
    n = len(arr)
    # The output array elements that will have sorted arr
    output = [0] * (n) 
    # initialize count array as 0
    count = [0] * (RANGE+1)
    # Store count of occurrences in count[]
    for i in range(0, n):
        count[arr[i]] += 1
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1,RANGE+1):
        count[i] += count[i - 1]
    # Build the output array
    for i in range(n-1,-1,-1): #dzieki przejsciu od tylu mamy sortowanie stabilne!
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    for i in range(0, len(arr)):
        arr[i] = output[i]


from random import randint
A = [randint(1,100) for i in range(1000)]
#customSort(A)
#A = [randint(1,100) for i in range(1000000)]
countingSort(A,100)
print(A)

