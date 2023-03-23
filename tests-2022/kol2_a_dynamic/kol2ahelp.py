from kol2atesty import runtests
def drivers( P, B ):
    n = len(P)
    dp =[[[float("inf") for i in range(2)] for j in range(2)] for k in range(n+1)]
    # dp[z][m][n] - [range(n)]range(m)]]range(z)]

    przesiadki =  []
    for i in range(len(P)):
        if P[i][1] == True:
            przesiadki.append((P[i][0],i))
           

    
    def dynamic(i,k,p): #i - iterator po tablicym k - ilosc ominietych punktow przesiadkowych przez daną osobę
        if i == n:                # p - Marian albo not MARIAN
            return 0
        if dp[i][k][p] != float("inf"): return dp[i][k][p]

        if k == 3: 
            dp[i][k][p] = dynamic(i+1,0,not p)

        else:
            if p: 
                dp[i][k][p] = (przesiadki[i][0] - przesiadki[i-k][0] - k  + min(dynamic(i+1,k+1,p),dynamic(i+1,0,not p)))
            else: 
                dp[i][k][p] =  min(dynamic(i+1,k+1,p),dynamic(i+1,0,not p))
        return  dp[i][k][p]
        
    

    

        
        
                

runtests( drivers, all_tests = True )