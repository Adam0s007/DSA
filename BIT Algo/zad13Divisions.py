# Dana jest tablica 2n liczb rzeczywistych. Zaproponuj algorytm, ktory podzieli
# te liczby na n par w taki sposob, ze podzial bedzie miał najmniejszą maksymalną
# sumę liczb w parze.

# Przykladowo:
# dla liczb (1,3,5,9) możemy mieć podziały ((1,3),(5,9)) oraz ((1,9),(3,5)) oraz ((1,9),(3,5)).
# Sumy par dla tych podzialow to (4,14), (6,12) oraz (10,8)
# dlatego maksymalne sumy to 14,12,10. Wynika z tego, że ostatni podział ma najmniejszą maksymalną sumę.


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



T = [1,3,5,9]

def min_max_suma(A):
    l,r = 0,len(A)-1
    quicksort(A)
    maksim = 0
    while l < r:
        maksim = max(A[l]+A[r],maksim)
        l +=1
        r -=1
    if maksim == 0: return T[0]
    return maksim
    

print(min_max_suma(T))

