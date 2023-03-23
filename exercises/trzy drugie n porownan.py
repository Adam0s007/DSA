#Mamy nieposortowana tablice, szukamy min i max w n-elem tablicy za pomocą 3/2 n porownan (n - ilosc elem w tablicy)
from math import inf
def min_max(T):
    if len(T) < 2:
        if len(T) == 0:
            return None,None
        return T[0],T[0]

    if T[0] < T[1]:
        minimum = T[0]
        maksimum = T[1]
    else:
        minimum = T[1]
        maksimum = T[0]
    a,b = inf,0
    for i in range(2,len(T)-1,2): #idziemy od T[2] co 2 indeksy 
        if T[i] < T[i+1]: #takich porownan bedzie n/2
            a = min(a,T[i]) #takich porownan bedzie n/2
            b = max(b,T[i+1]) #       -||-  n/2
        else:
            a = min(a,T[i+1])
            b = max(b,T[i])
        print(T[i])
    if b > maksimum:
        maksimum = b
    if a < minimum:
        minimum = a
    if len(T)%2!=0: #jesli dlugosc tablicy jest nieparzysta, petla for range skonczy dzialanie na 3. elemencie od konca!, jesli parzysta - konczy na przedostatnim 
        maksimum  = max(maksimum,T[len(T)-1])
        minimum = min(minimum,T[len(T)-1])
    return minimum, maksimum

T = [1,2,3] 
print(min_max(T))