# # Dostajemy na wejściu listę trójek (miastoA, miastoB,koszt). Każda z nich oznacza,
# # że możemy zbudować drogę między miastem A i B za podany koszt. Ponadto, w dowolnym
# # mieście możemy zbudować lotnisko za koszt K, niezależny od miasta. Na początku w żadnym mieście 
# # nie ma lotniska, podobnie między żadnymi dwoma miastami nie ma wybudowanej drogi.
# Naszym celem jest zbudować lotniska i drogi za minimalny łączny koszt, tak aby każde 
# miasto miało dostęp do lotniska. 

# Miasto ma dostęp do lotniska, jeśli: 
# jest w nim lotnisko, lub można z niego dojechać do innego miasta w którym jest lotnisko.

# Jeżeli istnieje więcej niż jedno rozwiązanie o minimalnym koszcie, należy wybrać to z 
# największą ilością lotnisk.

#rozw:
# robimy algorytm kruskala!!
# najpierw sortujemy krawedzie po cenach rosnąco. Robimy polaczenia miast uzywając find-union.
# w momencie, gdy cena kolejnych laczonych krawedzi bedzie wieksza od postawienia lotniska, to stawiamy lotnisko

'''L = [(ai,bi,wi),(aj,bj,wj)...]   gdzie ai - miasto A, bi - miasto B, wi - cena polaczenia miast'''
class Node:
    def __init__(self,value):
        self.parent = self
        self.val = value
        self.rank = 0

def make(i):
    return Node(i)

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if y.rank == x.rank: y.rank+=1


def lotniska_miasta(L,k):
    L.sort(key=lambda x: x[2])
    maks= 0
    for x,y,w in L:
        maks = max(x,y)
    
    makeSets = [make(i) for i in range(maks+1)]
    counter = maks+1
    cost_roads = 0
    edges = []
    for x,y,w in L:
        if w < k:
            if find(makeSets[x]) != find(makeSets[y]):
                counter -=1
                union(makeSets[x],makeSets[y])
                edges.append((x,y,w))
                cost_roads +=w

    return cost_roads + counter*k,edges

L = [(0,1,30),(0,2,90),(0,3,90),(0,4,80),(0,5,100),(1,2,90),(1,3,90),(1,4,90),(1,5,90),(2,5,75),(2,4,90),(2,3,65),(3,5,80),(3,4,70),(4,5,20)]
print(lotniska_miasta(L,75))