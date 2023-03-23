# Dany jest zbiór przedziałów A = {(a0,b0),...,(an-1,bn-1)}. Proszę zaimplementować funkcję:
# def kintersect(A,k):...
# która wyznacza k przedziałów, których przecięcie jest najdłuższym przedziałem. Zbiór A jest 
# reprezentowany jako lista par. Końce przedziałów to liczby całkowite. Można założyć, że k >=1 
# oraz k jest mniejsze lub równe łącznej liczbie przedziałów w A. Funkcja powinna zwracać listę 
# numerów przedziałów, któe należą do rozwiązania.
# Funkcja  powinna być jak najszybsza. Proszę oszacować złożoność czasową i pamięciową użytego
# algorytmu.
# Przykład: Rozważmy listę przedziałów:
# A = [(0,4),(1,10),(6,7),(2,8)]
# Dla k = 3 wynikiem powinno być [0,1,3] (lub dowolna permutacja tej listy), co daje przedziały
# o przecięciu [2,4], o długości 4- 2 = 2

#rozwiazanie: jesli jakas czesc wspolna przedzialow jest przecieciem k przedzialow - to ta czesc
# wspolna jest tez przecieciem jakichs dwoch przedzialow!!!
#wobec czego mozna wyznaczyc wszystkie mozliwe przeciecia dwoch przedzialow.
# to są dwa przedzialy, a więc dla kazdego takiego przeciecia jeszcze sprawdzamy, ktore z k-2 pozostalych
# przedzialow w tym sie zawiera
#doobrze jest zrobic jakis osobny licznik (na poczatku dla wszystkich mozliwosci ustawiony na 0)
# potem dla kazdej mozliwosci inkrementujemy licznik
# z tych mozliwosci co mają licznik >= k wybieramy najwieksze przeciecie

from zad9testy import runtests
from math import inf
# def kintersect(A,k):
#     tablica_mozliwosci = {}
#     counters = {}
#     if k == 1:
#         best_int = [0,0]
#         ind = 0
#         for i in range(len(A)):
#             if A[i][1] - A[i][0] > best_int[1] - best_int[1]:
#                 best_interval = A[i]
#                 ind = i 
#         return [ind]
#     for i in range(len(A)):
#         for j in range(i+1,len(A)):
#             tablica_mozliwosci[(i,j)] = [max(A[i][0],A[j][0]),min(A[j][1],A[i][1])]
#             counters[(i,j)] = 0

#     for x in range(len(A)):
#         for keys in tablica_mozliwosci.keys():
#             if tablica_mozliwosci.get(keys)[0] >= A[x][0] and tablica_mozliwosci.get(keys)[1] <= A[x][1]:
#                counters[keys] = counters.get(keys) + 1
#     best_interval = [0,0]
#     print(best_interval)
#     for keys,values in counters.items():
#         if values >= k and best_interval[1] - best_interval[0] < tablica_mozliwosci.get(keys)[1] - tablica_mozliwosci.get(keys)[0]:
#             best_interval = tablica_mozliwosci.get(keys).copy()
#     ans = []
#     licznik = 0
#     for x in range(len(A)):
#         if best_interval[0] >= A[x][0] and best_interval[1] <= A[x][1] and licznik < k:
#             ans.append(x)
#             licznik +=1
    
#     return ans


#rozwiazanie nlogn:
#sortujemy wzgledem poczatku przedzialy!
# najpierw oznaczamy kazdy punkt w tablicy A osobno, bedzie 2n tych punktow jedne muszą miec oznaczenie takie, ze
# są koncem danego przedzialu a inne takie, ze są poczatkiem przedzialu np kazdy punkt to krotka (x,P,y) lub (y,K,None)
# gdzie (x,P,y) to normalny przedzial [x,y] a P to oznaczenie ze jest to punkt poczatkowy
# natomiast (y,K,None) oznacza ze mamy punkt y bedący koncem w danym przedziale a K ozn ze to punkt koncowy danego 
# przedzialu
# ale po co nam takie oznaczenia? bedziemy sortować tablicę po początak tych krotek (czyli po 1. wspolrzednych przedzialow)
# za kazdym razem jak natrafiamy na normalny punkt (x,P,y) to counter (oznaczajacy ilosc wykorzystywanych w danym momencie
# przedzialow) zwiekszamy o 1 oraz dodajemy do kolejki priorytetowej y bedący koncem a kolejka ta jest typu minHeap
# czyli zawsze wyjety zostanie najmniejszy koniec!!!
# w momencie w ktorym nasz counter >= k to wtedy wiemy ze mamy juz wystarczajacą ilosc przedzialow za sobą,
# oraz wystarczającą ilosc końców tych przedzialow w kolejce wiec wyjmujemy jakis koniec z tej kolejki (zawsze bedzie minimalny)
# i laczymy go z naszym obecnym poczatkiem (ten przedzial bedzie zawsze przecieciem jakichs k przedzialow bo poczatek minimalny
# oraz koniec tez minimalny dopiero co wyjety)
# nastepnie prownujemy ten przedzial "zlozony z k przedzialow" z najlepszym przedzialem o najwiekszej roznicy end-start

#w sytuacji, gdy natrafimy na punkt typu (y,K,None), to wtedy nasz counter zmniejszamy o 1, sygnalizujac jednoczesnie, ze
# jakis przedzial juz nie moze byc rozpatrywany!!

# co moze nas zaniepokoic?
# gdy nasz counter >= k to wybieramy z heapu najkrotszy koniec i sie go pozbywamy ale
# czy ta wartosc juz nam sie nigdy nie przyda?? Otóż nie -> idąc dalej po posortowanej tablicy napotkamy juz tylko
# takie poczatki ze: (nasza wyjeta wartosc z heapu - te nowsze poczatki ) da w rezultacie wynik gorszy od 
# tego kiedy na poczatku wyjmujemy z heapu koniec. T roznica zawsze jest mniejsza wiec sie nie przejmujemy. Po to tez 
# sortowalismy tablicę


import heapq


def kintersect(A,k):
    queue = []
    newTab = []
    counter = 0
    for i in range(len(A)):#
        newTab.append((A[i][0],0,A[i][1])) # punkt poczatkowy przedzialu o znaczniku 0 o poczatku w A[i][0] 
        newTab.append((A[i][1],1,None)) #punktu koncowy o znaczniku 1, koniec ktory zaczyna sie w A[i][1]
    newTab.sort(key=lambda x: x[0]) #sortujemy ze wzgledu na punkty pierwsze

    best_interval = [0,0]
    for i in range(len(newTab)):
        if not newTab[i][1]:
            heapq.heappush(queue,newTab[i][2]) #dajemy koniec do heapu        
            counter +=1 #dodalismy nowy "przedzial" wiec dodajemy counter  
            if counter >= k:
                end = heapq.heappop(queue) #mamy najkrotszy koniec 
                interval = [newTab[i][0],end] #poczatek jest najkrotszy przy aktualnie rozpatrywanym przedziale, 
                # po to wlasnie sortowalismy tą tablicę, a my potrzebujemy aktualnie najkrotszy koniec do tego
                if best_interval[1] - best_interval[0] < interval[1] - interval[0]:
                    best_interval = interval.copy()            
        else:
            counter -=1 #jesli natrafilismy na punktu oznaczajacy koniec no to bedziemy rozpatrywac dalej o 1 mniej przedzialow 


    licznik = 0
    ans = []
    for i in range(len(A)):
        if best_interval[0] >= A[i][0] and best_interval[1] <= A[i][1] and licznik < k:
            licznik +=1
            ans.append(i)
    return ans

runtests( kintersect )