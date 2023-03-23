from egzP2btesty import runtests
from math import log10

def kryptograf( D, Q ):    
    #tutaj proszę wpisać własną implementację
    slowniczek = {}
    for strn in D:
        for i in range(len(strn)-1,-1,-1):
            slowniczek[strn[i:]] = slowniczek.get(strn[i:],0) + 1
    sum = 0
    for strn in Q:
        if strn == "": sum += log10(len(D))
        else: sum += log10(slowniczek.get(strn,1))
    return sum

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 3)