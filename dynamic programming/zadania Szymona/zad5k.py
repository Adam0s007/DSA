from zad5ktesty import runtests

def garek ( A ):
    lookup = [[0 for x in range(len(A))] for y in range(len(A))]
    def findMaxCoins(coin, i, j, lookup):
        if i == j:
            return coin[i]
        if i + 1 == j:
            return max(coin[i], coin[j])
        if lookup[i][j] == 0:
            start = coin[i] + min(findMaxCoins(coin, i + 2, j, lookup),
                                findMaxCoins(coin, i + 1, j - 1, lookup)) 
            end = coin[j] + min(findMaxCoins(coin, i + 1, j - 1, lookup),
                                findMaxCoins(coin, i, j - 2, lookup)) 
            lookup[i][j] = max(start, end)
        return lookup[i][j]
    return findMaxCoins(A, 0,len(A)-1,lookup)
    
runtests ( garek )