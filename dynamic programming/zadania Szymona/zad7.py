from zad7ktesty import runtests

def ogrodnik (T, D, Z, l):
    n = len(T)
    d = 0
    for x in T[0]:
        d += 1
    granice = [0]
    for x in D:
        flag = True
        while flag and x < d-1:
            x += 1
            for i in range(n):
                if T[i][x] != 0:
                    break
            else:
                granice.append(x)
                flag = False
    granice.append(n-1)
    j = 0
    for polozenie in D:
        for i in range(1, n):
            T[0][polozenie] += T[i][polozenie]
            k = polozenie
            x = T[i][polozenie]

            while k-1 != granice[j]:
                if k - 1 < 0: break
                x = T[i][k-1]
                T[0][polozenie] += x
                k -= 1

            x = T[i][polozenie]
            k = polozenie

            while k+1 != granice[j+1]:
                if k + 1 > d-1: break
                x = T[i][k + 1]
                T[0][polozenie] += x
                k += 1

        j += 1
    B = []
    for i in range(d):
        if T[0][i] != 0:
            B.append(T[0][i])
    print(B)
    m = len(D)
    dp = [[0 for _ in range(l+1)] for _ in range(m)]
    for i in range(T[0][D[0]], l+1):
        dp[0][i] = Z[0]

    for j in range(l+1):
        for i in range(1,m):
            dp[i][j] = dp[i-1][j]
            if j - B[i] >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j - B[i]] + Z[i])


    return dp[m-1][l]

runtests( ogrodnik, all_tests= False)