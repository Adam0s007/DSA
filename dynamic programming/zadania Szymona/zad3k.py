# Dla każdego ciągu n liczb możemy obliczyć k-ładną sumę (Zakładamy, że k <= n). Poprzez 
# k-ładną sumę rozumiemy minimalną sumę pewnych liczb wybranych w ten sposób, że z 
# każdych k kolejnych elementów wybraliśmy przynajmniej jeden z nich (w szczególności 
# oznacza to, że dla k=1 musimy wybrać wszystkie elementy, a dla k=n wystarczy wybrać 
# jeden, najmniejszy z nich). Proszę napisać algorytm, który dla zadanej tablicy liczb 
# naturalnych oraz wartości k oblicza k-ładną sumę. 
# Algorytm należy zaimplementować jako funkcję postaci:
# def ksuma( T, k ):
#  … 
# która przyjmuje tablicę liczb naturalnych T = [a1, a2, …, an] oraz liczbę naturalną k.
# Przykład. Dla tablicy:
# [1, 2, 3, 4, 6, 15, 8, 7] oraz k = 4
# Wynikiem jest liczba 7


from zad3ktesty import runtests

def ksuma( T, k ):
    dp = [0 for i in range(len(T))]
    for i in range(k):
        dp[i] = T[i]
    for i in range(k,len(T)):
        minim = float("inf")
        for j in range(i-k,i):
            minim = min(minim,dp[j])
        dp[i] = minim + T[i]
    return min(dp[len(T)-k:len(T)])
runtests ( ksuma )