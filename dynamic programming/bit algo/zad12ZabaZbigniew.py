# Żaba Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n-1, skacząc wyłacznie 
# w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j-i jednostek energii,
# a jego energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale
# na szczęscie na niektórych liczbach - także na zerze - leżą przekąski o określonej wartości energetycznej
# (wartość przekąski dodaje do aktualnej energii Zbigniewa).

# Proszę zaimplementować funkcję zbigniew(A), któa otrzymuje na wejściu tablicę A długości len(A) = n.
# Każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie. Funkcja
# powinna zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do n-1 lub -1 jeśli nie jest to możliwe


def zbyszek(T): #F[2][0] - mam 2 energie stojąc na polu 0
    n = len(T)
    F = [[10**9 for _ in range(n)] for _ in range(n+1)] #iterator] energia] 
    F[T[0]][0] = 0
    #majac jedno pole i daną ilosc energii na tym polu mamy 0 skokow jesli tylko to jedno pole istnieje
    for i in range(n):
        for j in range(n+1):
            if F[j][i] != 10**9:  # będąc na i-tym miejscu mamy j energii
                for k in range(1, j + 1): # idąc o k do przodu wykonujemy jeden skok i zużywamy k energii
                    if i+k<n and n >= j-k+T[i + k] >= 0:
                        F[j - k + T[i + k]][i + k] = min(F[j][i] + 1, F[j-k + T[i+k]][i + k])
                    if i+k < n and j-k+T[i+k] > n: # przypadek, jakby żab miał więcej energii niż rozmiar tablicy
                        #mozemy tak zrobic bo nie interesuje nas dokladna ilosc energii a jedynie skoki
                        F[-1][i + k] = min(F[-1][i+k], F[j][i] + 1)
                       # F[nasze maksimum energii][pole do ktorego zmierzamy] 
                        

    ans = 10**9
    for i in range(n+1):
        ans = min(ans, F[i][n - 1])
    for i in range(n): # to było tylko do ładnego printowania
        for j in range(n+1):
            if F[j][i] == float("inf"):
                F[j][i] = 0
    for el in F:
        print(el)
    print(ans)
    
A = [2,2,1,0,0,0]
A = [4,5,2,4,1,2,1,0]
zbyszek(A)

    