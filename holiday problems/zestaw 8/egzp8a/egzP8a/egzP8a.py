from egzP8atesty import runtests 


def binarySearchFloor(values,target):
        l,r = 0,len(values)-1
        res = -1
        while l <= r:
            m = (l+r)//2
            if values[m][0][1] <= target:
                res = m
                l = m + 1  
            else:
                r = m - 1
        while values[res][0][1] == target:
            res -=1 
        return res




def reklamy ( T, S, o ): #O(nlogn)
    newTab = [[T[i],S[i]] for i in range(len(T))]
    newTab.sort(key=lambda x: x[0][1])

    p = [binarySearchFloor(newTab,x[0][0]) for x in newTab]
    
    ans = 0
    #musimy zrobic tablice dp ktora zawiera po jednym najlepszym przedziale po posortowaniu ich ze wzgl na konce
    dp = [0 for k in range(len(newTab))] #1. 0 to najlepszy zysk, drugie 0 -> ilosc wliczonych firm
    dp[0] = newTab[0][1]
    for i in range(1,len(dp)): 
        #kazda nastepna wartosc w tablicy dp to maksymalna z tych co juz wczesniej byly i nowej (jedna!)
        dp[i] = max(dp[i-1],newTab[i][1])
    
    #dla kazdej wartosci z newTab szukamy binary searchem przedzialu niezachodzącego na niego i najlepszego!
    for i in range(1,len(T)):
        second = 0
        if p[i] > -1:
            second = dp[p[i]]
        ans = max(ans, newTab[i][1] + second)
        
        
    return ans

runtests ( reklamy, all_tests=True)