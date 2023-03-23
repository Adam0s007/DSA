# Dany jest zbiór przedziałów otwartych. Zaproponuj algorytm, który znajdzie podzbiór 
# tego zbioru, taki że:
# 1) jego rozmiar wynosi dokładnie k
# 2) przedziały są rozłączne
# 3) różnica między najwcześniejszym początkiem, a najdalszym końcem jest minimalna  

# Jeśli rozwiązanie nie istnieje to algorytm powinien to stwierdzić. Algorytm powinien być 
# w miarę możliwości szybki, ale przede wszystkim poprawny

#rozwiazanie:
#posortować nalezy przedzialy rosnaco ze wzgledu na poczatki
#dla kazdego przedzialu znalezc przedzialy rozlaczne z nim, a z nich wybrać ten o minimalnym koncu.
# powtarzać czynność dla kolejnych przedziałów k razy.
#powtarzamy krok 1. dla kazdego jednego przedzialu
# algorytm bedzie działał w O(n^2*k)

def przedzialyOtwarte(T,k):
    if k <=0: return None #aby nie bylo jakichs bledow
    T.sort(key=lambda x: x[0])
    minim = float("inf")
    best = -1
    zbiory = [[tup] for tup in T] #na poczatku wypelniamy jednym przedzialem na kazdy indeks

    def dfs(start_ind,i,ilosc): #tutaj start_ind sie nie zmieni, i - to ity indeks dla ktorego szukamy najlepszego przedzialu, ilosc - ilosc pozostalych przedzialow do rozpatrzenia
        if ilosc == 0: return True, zbiory[start_ind][-1][1] - zbiory[start_ind][0][0]
        best_ind = i
        minim_ending = float("inf")
        for j in range(i+1,len(T)):
            if T[i][1] <= T[j][0]: # znajdujemy pierwszy przedzial rozlaczny! Dalej bedą same rozlaczne ze wzgledu na nasz i'ty
                for x in range(j,len(T)): #teraz szukamy przedzialu z minimalnym koncem!
                    if minim_ending > T[x][1]:
                        best_ind = x
                        minim_ending = T[x][1]
                #gdy juz uzyskamy tez nanjlepszy zbior, to dodajemy go do naszych zbiorow!
                zbiory[start_ind].append(T[best_ind])
                # po wyjsciu z petli for x in... musimy breakowac od razu!
                break
        if best_ind != i:
            return dfs(start_ind,best_ind,ilosc-1)
        #jesli natomiast best_ind == i to musimy zwrocic False! Ze wzgledu na to, ze ilosc zbiorow pozostalych do rozpatrzenia != 0 oraz nie znalezlismy juz innego
        # to musimy zwracać false
        else: return False, float("inf")
    
    for i in range(len(T)): #nasz pierwszy przedzial od ktorego idziemy
        czyDaSie,new = dfs(i,i,k-1) # z uwagi na fakt ze 1 zbior juz mamy w zbiorach, to pozostalo nam k-1 do rozpatrzenia
        if czyDaSie:
            if minim > new:
                minim = new
                best = i 
    if best != -1: return zbiory[best]
    return None         

T = [(0,3),(0,2),(1,4),(2,4),(2,3),(3,5),(4,7),(5,8),(5,7),(6,9),(7,11),(8,10),(8,9),(9,12)]
# T = [(0,3),(0,2),(1,4),(2,4),(2,3),(3,5),(4,7),(5,8),(5,7),(6,7),(7,8),(8,10),(8,9),(9,12)]
k = 3
print(przedzialyOtwarte(T,k))    
                



