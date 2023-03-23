from zad12ktesty import runtests 



# def sum(T, frm, to):
#     total = 0
#     for i in range(frm, to + 1):
#         total += T[i]
#     return total
# def s(T,j,i,dpSum):
#     if dpSum[j][i]: return dpSum[j][i]
#     dpSum[j][i] = sum(T,j,i)
#     return dpSum[j][i]

# def autostrada( T, k ): #tworzymy sumy w przedzialach, returned zawiera najwiekszą z nich
#     #a naszym zadaniem jest zwrocenie minimalnej sumy z tych sum
#     dpSum = [[0 for i in range(len(T)+1)] for j in range(len(T)+1)]
#     dp = [[0 for i in range(len(T) + 1)] for j in range(k + 1)]
    
#     def s(T,j,i):
#         if dpSum[j][i]: return dpSum[j][i]
#         dpSum[j][i] = sum(T,j,i)
#         return dpSum[j][i]

#     # base cases
#     # k=1
#     for i in range(1, len(T) + 1):
#         dp[1][i] = s(T, 0, i - 1)
 
#     # n=1
#     for i in range(1, k + 1):
#         dp[i][1] = T[0]
 
#     # 2 to k partitions
#     for i in range(2, k + 1): # 2 to n boards
#         for j in range(2, len(T) + 1):
      
#             # track minimum
#             best = 100000000
             
#             # i-1 th separator before position T[p=1..j]
#             for p in range(1, j + 1):
#                 best = min(best, max(dp[i - 1][p],s(T, p, j - 1)))    
#             dp[i][j] = best
#     return dp[k][len(T)]


# def autostrada( T, k ):
#     dp = [[0 for i in range(len(T)+1)] for j in range(k + 1)]
#     dpSum = [[0 for i in range(len(T)+1)] for j in range(len(T)+1)]
#     def partition(arr, n, k):
#         # base cases
#         if k == 1: # one partition
#             return s(arr, 0, n - 1,dpSum)
#         if n == 1: # one board
#             return arr[0]
#         if dp[k][n]: return dp[k][n]
#         best = float("inf")
#         for i in range(1, n):
#             best = min(best,max(partition(arr, i, k - 1),s(arr, i, n - 1,dpSum)))
#         dp[k][n] = best
#         return dp[k][n]
#     return partition(T,len(T),k)
def autostrada( nums, m ):
    dp = [[0 for i in range(m+1)] for j in range(len(nums))]
    def dfs(i,m):
        if m == 1:
            return sum(nums[i:])
        if dp[i][m]: return dp[i][m]
            
        res, curSum = float("inf"), 0
        for  j in range(i,len(nums)-m +1):
            curSum += nums[j]
            maxSum = max(curSum,dfs(j+1,m-1))
            res = min(res,maxSum)

            if curSum > res: break
        dp[i][m] = res
        return res
    return dfs(0,m)
     



runtests ( autostrada,all_tests=True )