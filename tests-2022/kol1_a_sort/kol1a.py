from kol1atesty import runtests


#najlepsze jest to ze dla dobrze zrobionej hashmapy to zadanie da sie zrobic w O(n+N) gdzie N - laczna dlugosc wszystkich wyrazow a n - ilosc wyrazow 
def g(T):
    hashmap = {}
    for elem in T:
        strn1 = elem + elem[::-1]
        strn2 = elem[::-1] + elem
        if strn1 in hashmap:
            hashmap[strn1] = hashmap.get(strn1) + 1
        elif strn1 not in hashmap and strn2 not in hashmap:
            hashmap[strn1] = 1
        if strn1 not in hashmap and strn2 in hashmap:
            hashmap[strn2] = hashmap.get(strn2) + 1
        

    return max(hashmap.values())

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
