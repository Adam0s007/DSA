from zad9ktesty import runtests
from math import inf

def f(T,DP,i,l1,l2):
    if i > len(T)-1: return 0
    if DP[i][l1][l2] != -1: return DP[i][l1][l2]
    if T[i] > l1 and T[i] > l2: 
        DP[i][l1][l2] = 0
        return 0
    
    if T[i] > l1:
        DP[i][l1][l2] = f(T,DP,i+1,l1,l2-T[i]) + 1 
    elif T[i] > l2:
        DP[i][l1][l2] = f(T,DP,i+1,l1-T[i],l2) + 1
    else:
        w1 = f(T,DP,i+1,l1-T[i],l2)
        w2 = f(T,DP,i+1,l1,l2-T[i])
        DP[i][l1][l2] = max(w1,w2) + 1
    return DP[i][l1][l2]

def prom(P, g, d):
    DP  = [[[-1 for i in range(d+1)] for i in range(g+1)] for i in range(len(P))]
    l2 = d
    l1 = g
    w = f(P,DP,0,g,d)
    
    i = 0
    sol = []
    sol2 = []
    while i < len(P) and (l1 >= P[i] or l2 >= P[i]):
        if P[i] > l1 and P[i] > l2:
            w1 = 0
            w2 = 0
        elif P[i] > l1:
            w1 = 0
            w2 =1
        elif P[i] > l2:
            w1 = 1
            w2 = 0
        else:
            w1 = f(P,DP,i+1,l1-P[i],l2) 
            w2 = f(P,DP,i+1,l1,l2-P[i])
        if w1 > w2:
            sol.append(i)
            l1 = l1 - P[i]
        else:
            sol2.append(i)
            l2 = l2 - P[i]
        i+=1
    if w-1 in sol:#pojazd ostatni ktory wjechal to liczba wszystkich pojazdow minus 1
        return sol
    else:
        return sol2
    #d - l2
    #g - l1
    

runtests ( prom )