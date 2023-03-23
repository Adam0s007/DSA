# Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0,k]. Zamieniono 10 liczb z tej
# tablicy na losowe liczby spoza tego zakresu (np. dużo wieksze lub ujemne). Napisz algorytm, ktory posortuje tablice w czasie O(n)

def insertionsort(A):
    for i in range(1,len(A)):
        curNum = A[i]
        j = i-1
        while j>=0 and curNum < A[j]:
            if A[j] > curNum:
                A[j+1] = A[j]
                j-=1    
        A[j+1] = curNum         
    return A

def sort_with_cases(tab,k):
    n = len(tab)
    r = n-1 #ten wsk bedzie przemieszczany by pozbyc sie niepasujacych liczb w srodku tablicy
    buckets  = [[] for i in range(2)] #separately for negative and huge numbers
    
    #tworzenie bucketow & przenoszenie niepoprawnych elementow na koniec
    while tab[r] > k or tab[r] < 0:
        if tab[r] > k: buckets[1].append(tab[r])
        else: buckets[0].append(tab[r])
        r-=1
    for i in range(n-10):
        if tab[i] > k:
            buckets[1].append(tab[i])
            tab[i],tab[r] = tab[r],tab[i]
            r-=1
            while tab[r] > k or tab[r] < 0: 
                if tab[r] > k: buckets[1].append(tab[r])
                else: buckets[0].append(tab[r])
                r-=1
        elif tab[i] < 0:
            buckets[0].append(tab[i])
            tab[i], tab[r] = tab[r],tab[i]
            r-=1
            while tab[r] > k or tab[r] < 0: 
                if tab[r] > k: buckets[1].append(tab[r])
                else: buckets[0].append(tab[r])
                r-=1
        if r == n-11: break
    #count sort for n-10 numbers
    #for i in range(n-10):
    output = [0 for i in range(n-10)]
    C = [0 for i in range(k+1)]
    for i in range(n-10):
        C[tab[i]]+=1
    for i in range(1,k+1):
        C[i] +=C[i-1]
    for i in range(n-10):
        output[C[tab[i]]-1] = tab[i]
        C[tab[i]]-=1
        
    #insertion sort for rest of numbers:
    buckets[0] = insertionsort(buckets[0])
    buckets[1] = insertionsort(buckets[1])
    k = 0
    for elem in buckets[0]:
        tab[k] = elem
        k+=1
    for elem in output:
        tab[k] = elem
        k+=1
    for elem in buckets[1]:
        tab[k] = elem
        k+=1
    return tab
t = [-9,6,8,-5,5,1,55,43,7,-88,88,2,1,2,6,3,4,6,423,6,23,4,34,2,10,37] #k = 8
print(sort_with_cases(t,10))
