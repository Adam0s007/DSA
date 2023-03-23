from kol1btesty import runtests



def f(T):
    hashmap = {}
    for elem in T:
        tab = [0 for i in range(26)]
        for znak in elem:
            tab[ord(znak)-97] +=1
        strn = ""
        for liczba in tab: strn += str(liczba)
        hashmap[strn] = hashmap.get(strn,0) + 1
    return max(hashmap.values())

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True)
