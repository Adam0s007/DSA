from egzP8btesty import runtests

def floydWarshall(M): #O(n^3)
    for k in range(len(M)):
        for i in range(len(M)):
            for j in range(i,len(M)):
                if M[i][j] > M[i][k] +  M[k][j]:
                    M[i][j] = M[i][k] +  M[k][j]
                    M[j][i] = M[j][k] +  M[k][i]
def robot( G, P ):
    M = [[float("inf") for i in range(len(G))] for j in range(len(G))]

    for u in range(len(G)):
        for v,w in G[u]:
            M[u][v] = w
            M[v][u] = w     
    floydWarshall(M)

    dist = 0
    for i in range(len(P)-1):
        dist += M[P[i]][P[i+1]]

    return dist
    
runtests(robot, all_tests = True)
