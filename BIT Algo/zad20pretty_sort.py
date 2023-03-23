# Cyfra jednokrotna to taka, ktora wystepuje w danej liczbie dokladnie jeden raz.
# Cyfra wielokrotna to taka, ktora w liczbie wystepuje wiecej niz raz.
# Mowimy, że liczba naturalna A jest ladniejsza od liczby naturalnej B,
# jesli w liczbie A wystepuje wiecej cyfr jednokrotnych niz w B, a jezeli cyfr 
# jednokrotnych jest tyle samo to ladniejsza jest ta liczba, ktora posiada mniej cyfr 
# wielokrotnych. Np liczba 123 jest ladniejsza od 455, liczba 1266 jest ladniejsza od 114577, 
# a liczby 2344 i 67333 sa jednakowo  ladne.

# Dana jest tablica T zawierajaca liczby naturalne. Prosze zaimplementować funkcję:
# pretty_sort(T), ktora sortuje elementy tablicy T od najladniejszych do najmniej ladnych.
# Uzyty algorytm powinien byc mozliwie jak najszybszy. Prosze w rozwiazaniu umiescic 1-2 zdaniowy
# opis algorytmu oraz proszę oszacować jego złożonośc czasową.

def pretty_sort(T):
    n = len(T)
    buckets = [[0,0,T[i]] for i in range(n)]

    for i in range(len(T)):
        C = [0 for _ in range(10)]
        tmp = T[i]
        while tmp>0:
            C[tmp%10]+=1
            tmp//=10
        for j in range(len(C)):
            if C[j] == 1:
                buckets[i][0] +=1
            elif C[j] > 1:
                buckets[i][1] +=1
    #finding max value for first pos and sec pos:
    max0=0
    max1=0
    for i in range(n):
        max0 = max(buckets[i][0],max0)
        max1 = max(buckets[i][1],max1)
    
    countingSort(buckets,1,max1,n,1)
    
    countingSort(buckets,0,max0,n,1)
    #print(buckets)

    for i in range(len(buckets)):
        T[i] = buckets[i][2]
    return T

def countingSort(buckets,index,RANGE,n,flag=0):
    output = [0] * (n)
    count = [0] * (RANGE+1)
    for i in range(n):
        count[buckets[i][index]] += 1
    for i in range(1,RANGE+1):
        count[i] += count[i - 1]
    for i in range(n-1,-1,-1): 
        output[count[buckets[i][index]] - 1] = buckets[i]
        count[buckets[i][index]] -= 1
    if flag == 1:
        x = 0
        for i in range(n-1,-1,-1):
            buckets[x] = output[i]
            x+=1
    else:
        for i in range(n):
            buckets[i] = output[i]
    

from random import randint
T = [randint(0,100000000) for i in range(100)]
print(pretty_sort(T))




