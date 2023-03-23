# Dostajemy tablicę (M x N) wypełnioną wartościami (kosztem wejścia).
# Możemy znaleźć minimalny koszt potrzebny do dostania się 
# z pozycji [0][0] do [M-1][N-1] 
# Wprowadzimy pewne ustalenia:
# 1. Możemy poruszać się tylko w bok i w dół
# 2. Wszystkie koszty są dodatnie
import heapq

#O(M*Nlog(M*N))
def path_sum(T):
    visited = set()
    
    q = [[0,(0,0)]]
    dist = [[float("inf") for i in range(len(T[0]))] for j in range(len(T))]
    dist[0][0] = T[0][0]
    ROWS,COLS = len(T),len(T[0])
   #             (y,x)
    positions = [(0,1),(0,-1),(1,0)]
    while q:
        cost,u = heapq.heappop(q)
        i,j = u
        if u in visited: continue
        visited.add(u)
        for y,x in positions:
            if i+y < 0 or i+y >= ROWS or j+x < 0 or j+x >= COLS: continue
            if dist[i+y][j+x] > dist[i][j] + T[i+y][j+x]:
                dist[i+y][j+x] = dist[i][j] + T[i+y][j+x]
                heapq.heappush(q,[dist[i+y][j+x],(i+y,j+x)])
    
    return dist[ROWS-1][COLS-1]
    
T = [ 
    [    10,    10,10,100000],
    [10000,100000,10,10000],
    [     10,   10,10,10000],
    [ 10,10000,1000000,100000],
    [10,10         ,10,    10]
]

print(path_sum(T))