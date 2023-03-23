from egzP4atesty import runtests 

#longest increasing subsequence problem O(n^2)
# def mosty ( T ):
#     T.sort(key=lambda x: (x[0],x[1])) #sortuję po pierwszej współrzędnej rosnąco, po drugiej też rosnąco
#     #pierwsze wspolrzedne są posortowane, co jesli pierwsza wsp jest taka sama natomiast w drugich i1 > i2?
#     #trzeba niestety posortowac tez ze wzgledu na drugie
#     #if (T[i][0] >= T[j][0] and T[i][1] >= T[j][1]) or (T[i][0] <= T[j][0] and T[i][1] <= T[j][1]):
#     #warunkiem analogicznym do tego  na mosty w lis jest lis[i] >= lis[j] gdy mamy same drugie wspolrzedne posortowane dwuwarunkowo
#     lis = []
#     for tuple in T:
#         lis.append(tuple[1])
    
#     dp = [1 for _ in range (len(T))] #maksymalna liczba mostów dla i-tego mostu z T
#     dp[0] = 1

#     for i in range (len(T)):
#         for j in range(i):
            
#             if lis[i] >= lis[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#     return max(dp)


#O(nlogn)
# longest ()
def ceilIndex(A,l,r,key): #binary search - wyszukaj najmniejszy element ktory jest wiekszy od rozpatrywanego!!!! 
    while (r-l > 1 ):
        m = l + (r-l) // 2
        if A[m] >= key:
            r = m
        else:
            l = m
    return r



def lis(T):
    n = len(T)
    S = []
    S.append(T[0])
    for i in range(1,n):
        if T[i] >= S[-1]:
            S.append(T[i])
        else:
            S[ceilIndex(S, -1, len(S)-1,T[i])] = T[i]
    return len(S) #zwraca dlugosc!
def mosty ( T ):
    T.sort(key=lambda x: (x[0],x[1])) 
    T2 = [T[i][1] for i in range(len(T))]
    return lis(T2)


runtests ( mosty, all_tests=True )