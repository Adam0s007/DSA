from random import randint
def quicksort_rek(T,left,right):
    i = left
    j = right
    pivot =T[(left+right)//2]
    while i <= j:
        while T[i] < pivot:
            i+=1
        while T[j] > pivot:
            j-=1
        if i<=j:
            T[j], T[i] = T[i], T[j]
            i+=1
            j-=1 
    if left < j:
        quicksort_rek(T,left,j) 
    if i < right:
        quicksort_rek(T,i,right)  





def quicksort(T): #O(nlogn)
    stos = []
    stos.append((0,len(T)-1)) #na stos juz trzeba coś wlozyc
    while stos: #dopoki stos cokolwiek zawiera
        left,right = stos.pop()
        i = left
        j = right
        #powtorka kodu z quicksort_rek:
        pivot = T[(left+right)//2]
        while i <= j:
            while T[i] < pivot:
                i+=1
            while T[j] > pivot:
                j-=1
            if i<=j:
                T[j], T[i] = T[i], T[j]
                i+=1
                j-=1
        if left < j: #tutaj ponizej zmieniamy:
            stos.append((left,j))
        if i < right: #tutaj ponizej zmieniamy:
            stos.append((i,right))  

# from random import randint
# A = [randint(0,100000) for i in range(4000000)]
# quicksort(A)    


def quicksort2(A):
    stos = []
    stos.append((0,len(A)-1))
    while len(stos) > 0:
        l,r = stos.pop()
        if l < r:
            p = partition(A,l,r)
            stos.append((l,p-1))
            stos.append((p+1,r))

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
    A[pivotIndex], A[low] = A[low], A[pivotIndex] 
    border = low
    for i in range(low,high+1):
        if A[i] < pivotValue:
            border+=1
            A[i],A[border]  = A[border],A[i]
    A[low],A[border] = A[border],A[low]
    return (border)

def quicksort3(A):
    stos = []
    stos.append((0,len(A)-1))
    while len(stos) > 0:
        l,r = stos.pop()
        while l < r:
            p = partition(A,l,r)
            stos.append((l,p-1))
            l = p +1

def quicksort4(A):
    tailRecursiveQS(A,0,len(A)-1)
def tailRecursiveQS(arr,start,end):
    while start < end:
        pivot = partition(arr,start,end)
        if pivot - start < end - pivot:
            tailRecursiveQS(arr,start,pivot - 1)
            start = pivot + 1
        else:
            tailRecursiveQS(arr,pivot+1,end)
            end = pivot - 1

t = [1,7,8,5,32,5,7,8,7,4,32,2]
quicksort2(t)
print(t)
   



def insertionsort(A,start,end):
    for i in range(start+1,end+1):
        curNum = A[i]
        j = i-1
        while j>=start and curNum < A[j]:
            A[j+1] = A[j]
            j-=1    
        A[j+1] = curNum         


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
 
# Partition using Hoare's Partitioning scheme
def partition(a, low, high):
    pivot = a[low]
    (i, j) = (low - 1, high + 1)
    while True:
        while True:
            i = i + 1
            if a[i] >= pivot:
                break
        while True:
            j = j - 1
            if a[j] <= pivot:
                break
        if i >= j:
            return j
        swap(a, i, j)
 
def quicksort5(arr):
    return quicksort_h(arr,0,len(arr)-1)

def quicksort_h(a, low, high):
    if low >= high:
        return
    pivot = partition(a, low, high)
    quicksort_h(a, low, pivot)
    quicksort_h(a, pivot + 1, high)
 
 
# quick selection algorithm
def qSelect(l,r,nums,k):
    pivot, p = nums[r],l
    for i in range(l,r):
        if nums[i] <= pivot: #weakly ascending order preserved
            nums[p], nums[i] = nums[i], nums[p]
            p+=1
    nums[p], nums[r] = nums[r], nums[p]
    if p > k: return qSelect(l, p-1,nums,k)
    elif p < k: return qSelect(p+1,r,nums,k)
    else: return nums[p]





def quickSelect(tab,k):
    def qSelect(l,r,k):
        pivot,p = tab[r],l
        for i in range(l,r):
            if tab[i] <= pivot: #p informuje o ilosci elementow <= od pivota
                tab[i],tab[p] = tab[p],tab[i]
                p+=1
        tab[p],tab[r] = tab[r],tab[p]
        if p > k: return qSelect(l,p-1,k)
        elif p < k: return qSelect(p+1,r,k)
        else: return tab[p]
    return qSelect(0,len(tab)-1,k)

tab = [10,16,8,12,15,6,3,9,5]
# tab = [randint(1,50) for _ in range(1000000)]

#     [3,5,6,8,9,10,12,15,16]
for i in range(len(tab)):
    print(quickSelect(tab,i))