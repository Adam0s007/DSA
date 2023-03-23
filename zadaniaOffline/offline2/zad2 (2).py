from zad2testy import runtests
#Adam Biśta
#funkcja sklada sie z 3 czesci:
# 1) sortujemy tablice przedzialow Quicksortem typu Hoare'a rosnaco wzgledem poczatku przedzialu
# 2) szukamy  kandydatow na posiadanie najwiecej przedzialow wewnatrz swojego przedzialu
#   przedzialy zawarte w rozpatrywanym przedziale sa pomijane
#   pomijanie nastepuje rowniez w przypadku tego samego poczatku (dlatego sortowalismy wczesniej)
#   odnalezienie 1. przedzialu niezawierajacego sie w rozaptrywanym przedziale  skutkuje jego przeniesieniem na stos 
#   kolejny rozpatrywany przedzial to ten, co dopiero wrzucilismy na stos
# 3) wydobywamy ze stosu kolejne przedzialy, sprawdzamy czy "pod nim" czasem nie wystepuja inne z tym samym poczatkiem, a nastepnie szukamy zawierajacych sie w rozpatrywanym.

#Zlozonosc czasowa algorytmu moze wahać się od O(nlogn) do O(n^2) gdyż w pesymistycznym przypadku
#wszystkie przedzialy mogą byc częściowo rozlaczne skutkując tym, ze wszystkie pojdą na stos i bedzie trzeba rozpatrywać w łącznym czasie kwadratowym
#inny przypadek: pesymistyczne dane do sortowania skutkujące zlozonosc O(n^2) sortowania


def depth(L):
    #quicksort(L) 
    L.sort(key=lambda x: x[0])
    stos = [0]
   
    a = L[0][0]
    b = L[0][1]
    for i in range(1,len(L)):
        if L[i][1] > b and a != L[i][0]:
            stos.append(i) 
            b = L[i][1]
            a = L[i][0]
        
    maks =0
    for i in stos:
        c = 0
        a = L[i][0]
        b = L[i][1]
    
        tmp = i-1
        while tmp >= 0 and a == L[tmp][0]:
            c+=1
            tmp-=1

        for j in range(i+1,len(L)):
            if L[j][1]<=b:
                c+=1
            elif L[j][0] == a:
                b = L[j][1]
                c+=1
            elif b < L[j][0]: break 
        maks = max(maks,c)
        if len(L)-i-1-maks <=0:
            return maks
    return maks
    
def quicksort(T): 
    stos = []
    stos.append((0,len(T)-1))
    while len(stos)>0: 
        left,right = stos.pop()
       
        i = left
        j = right
        pivot =T[(left+right)//2]
        while i <= j:
            while T[i][0] < pivot[0]:
                i+=1
            while T[j][0] >  pivot[0]:
                j-=1
            if i<=j:
                T[j], T[i] = T[i], T[j]
                i+=1
                j-=1 
        if left < j: 
            stos.append((left,j))
        if i < right: 
            stos.append((i,right))    

runtests( depth )