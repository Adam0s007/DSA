# Dana jest tablica A oraz liczba k. Znaleźć liczbę 
# różnych par elementów z tablicy A o różnicy równej k. 
# Np. Dla tablicy [7,11,3,7,3,9,5] oraz k = 4, odpowiedź to 3

#[3,3,5,7,7,9,11], k = 4:   3 - 3 < 4,
#[3,5,7,9,11], k =4 : 
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

def removeDuplicates(A):
    quicksort(A)
    l  = 1
    for r in range(1,len(A)):
        if A[r] != A[r-1]:
            A[l] = A[r]
            l+=1
    return l #nr of elements in A without duplicates!
def amount_of_things(A,k):
    leng = removeDuplicates(A)
    wsk1 =0
    wsk2 = 1
    counter = 0
    while wsk1 < leng:
        if A[wsk2] - A[wsk1] == k:
            counter+=1
            if wsk2 < leng: wsk2+=1 
            else: break #jesli przesunelibysmy wsk1 dalej, to otrzymalibysmy juz tylko mniejszą roznice!
        elif A[wsk2] - A[wsk1] > k: wsk1+=1
        else: 
            if wsk2 < leng: wsk2+=1
            else: break #skoro wsk2 nie mozemy juz przesunac to, przesuwajac wsk1 zrobimy jedynie mniejsza roznice!
    return counter

t = [3,3,5,7,7,9,11]
print(amount_of_things(t,4))
        










    
        