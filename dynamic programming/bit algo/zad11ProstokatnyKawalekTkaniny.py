# Dany jest prostokątny kawałek tkaniny o wymiarach X na Y, oraz lista n produktów, 
# które mogą zostać wykonane z tej tkaniny. Do wytworzenia każdego produktu i (i zmienia się od 1 do n)
# potrzebny jest prostokątny kawałek tkaniny o wymiarach ai na bi, a zysk ze sprzedaży tego produktu wynosi ci.
# Zakładamy, że ai, bi, ci są dodatnie całkowite. Mając maszynę, która może przeciąć dowolny prostokątny kawałek
# tkaniny na dwa kawałki wzdłuż linii poziomej lub pionowej, zaprojektuj algorytm, który wyznaczy taką strategię
# cięcia materiału o wymiarach X na Y, aby sprzedaż wytworzonych produktów dała łacznie największy zysk


# f(i,j) - najwiekszy zysk dla rozw i x j 
# f(i,j) = max(Z(k,m) + max(f(i-k,j)+ f(j-m,k), f(j-m,i) + f(i-k,m)))

#      k (i-k)
#    ________________
#   |    |  |         |
#   |    |  |         |
#   |    |  |         | 
# m |-----  | (m-j)   |
# j |------ |         |
#    ------------------

#P - prostokatny kawalek tkaniny = (szer,wys)
#M - tablica kawalkow tkaniny (ai,bi,ci) => (szer,wys,cena)
def tkanina(P,M):
    dp = [[0 for i in range(P[1]+1)] for j in range(P[0]+1)]
    for szer in range(P[0]+1):
        for wys in range(P[1]+1):
            for k in range(len(M)):
                #material mozemy pociac w pionie lub tez w poziomie stad te dwa ify i totalH oraz totalV
                totalH = 0
                if szer-M[k][0] >=0 and wys-M[k][1] >=0:
                    total1 =  dp[szer-M[k][0]][wys]
                    total2 = dp[M[k][0]][wys-M[k][1]]
                    totalH = M[k][2] + total1 + total2 
                       
                totalV = 0
                if szer-M[k][1] >=0 and wys-M[k][0] >=0:
                    total3 = dp[szer-M[k][1]][wys]
                    total4 =  dp[M[k][1]][wys-M[k][0]]
                    totalV = M[k][2] + total3 + total4 

                dp[szer][wys] = max(dp[szer][wys],max(totalH,totalV))
        
    return dp[szer][wys]

P  = [6,8]
M = [(3,3,7),(2,2,4),(6,2,5)]
print(tkanina(P,M))


