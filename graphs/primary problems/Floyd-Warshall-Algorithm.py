# Floyd Warshall Algorithm in python


# The number of vertices
nV = 4

INF = 999
#in matrix representation of graphs G[i][j] -> i - vertex, j - destination vertex from vertex i so -> edge is from i to j

def propagateNegativeCycles(dp,parent):
    #Execute FW APSP algorithm a second time but
    # this time if the distance can be improved 
    # set the optimal distance to be -inf. 
    # Every edge (i,j) marked with -inf is either 
    # part of ir reaches into a negative cycle 
    for k in range(len(dp)):
        for i in range(len(dp)):
            for j in range(len(dp)):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = -1 * INF
                    parent[i][j] = -1


def reconstructPath(dp,parent,start,end):
    path = []
    #check if there exists a path between the starts and end node.
    if dp[start][end] == INF: return path 
    #reconstructing path from parent matrix
    at = start
    while at != end: 
        if at == -1: return []
        path.append(at)
        at = parent[at][end]
#wczesniej parent[i][j] = j
#teraz: at = parent[at][end]  
    if parent[at][end] == -1: return []
    path.append(end)
    return path

# Algorithm implementation
def floyd_warshall(G):
    dp = [[0 for i in range(len(G))]for j in range(len(G))]
    parent = [[-1 for i in range(len(G))] for j in range(len(G))] #for reconstructing the shortest path from vertices
    
    for i in range(len(G)):
        for j in range(len(G)):
           dp[i][j] = G[i][j] 
           if G[i][j] != INF:
               parent[i][j] = j #from i to j, therefore for i we choose j
    # Adding vertices individually
    for k in range(nV): # nV - nr of vertices
        for i in range(nV):
            for j in range(nV):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    parent[i][j] = parent[i][k]
    #addition for < 0 weights:
    # detect and propagate negative cycles:
    #propagateNegativeCycles(dp)

    print_solution(dp)
    print(reconstructPath(dp,parent,2,3))


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[0, 3, INF, 5],
     [2, 0, INF, 4],
     [INF, 1, 0, INF],
     [INF, INF, 2, 0]]
floyd_warshall(G)