# Igor Urbanik
# Liczymy dystrybuante
# Rozdzielamy buckety ze wzgledu na (zinterpolowana liniowo) dystrybuante (ilsoc podzielona przez 7 bo ta stala dawala najlepsze wyniki)
# Ta ostatnia dziwna linijka sumuje
# Zlozonosc czasowa O(n+k)
# gdzie k to dlugosc tablicy z przedzialami

from zad3testy import runtests

def SortTab(T,P):
    n = len(T)

    distr = [0]*(n+2)
    for a, b, p in P:
        f = p/(b-a+1)
        distr[a] += f
        distr[b+1] -= f

    for i in range(1, n+2):
        distr[i] += distr[i-1]

    for i in range(1, n+2):
        distr[i] += distr[i-1]
# pierwsza robi funkcję gęstości prawdopodobieństwa 
# czyli potoczny rozkład a druga dopiero zamienia to w dystrybuante czyli de facto całkuje
# bo to co na poczatku tam pakujemy to w bardzo nieformalnym sensie pochodna funkcji gęstości prawodpodobieństwa, 
# która jest stała przez większość czasu i ma skoki co jakiś czas gdy rozpoczyna/konczy sie przedział

    FACTOR = 7
    buckets = [[] for _ in range(n//FACTOR+1)]

    nfac = n/FACTOR
    for x in T:
        xint = int(x)
        buckets[int( nfac*(distr[xint] + (distr[xint+1]-distr[xint])*(x-xint)) )].append(x)

    for bucket in buckets:
        n = len(bucket)
        
        if n < 2: continue
        if n < 3:
            if bucket[1] < bucket[0]:
                bucket[0], bucket[1] = bucket[1], bucket[0]
            continue

        for i in range(1, n):
            key = bucket[i]
            j = i-1
            while j >= 0 and key < bucket[j]:
                    bucket[j+1] = bucket[j]
                    j -= 1
            bucket[j+1] = key
    
    return [_ for _ in buckets for _ in _] # Suma wszystkich bucketow

runtests( SortTab )