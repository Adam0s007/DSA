from zad11ktesty import runtests
# W porcie na odbiór oczekuje n kontenerów z towarem. Waga każdego kontenera jest znana i
# zapisana w tablicy T (w kilogramach). Dwuczęściowy kontenerowiec, który przypłynął
# odebrać towar jest ogromny - na tylko jednej z jego części zmieściłyby się wszystkie
# oczekujące kontenery. Jednak ze względów technicznych, aby statek nie zatonął, w każdej z
# dwóch jego części musi znajdować się towar o tej samej łącznej wadze. Z tego względu
# władze portowe muszą zaopatrzyć statek w pewną ilość kilogramowych odważników, które
# pozwolą na wyrównanie wagi w obydwu jego częściach. Odważniki te jednak są drogie, więc
# zależy im na tym, aby użyć ich jak najmniej. Twoim zadaniem jako programisty jest napisanie
# programu, który policzy, jaka jest ta najmniejsza możliwa liczba odważników.

def kontenerowiec(T):
    #Tutaj proszę wpisać własną implementację
    suma = sum(T)
    dp = [[-1 for i in range(suma+1)]for i in range(len(T)+1)]
    def dfs(i,s1=0):
        if i > len(T) - 1: return abs(suma - s1 - s1) #s2 == suma - s1, abs(s2 - s1) == abs(suma - 2s1)
        if dp[i][s1] != -1: return dp[i][s1]
        
        dp[i][s1] = min(dfs(i+1,s1+T[i]),dfs(i+1,s1))
        return dp[i][s1]
    return dfs(0)

runtests ( kontenerowiec )
    