from zad1testy import runtests
#1. prog: O(n^2)
#2. prog: O(nlogn)
# mowimy, ze ciag liczb jest typu MR, jesli najpierw jest scisle malejacy a potem scisle rosnacy,
# albo jesli jest tylko scisle malejacy lub tylko scisle rosnacy. Proszę zaimplementować funkcje def mr(X)...
# ktora majac na wejsciu ciag liczb X = [x1,...xn-1] zwraca jeden z jego najdluzszych podciagow typu MR.


#rozwiazanie:
# O(n^2) - przechodzi ledwo 5 testow

#robimy longest increasing subsequence ale tablica dp jest dwuwymiarowa [i][1/0] 
# jak rozpatrujemy ciag malejacy dp[i][m] to operujemy tylko na ciagach malejacych jak w normalnych LIS'ie
#jesli rozpatrujemy ciag rosnacy dp[i][r] to sprawdzamy na danej pozycji ciag rosnacy oraz malejący!!

#nie rozumiem O(nlogn) - problem LIS'a dla szybszej zlozonosci nie zwroci ciągu poprawnego a jedynie dlugosc tego ciagu
def mr( X ):
    """tu prosze wpisac wlasna implementacje"""
    m = 0 #malejacy
    r = 1 #rosnacy
   
    dp = [[1 for i in range(2)] for j in range(len(X))] #dp[i][0]

    # gdy mamy ciag rosnący to musimy rozpatrzyc dwie mozliwosci:
    # patrzymy na wyraz j'ty ktory tez byl rosnący
    # patrzymy na wyraz j'ty ktory byl malejacy, ale stal sie rosnacy [wyraz mr]  

    parent = [[[-1,-1] for i in range(2)] for j in range(len(X))]
    maksim = 0
    index = [0,0]
    for i in range(1,len(X)):
        for j in range(i):
            #jesli X[j] > X[i] to mamy ciag malejacy
            if X[j] > X[i] and dp[i][m] < dp[j][m] + 1:
                dp[i][m] = dp[j][m] + 1 #bo malejacy
                parent[i][m] = [j,m].copy()
                if maksim < dp[i][m]:
                    maksim = dp[i][m]
                    index[0] = i
                    index[1] = m
                             
            elif X[j] < X[i]: 
                if dp[i][r] < dp[j][r] + 1:
                    dp[i][r] = dp[j][r] + 1
                    parent[i][r] = [j,r].copy()
                #musimy sprawdzic podciag malejacy w dp
                if dp[i][r] < dp[j][m] + 1:
                    dp[i][r] = dp[j][m] + 1
                    parent[i][r] = [j,m].copy()
                if maksim < dp[i][r]:
                    maksim = dp[i][r]
                    index[0] = i
                    index[1] = r   
    u = index[0]
    monot = index[1]
    ans = []
    while u != -1:
        ans.append(X[u])
        u,monot = parent[u][monot]
    return list(reversed(ans))
    
runtests( mr )


