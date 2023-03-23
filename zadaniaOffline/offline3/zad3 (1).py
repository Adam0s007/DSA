from zad3testy import runtests
"""Adrian Madej"""
"""Złożoność O(n), Bucket sort. Wstawiając do kubełka odrazu ustawiamy elementy w poprawnej
kolejności"""

def Insertion(T):
    n = len(T)
    j = n-2
    x = T[n-1]
    while j >= 0 and T[j] > x:
        T[j+1] = T[j]
        j -= 1
    T[j+1] = x

def SortTab(T, P):
    n = len(T)
    highest = max(T)
    Bucket_arr = [[] for _ in range(n)]
    for i in range(n):
        indeks = int((T[i]/highest)*n)
        if indeks == n:
            indeks -= 1
        Bucket_arr[indeks].append(T[i])
        Insertion(Bucket_arr[indeks])
    iter = 0
    for i in range(len(Bucket_arr)):
        for elem in Bucket_arr[i]:
            T[iter] = elem
            iter +=1      
    return T


runtests( SortTab )