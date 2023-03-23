# Dane sa trzy zbiory reprezentowane przez tablice: A,B, i C
# Napisz algorytm, ktory powie, czy istnieje taka trjka a,b,c z odpowiednio
# A,B i C, że a + b = c. Nie wolno korzystac ze slownikow!

# A[1,3,5,7,9,12,16,18]    jesli a + b > c to konczymy!!
# B[13,17,18,21,30,37]
# C[1,2,4,8,9,13,14,15]

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

def sum_of_nums(A,B,C): #O(ALOGA + BLOGB + CLOGC + a+b+c)
    quicksort(A)
    quicksort(B)
    quicksort(C)
    a=0
    b=0
    c=0
    while c < len(C):
        if A[a] + B[b] == C[c]: return True
        elif A[a] + B[b] > C[c]: c +=1
        else:
            if A[a] < B[b]:
                if a < len(A): a+=1
                else: b+=1
            else:
                if b < len(B): b+=1
                else: a +=1
    return False

def sum_of_nums2(A,B,C): # O(AlogA + BlogB + c(a+b))
    quicksort(A)
    quicksort(B)
    for c in range(len(C)):
        a = 0
        b = len(B)-1
        while a < len(A) and b >=0:
            if A[a] + B[b] == C[c]: return True
            elif A[a] + B[b] < C[c]: a+=1
            else: b-=1
    return False

A =[1,3,5,7,9,12,16,18]  
B =[13,17,18,21,30,37]
C =[1,2,4,8,9,13,14,15]
print(sum_of_nums(A,B,C))
print(sum_of_nums2(A,B,C))
#inne rozwiazanie:  AlogA + BlogB + c(a+b)
# sortujemy A i B
# dwa wskazniki: jeden na poczatku A, drugi na koncu B:
# dla kazdego elementu c z osobna szukamy liniowo dwoma wskaznikami tamtych tablic rozwiazania!
# obydwoma wskaznikami dochodzimy do obu koncow tablic!       
         