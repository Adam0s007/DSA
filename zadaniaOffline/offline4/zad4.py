#Adam Biśta



from zad4testy import runtests

def binary_search(array, searchValue,start_index):
    """
    Binary search for the closest value less than or equal to the search value
    :param array: The given sorted list
    :param searchValue: Value to be found in the array
    :param startIndex: Initialized with 0
    :param endIndex: Initialized with 2**32
    :return: Returns the index closest value less than or equal to the search value
    """
    left = 0
    right = len(array)

    while left < right:
        mid = (left + right) // 2
        if array[mid][2] < searchValue + 1:
            left = mid + 1
        else:
            right = mid
    while left-1 >=0 and array[left-1][2] == array[start_index][1]:
        left -=1
    
    return left - 1



def select_buildings(T,p):
    origin_indexes = {}
    for i in range(len(T)):
        origin_indexes[T[i]] = i
    
    T.sort(key=lambda x: x[2]) #O(nlogn)
    
    
    dp = [[[0,[]] for _ in range(p+1)] for _ in range(len(T))]
    #edge:
    #jesli nas stac:
    for i in range(p+1): 
        if i >= T[0][3]:
            dp[0][i][0]= T[0][0]*(T[0][2]-T[0][1])
            dp[0][i][1].append(T[0])
    ost_i = [binary_search(T,T[i][1],i) for i in range(len(T))]
    
    for i in range(1,len(T)):
        for j in range(p+1):
            dp[i][j][0] = dp[i-1][j][0]
            dp[i][j][1] = dp[i-1][j][1].copy()
            if j >= T[i][3] and dp[i][j][0] < T[i][0]*(T[i][2] - T[i][1]): 
                dp[i][j][0] = T[i][0]*(T[i][2] - T[i][1])
                dp[i][j][1] = []
                dp[i][j][1].append(T[i])


            if j >= T[i][3] and ost_i[i] > -1:
                if T[i][0]*(T[i][2]-T[i][1]) +  dp[ost_i[i]][j-T[i][3]][0] > dp[i][j][0]:
                    dp[i][j][0]= T[i][0]*(T[i][2]-T[i][1]) +  dp[ost_i[i]][j-T[i][3]][0]
                    dp[i][j][1] = dp[ost_i[i]][j-T[i][3]][1].copy()
                    dp[i][j][1].append(T[i])
    
    return [origin_indexes[dp[-1][-1][1][i]] for i in range(len(dp[-1][-1][1]))]
    

runtests( select_buildings )

