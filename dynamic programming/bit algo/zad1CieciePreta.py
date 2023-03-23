# Firma kupuje dlugie stalowe prety i tnie je na kawałki, ktore sprzedaje. Kawalki
# mają dlugosc w metrach wyrażoną zawsze liczbą naturalną. Dla kawałka dlugosci n metrow
# znane są ceny kawałków długości 1,2,..., n metrow. Firma chce znać maksymalny zysk, ktore moze 
# uzyskać z pocięcia i sprzedania pręta długości n.

#rozw:
# f(i) = max zysk z preta dlugosci i 
# T: [0,2,3,7,8,...,9] -> wartosci tablicy to ceny , dlugosci preta to indeksy!

def cut_rod(p,n):
    dp = [0 for i in range(n+1)]
    s = [0 for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,i+1):
            if dp[i] < p[j] + dp[i-j]:
                dp[i] = p[j] + dp[i-j]
                s[i] = j #indeks z maksymalną wartością!
        print(dp)
    
    while n >0:
        print(s[n], end=' ')
        n = n - s[n] # bo mamy p[j] czyli indeks j zapisany w tablicy s , i idziemy do dp[i-j] -> dp[i-ost[i]]
    
    
    return dp[-1]

p = [0,1,5,8,9,10,17,80,20,24,30,2,23]
print(cut_rod(p,10))

