# Cel: dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1. Poczatkowo stoimy na pozycji
# 0, wartosc A[i] informuje nas jaka jest maksymalna długość skoku na następną pozycję.

# Przyklad A = [1,3,2,1,0]
# Z pozycji 0 mogę przejsć na pozycję 1. z pozycji 1 mogę przejść na 2,3,4. Należy policzyć
# na ile sposobów mogę przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy.



def skoki(A):
    n = len(A)
    dp = [0 for i in range(n)]
    dp[-1] = 1
    dp[-2]  = 1
    
    for i in range(n-3,-1,-1):
        for k in range(1,A[i]+1):
            if i + k < n:
                dp[i] += dp[i+k]
    print(dp)
    return dp[0]

A  =[1,3,2,1,0]
print(skoki(A))

