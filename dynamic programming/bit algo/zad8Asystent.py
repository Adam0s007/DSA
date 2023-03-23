# Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb
# (liczby mogą być zarówno dodatnie jak i ujemne). 
# Aby zminimalizować błędy zaokrągleń asystent
# postanowił wykonać powyższe dodawania w takiej kolejności, by największy
# co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji dodawania; wartośc końcowej sumy również
# traktujemy jak wynik tymczasowy) był możliwie najmniejszy.
# Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie wybiera kolejność dodawań.
# Napisz funkcję opt sum, która przyjmuje tablicę liczb n1,n2,...nk (w kolejnosci w jakiej występują w sumie;
# zakładamy, że tablica zawiera co najmniej dwie liczby) i zwraca
# największą wartość bezwzględną wyniku tymczasowego w optymalnej kolejności dodawań.

# Na przykład dla tablicy wejściowej: [1,-5,2] funkcja powinna zwrócić wartość 3, co odpowiada dodaniu 
# -5 i 2 a następnie dodaniu 1 do wyniku. Uzasadnij poprawnośc zaproponowanego rozwiązania i oszacuj jego 
# złożoność obliczeniową.


#rozw:
# F = [[0]*n for _ in range(n)]
# F(i,j) - najwieksza wartosc bezwzgledna w wyniku tymczasowym
# od i do j
# sum(i,j) = suma elementow od i do j
#   F(i,i+1) = abs(n(i) + n(i+1))
# F(i,j) = max(abs(sum(i,j)), min(F(i-1,j),F(i,j-1)))

def weird_sum(T):
    n = len(T)
    dp = [[0 for j in range(n)] for i in range(n)]
    i = 0
    j = len(T) -1 
    def dfs(i,j):
        if i == n or j <0: return 0
        if i == j: return T[i]
        if dp[i][j] != 0: return dp[i][j]
        if i + 1 == j: return abs(T[i] + T[j])
        for k in range(i+1,j):
            total1 = dfs(i+1,k)
            total2 = dfs(k,j-1)
            c = dp[i][j] if dp[i][j] != 0 else float("inf")
            if total1 == 0 and total2 == 0: continue
            
            if total1 == 0 and total2 != 0: 
                dp[i][j] = min(c,abs(T[j] +  total2))
            if total2 == 0 and total1 != 0:
                dp[i][j] = min(c,abs(T[i] + total1))
            else:
                dp[i][j] = min(c,abs(T[i] + total1), abs(T[j] +  total2))

        dp[i][j]  = max(sum(T[i:j+1]),dp[i][j])
        return dp[i][j]
    return dfs(i,j)

T = [1,-5,2]
print(weird_sum(T))

