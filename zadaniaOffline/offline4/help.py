
def traverse_check_czyPokrywaja(dp,i,j,T,a):
    if i>0 and dp[i][j] == dp[i-1][j]:
        return traverse_check_czyPokrywaja(dp,i-1,j,T,a)
    elif i>=0 and j>=0: 
        if a != i and ((T[i][1] <= T[a][1] <= T[i][2]) or (T[i][1] <= T[a][2] <= T[i][2]) or\
           ( T[a][1] <= T[i][1] <= T[a][2] ) or (T[a][1] <= T[i][2]  <= T[a][2])):
            return True
        return traverse_check_czyPokrywaja(dp,i-1,j-T[i][3],T,a)
    return False

def traverse_ans(dp,i,j,T):
    ans = []
    def rek_traverse(dp,i,j):
        if i>0 and dp[i][j] == dp[i-1][j]:
            rek_traverse(dp,i-1,j)
        elif i>=0 and j>=0:
            rek_traverse(dp,i-1,j-T[i][3])
            ans.append(i)
    rek_traverse(dp,i,j)
    return ans




def check(ans,i,T):
    for j in ans:
        if (T[i][1] <= T[j][1] <= T[i][2]) or\
            (T[i][1] <= T[j][2] <= T[i][2]) or\
            (T[j][1] <= T[i][1] <= T[j][2]) or\
            (T[j][1] <= T[i][2] <= T[j][2]):
            return False
    return True



def select_buildings(T,p):
    # tu prosze wpisac wlasna implementacje
    dp = [[[0,[]] for i in range(p+1)] for j in range(len(T))]
    def rekur(T,p,i,ans=[]):
        
        if i >= len(T):
            return 0,[]
        
        if dp[i][p][0]:
            return dp[i][p]
        else:
            first,tab1 = rekur(T,p,i+1,ans)
            sec = 0
            tab2 = []
            if p - T[i][3] >= 0 and check(ans,i,T):
                sec,tab2 = rekur(T,p-T[i][3],i+1,[*ans,i])
                if i not in tab2:
                    if check(tab2,i,T) == True:
                        tab2.append(i)
                        sec += T[i][0]*(T[i][2]-T[i][1])
                
            dp[i][p] = [first,tab1] if first > sec else [sec,tab2]
            return dp[i][p] 
    
    a = rekur(T,p,0)
    for i in range(len(T)):
        for j in range(p+1):
            print(dp[i][j][0],end=" ")
        print()
    return a[1]
        

#T = [(5, 3, 4, 11), (6, 5, 7, 3), (3, 2, 3, 11), (3, 11, 21, 19), (4, 12, 15, 6), (3, 7, 9, 7), (2, 2, 3, 15)]
#T = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)]

T = [(7,11,28,23),(6,11,18,91),(3,6,7,75),(3,21,76,95),(3,1,88,35),(4,1,2,3)]
p = 150
print(select_buildings(T,p))