# Given a list of jobs which has a start,finish time and a profit/weight associated with it:
# we want to find the subset with the maximum weight where each job is disjoint
# (The jobs cannot occur at the same time)

#for a job i we have [s,f,w] [starting time, finish time, weight]
import bisect 

def binary_search(T,value,init_index): #bedziemy szukac po starting Pointcie Akademika! Najblizszy ending point innego akademika!
    l,r = 0,len(T)-1
    middle = None
    while l <= r:
        middle = (r+l)//2
        if T[middle][1] > value: r = middle - 1
        elif T[middle][1] < value: l = middle + 1
        else: return middle
    if middle == None: return -1
    if middle == init_index and init_index == 0: return -1
    if middle < 0 or middle > len(T): return -1
    if T[middle][1] < value: return middle
    return middle-1


def previous_intervals(I):
    p = []
    start =[task[0] for task in I]
    finish = [task[1] for task in I]

    for i in range(len(I)):
        idx = bisect.bisect(finish, start[i]) - 1 #we are looking for a first value in arr finish, which is lower than start[i]
        p.append(idx)
    return p 


def find_solution(j):
    if j == -1:
        return
    else:
        if (I[j][2] + OPT[p[j]] >= OPT[j-1]): #gdy ta nierownosc zajdzie to tylko wtedy wiemy ze zabralismy element pod I[j]
            O.append(I[j])
            find_solution(p[j])
        else:
            find_solution(j-1)

def compute_opt(j):
    #Use recursive formula max(W(j) + OPT(p(j)), OPT(j-1))
    if j == -1: return 0
    #elif (0 <= j) and (j < len(OPT)): return OPT[j]
    else: return max(I[j][2] + compute_opt(p[j]),compute_opt(j-1))


def weighted_interval(I):
    for j in range(len(I)):
        opt_j = compute_opt(j)
        OPT.append(opt_j)
    find_solution(len(I)-1)
    return OPT[-1]

if __name__ == '__main__':
    #OPT for optimal weight, O for best items to pick 
    OPT = []
    O = []
    #they are labeled as: (start,end,weight)

    t1 = (0,3,3)
    t2 = (1,4,2)
    t3 = (0,5,4)
    t4 = (3,6,1)
    t5 =  (4,7,2)
    t6 = (3,9,5)
    t7 = (5,10,2)
    t8 = (8,10,1)

    I = [t1,t2,t3,t4,t5,t6,t7,t8]
    I.sort(key= lambda tup: tup[1])
    p = previous_intervals(I)
    print(weighted_interval(I))
    print(O[::-1])
