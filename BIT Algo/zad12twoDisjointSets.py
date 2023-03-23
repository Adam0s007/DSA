# Dane sa dwa zbiory liczb, reprezentowane jako tablice rozmiarow m i n, gdzie m jest znacznie mniejsze od n.
# Zaproponuj algorytm, ktory sprawdzi, czy zbiory są rozlączne.

#1. rozwiazanie O(mlogm + nlogm):
#posortować mniejszą tablicę, i dla kazdego elementu w drugiej tablicy
#sprawdzac szukaniem binarnym czy istnieje wartosc w drugiej tablicy!


def quicksort(A):
    stack = [(0,len(A)-1)]
    while len(stack):
        left,right = stack.pop()
        pivot = A[(left+right)//2]
        l,r = left,right
        while l <= r:
            while A[l] < pivot: l+=1
            while A[r] > pivot: r-=1
            if l <=r:
                A[r],A[l] = A[l],A[r]
                r-=1
                l+=1
        if left < r:
            if r - left  > 20:
                stack.append((left,r))
            else:
                insertionSort(A,left,r)

        if l < right:
            if right - l  > 20:
                stack.append((l,right))
            else:
                insertionSort(A,l,right)

# A = [7,3,1,5,8,9,6,3,1,4,6]
# quicksort(A)
# print(A)

#for data set to 20 elements:
def insertionSort(Arr,left,right):
    for i in range(left+1,right+1):
        currNum = Arr[i]
        j = i-1
        while j >= left and currNum < Arr[j]:
            Arr[j+1] = Arr[j]
            j-=1
        Arr[j+1] = currNum
    return Arr

#to 10 000 elems and max value not greater than m
def countingSort(arr, RANGE): #stable!!
    n = len(arr)
    output = [0] * (n)
    count = [0] * (RANGE+1)
    for i in range(0, n):
        count[arr[i]] += 1
    for i in range(1,RANGE+1):
        count[i] += count[i - 1] 
    for i in range(n-1,-1,-1): 
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    for i in range(0, len(arr)):
        arr[i] = output[i]

# from random import randint
# A = [randint(0,100000) for i in range(4000000)]
# quicksort(A)



def binarySearch(T,elem):
    l,r = 0,len(T)-1
    while l <= r:
        mid = (l+r)//2
        if T[mid] == elem:
            return True
        elif T[mid] < elem:
            l = mid+1
        else:
            r = mid -1
    return False
a = [1,3,5,6,7,9,9,14]
print(binarySearch(a,4))
def check_disconnected(arrN,arrM):
    n = len(arrN)
    m = len(arrM)
    k = max(arrM)
    if m > 10000 or k > m:
        quicksort(arrM)
    else:
        countingSort(arrM,k)

    for elem in arrN:
        if binarySearch(arrM,elem):
            return False
    return True

    
