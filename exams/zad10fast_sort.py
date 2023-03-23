# Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x, gdzie a to pewna
# stała większa od 1 ( a > 1) zaś x  to liczby rzeczywiste rozłożone równomiernie na przedziale
# [0,1]. Napisz funkcję fast_sort, któa przyjmuje tablicę liczb z wynikami eksperymentu 
# oraz stałą a i zwraca tablicę z wynikami eksperymentu 
# posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej. Uzasadnij poprawność
# zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową. Nagłówek funkcji fast_sort
# powinien mieć postać:


#rozwiazanie:
# wszystkie liczby zamienic na postac log(a)y czyli (log(a)a^x) (wtedy dostaniemy x)
#robimy bucket sorta na x'sach!

#wszystkie liczby zamieniamy na postac a^x 
from math import log 


def insertion_sort(T):
    for i in range(1,len(T)):
        elem = T[i]
        j = i-1
        while j >= 0 and elem < T[j]:
            T[j+1] = T[j]
            j -=1
        T[j+1] = elem
    return T

def fast_sort(T,a):
    new_T = [0 for i in range(len(T))]
    for indx,elem in enumerate(T):
        new_T[indx] = log(elem,a)
    #bucketsort:

    maksim = max(new_T)
    minim = min(new_T)
    range = len(new_T)
    r = (maksim-minim)/range 

    buckets = [[] for i in range(range)]
    for i in range(len(new_T)):
        index = int((new_T[i]- minim)/r)
        if index == range: index -=1
        buckets[index].append(new_T[i])
    
    for i in range(len(buckets)):
        buckets[i] = insertion_sort(buckets[i])

    
    ans = []
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            ans.append(buckets[i][j])

    for i in range(len(ans)):
        ans[i] = a**(ans[i])
    return ans


#a^x = y
# log(a)y = x 

