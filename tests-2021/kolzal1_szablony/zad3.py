from zad3testy import runtests
# Dyrektor działu handlowego pewnej firmy odbywa podróż służbową z miasta A do B.
# W pewnych punktahc zaplanowanej trasy znajdują się stacje benzynowe. Niestety,
# ze względu na problemy z dostawami surowca, stacje limitują objętość paliwa, którą może zatankować 
# pojedyńczy klient. Co więcej, z powodu modyfikacji zmierzających do zwiększenia głośności i mocy silnika,
# samochód dyrektora spala aż 1 litr paliwa na 1 kilometr trasy. Dyrektor się spieszy - musi więc 
# tak zaplanować podróż, by zatrzymać sie na jak najmniejszej liczbie stacji. Jest to 
# o tyle niełatwe, że każda stacja ma własny limit litrów paliwa, które można na niej zatankować.
# Dodatkową przeszkodą jest fakt, że w celu zmniejszenia masy pojazdu zmodyfikowano w nim zbiornik paliwa ,
# który obecnie mieści jedynie q litrów benzyny.

# Zaproponuj i zaimplementuj algorytm wskazujący na których stacjach dyrektor powinien
# tankować paliwo (tak, by tankować możliwie najmniejszą liczbę razy). Algorytm powinien być możliwie
# jak najszybszy i zużywać jak najmniej pamięci. Uzasadnij jego poprawność i oszacuj złożoność obliczeniową.
# Algorytm należy zaimplementować jako funkcję: def iamlate(T,V,q,l):

# która przyjmuje:
# 1. Tablicę liczb naturalnych T z pozycjami stacji benzynowych, wyrażonymi jako kilometry 
# od początku trasy. Pierwsza stacja znajduje się na początku trasy, t.j. T[0] == 0. Kolejne stacje 
# umieszczone są w T w kolejności odległości od początku trasy. 

# 2. Tablicę dodatnich liczb naturalnych V zawierających limity paliwa, które może zatankować pojedyńczy klient. 
# Tak więc V[i] to liczba litrów paliwa, którą można zatankować na stacji w pozycji T[i]. Na danej stacji można 
# tankować tylko raz.

# 3. Dodatnią liczbę naturalną q będącą pojemnością baku samochodu (liczba litrów paliwa, które mieszczą się w baku).
# Zakładamy, że przed pierwszym tankowaniem w baku nie ma paliwa

# 4. Dodatnią liczbę naturalną l będącą długością trasy w kilometrach.

# Funkcja powinna zwrócić listę numerów stacji, na których należy zatankować paliwo (w kolejności tankowania).
# Jeśli warunki zadania uniemożliwiają dotarcie do celu, funkcja powinna zwrócić pustą listę.
# Stacje numerujemy od 0. Stacja na początku trasy stanowi część rozwiązania. 



def iamlate(T, V, q, l):
    """tu prosze wpisac wlasna implementacje"""
    T.append(l) #ostatnia stacja jest nie do tankowania ale jedynie do wskazania ze tam dotarlismy
    V.append(0) #ostatnie miejsce ma zero paliwa
    dp = [[float("inf") for i in range(q+1)] for j in range(len(T))]
    # dp[dist][paliwo]
    #bierzemy cale paliwo na stacji poczatkowej
    newPaliwo = min(V[0],q)
    dp[0][newPaliwo] = 0 
    
    parents = [[[-1,-1] for i in range(q+1)] for j in range(len(T))]
    #przemieszczenie na kolejne stacje
    for i in range(len(T)):
        for j in range(q+1):
            #będąc na danej pozycji w tablicy T[i] oraz mając j paliwa, mozemy sie przemiescic maksymalnie do pozycji T[k+i]-T[i] <=j
            if dp[i][j] != float("inf"):
                k = 1
                while i + k < len(T) and T[i+k] - T[i] <= j:
                    newPaliwo = min(q,j - (T[i+k] - T[i]) + V[i+k]) 
                    if dp[i+k][newPaliwo] > 1 + dp[i][j]:
                        dp[i+k][newPaliwo] = 1 + dp[i][j]
                        parents[i+k][newPaliwo][0] = i
                        parents[i+k][newPaliwo][1] = j 
                    k+=1
    
    minimDist = float("inf")
    paliwo = 0
    for j in range(q+1):
        if minimDist > dp[-1][j]:
            minimDist = dp[-1][j] 
            paliwo = j
    if minimDist == float("inf"): return []

    i,j = parents[-1][paliwo] #T append(l)

    ans = []
    while i != -1:
        ans.append(i)
        i,j = parents[i][j]
        
    return list(reversed(ans))

runtests( iamlate )
