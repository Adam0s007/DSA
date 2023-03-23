from zad7ktesty import runtests 


def printer(T):
    for i in range(len(T)):
        for j in range(len(T[0])):
            print(T[i][j],end=" ")
        print()

def check_modify(T,x):
    for i in range(len(T)):
        if T[i][x] != 0: return False
    
    for i in range(len(T)):
        T[i][x] = -1

def ogrodnik (T, D, Z, l):
    
    wage = l
    litry = []

    #ozn granic:
    for x in range(len(T[0])):
        check_modify(T,x) 
    

    for x in D:
        max_litr =0
        y = 0
        while y < len(T): #glebokosc
            l,r = x,x
            max_litr += T[y][x]
            l -=1
            r +=1
            while (l >= 0 and T[y][l] != -1) or (r < len(T[0]) and T[y][r] != -1):
                if l >=0 and T[y][l] != -1: 
                    max_litr +=T[y][l]
                    l -=1
                if r < len(T[0]) and T[y][r] != -1:
                    max_litr +=T[y][r]
                    r+=1
            y+=1
        litry.append(max_litr)
    l = wage
    #print(litry)
    dp = [[0 for i in range(l+1)] for j in range(len(Z))]
    for i in range(l+1):
        if litry[0] <= i:
            dp[0][i] = Z[0]
    
    for i in range(1,len(Z)):
        for j in range(l+1):
            if litry[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-litry[i]] + Z[i],dp[i-1][j])
    return dp[-1][-1]




runtests( ogrodnik, all_tests=True )
