#posortuj n-elementowa tablice A zawierającą wartości e [0,n^2-1]
#[1,13,24,5,9] -  zaminimy na liczby o podstawie n

#x = lambda x: x + 1  

def sortbyKey(tab,n,key):
    count = [0 for _ in range(n)]
    res = [0] * n
    for elem in tab:
        count[key(elem)] +=1
    for i in range(1,n):
        count[i] += count[i-1]
    for i in range(n-1,-1,-1):
        res[count[key(tab[i])]-1] = tab[i]
        count[key(tab[i])]-=1
    print(res)
    return res

def sort_this(tab,n):
    sorteD =sortbyKey(tab,n,lambda x: x%n) #najpierw metoda key(x%n) a potem key(x//n) -> dokladnie jak przy zamianie systemow!!!
    return sortbyKey(sorteD,n,lambda x: x//n)

t = [5,8,9,7,5,32,5,5,120,67,6,54]
sort_this(t,len(t))
#n-elementowa tablica A, wartosci w A pochodzą ze zbioru R, |B| = log(n) Posortuj
#O(log(log(n))*n)

# def _sort(T):
#     p = []
#     for i in T:
#         if find(p,i):
#             insert(p,i)
#     licznik = [0 for _ in p]
#     for i in T:
#         licznik[index(p,i)] +=1
#     iter =0
#     for i in range(len(p)):
#         while licznik[i] != 0:
#             licznik[i] -=1
#             T[iter] = p[i]
#             iter +=1
#     return T

#3 n-literowe slowa A i B czy A i B to anagramy?

def anagram(A,B,k):
    letters = [0 for _ in range(k)] 
    for i in A:
        letters[i] +=1
    for i in B:
        letters[i] -=1
    for i in letters:
        if i != 0:
            return False
    return True

def anagram2(A,B,arr): #O(n)
    for i in A:
        arr[i] = 0
    for i in B:
        arr[i] = 0
    for i in A:
        arr[i]+=1
    for i in B:
        arr[i] -=1
    for i in A:
        if arr[i] !=0:
            return False
    for i in B:
        if arr[i] !=0:
            return False
    return True

#generujemy ciagi liczb od 0 do 10^9 - musimy stwierdzic ile jest unikalnych wartosci
#musimy miec duza tablice
#odniesienia miedzy elementami tablicy i stosem



#mamy tablice zaw n liczb. zaimplementuj algorytm ktory znajdzie pare x i y miedzy ktorymi jest najwieksza roznica, jak sie posortuje.
#w czasie liniowym
#Rozw: bucket sortem
#[4,15,1,6,5]
#min=1
#max = 15
#5 pudelkow 

#kubelki:
# 1  
# 5,4,6
# 7 
#
# 15



