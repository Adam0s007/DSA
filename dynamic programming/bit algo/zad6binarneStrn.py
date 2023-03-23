# Dostajemy liczbe naturalną n. Naszym zadaniem jest policzenie wszystkich binarnych (0/1) stringow
# o dlugosci n bez jedynek obok siebie.

#rozw:
#ciagiem fibbonaciego:
#f(n) = f(n-1) + f(n-2)   [...] dl n-1 + 0 lub [...] dl n-2 + 01
#n = 1: 0,1 => f(1) = 2
# n=2: 00,01,10 => f(2) = 3

def strn(n):
    ostZero = 1
    ostJeden = 1
    newZero = 1
    newJeden = 1
    for i in range(2,n+1):
        newZero = ostZero + ostJeden #gdy nowe zero na koncu, to bierzemy te gdzie byly zera i jedynki 
        newJeden = ostZero

        ostZero = newZero
        ostJeden = newJeden

    return newZero + newJeden 

print(strn(4))



