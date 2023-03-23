


#problem plecakowy
def plecak(W,P,n): #W - wagi, P - wartosci , n - maks. waga
    T = [[0 for _ in range(n+1)] for _ in range(len(W))]
    for i in range(n+1):
        if W[0] <= i: T[0][i] = P[0]
    
    for i in range(1,len(W)):
        for j in range(n+1):  
            if j - W[i] < 0:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j],P[i] + T[i-1][j-W[i]]) #nie bierzemy, bierzemy!
    return [T[len(W)-1][n],traverse_ans(T,P,W,len(W)-1,n)]


def traverse_ans(dp,P,W,i,j):
    ans = []
    def rek_traverse(dp,i,j):
        if i>0 and dp[i][j] == dp[i-1][j]:
            rek_traverse(dp,i-1,j)
        elif i>=0 and j>=0:
            rek_traverse(dp,i-1,j-W[i])
            ans.append(i)
    rek_traverse(dp,i,j)
    return ans

ceny = [1,3,5,7,8,2]
wagi = [1,2,2,3,4,9]
print(plecak(wagi,ceny,18))



def f(W,P,n,i,tab):
    if i  < 0 or n <=0: 
        return 0
    return max(f(W,P,n-W[i],i-1, tab) + P[i],f(W,P,n,i-1,tab))

#mamy tablice liczb naturalnych, czy istnieje podzbior elementow z tej tablicy, ze suma elementow = N?
#A - tablica
def podz_elem(A,n,i,results,has_result):
    if n == 0: return True
    if i < 0 or n < 0: return False
    if not has_result[n][i]: results[n][i] = f(A,n,i-1,results,has_result) or f(A,n-A[i],i-1,results,has_result)
    return results[n][i]

#ciagi macierzy
def f2(M,i,j): # i == j, 0 |  j =/= i => min(f(M,i,k) + f(M,k+1,j) g(M,i,j,k))
    pass

#nominały 
#O(n)
# f(k,N):
#  1) 1, k e N
#  2) 0, dla kazdego n e N  k < n
#  3) dla n e N: min({ f(k-n,N) | n <=k }) +1

# A = [1,7,3,2,9,5]
# B = [3,5,2,7,9]

#znajdz najdluzszy wspolny podciag miedzy tablicami A i B
#w O(n^2)
# f(A,B,i,j):
#  1) f(A,B,i-1,j-1) + 1, A[i]== B[j]
#  2) max(f(A,B,i-1,j),f(A,B,i,j-1)) w p.p.
#  3) 0, i < 0 || j < 0
# f(A,B,||A||-1,||B||-1)


#znajdz najdluzszy podciag rosnacy w tablicy A

#f(A,sorted(A),||A||-1,||A||-1) w nlogn zad dom


