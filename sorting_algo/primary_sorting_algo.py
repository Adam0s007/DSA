

def bubblesort(myList):
    for i in range(len(myList)-1):
        flag = 1
        for j in range(0, len(myList) - i - 1):
            if myList[j] > myList[j+1]:
                flag = 0
                myList[j],myList[j+1] = myList[j+1],myList[j]
        if flag == 1:
            return myList
    return myList


def selectionsort(A):
    for i in range(len(A)-1):
        minInd = i
        for j in range(i+1,len(A)):
            if A[j] < A[minInd]:
                minInd = j
        if minInd != i:
            A[i],A[minInd] = A[minInd],A[i]
    return A

def insertionsort(A):
    for i in range(1,len(A)):
        curNum = A[i]
        j = i-1
        while j>=0 and curNum < A[j]:
            A[j+1] = A[j]
            j-=1    
        A[j+1] = curNum         
    return A
print(insertionsort([1,2,3,4]))

#quicksort

def quick_sort(A):
    quick_sort2(A,0,len(A)-1)

def quick_sort2(A,low,high):
    if low < high:
        p = partition(A,low,high)
        quick_sort2(A,low,p-1)
        quick_sort2(A,p+1,high)

def get_pivot(A,low,high):
    mid = (high + low)//2
    pivot =  high
    if A[low] < A[mid]:
        if A[mid] < A[high]:
            pivot = mid
    elif A[low] < A[high]:
        pivot = low
    return pivot

def partition(A,low,high):
    pivotIndex = get_pivot(A,low,high)
    pivotValue = A[pivotIndex]
    #changing arr element with pivot index with A[low]
    A[pivotIndex], A[low] = A[low], A[pivotIndex] 
    #helping variable = low
    border = low
#iterowanie od low do high wlacznie (petla wykona sie do high)
    for i in range(low,high+1):
        if A[i] < pivotValue:
            border+=1
            A[i],A[border]  = A[border],A[i]
    A[low],A[border] = A[border],A[low]
    return (border)


T = [1,5,6,7,4,3,5,6,8,0,8,6,4,2,2,4,6,7843,32,6,5,5,2,393,39,222]
quick_sort(T)
print(T)

