# Dana jest nieskonczona tablica A, gdzie pierwsze n pozycji zawiera posortowane
# liczby naturalne, a reszta tablicy ma wartosci None. Nie jest dana wartosc n.
# Przedstaw algorytm, ktory dla danej liczby naturalnej x znajdzie indeks w tablicy,
# pod ktorym znajduje sie wartosc x. Jesli nie ma jej w tablicy, to zwrocic None.

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

def insertionSort(Arr,left,right):
    for i in range(left+1,right+1):
        currNum = Arr[i]
        j = i-1
        while j >= left and currNum < Arr[j]:
            Arr[j+1] = Arr[j]
            j-=1
        Arr[j+1] = currNum
    return Arr


def BS(arr,edge,x):
    l,r = 0,edge
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == x: return mid
        elif arr[mid] > x: r = mid - 1
        else: l = mid + 1
    return None


def infinityTableBS(arr,x):
    #looking for edge!
    left = 0
    if arr[left] and arr[left+1] == None: return BS(arr,left,x)
    right = 1
    edge = None
    while arr[right]:
        right *=2
    #now arr[right] is None for sure, so we are looking for edge!
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == None:
            if arr[mid-1]: 
                edge = mid-1
                break
            else:
                right = mid - 1
        elif arr[mid]:
            if arr[mid+1] == None:
                edge = mid
                break
            else:
                left = mid + 1
    return BS(arr,edge,x)



t = [1,2]
T = [None]*100000
t.extend(T)
print(infinityTableBS(t,1))
     
        
        



