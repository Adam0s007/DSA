
#algorytm do zastosowania: maxFlow, wymyslamy sobie:
#jakies zrodlo podlaczone do kazdej osoby krawedzią o wadze 1
# kazda osoba ma polaczenia do swoich preferencji o wadze 1
#wszystkie pokoje preferowane przez studentow podlaczamy do wymyslonego ujscia o wadze 1

#musimy usunac te wybory uczniow, w ktorych wszedzie dali None, bo ci nie będą mieli karnetow!
#odpalamy edmunda karpa, dla poprawy zlozonosci najlepiej uzyc postaci listy sadziedztwa dla grafu

from egzP7atesty import runtests 
from collections import deque


def bfs(graph, s, t, parent):
    visited = [False]*(len(graph))
    queue = deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.pop()
        for v,w in graph[u].items():
            if visited[v] == False and w > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True
    return False

def edmund_karp_adjacency(graph,source, sink):
    parent = [-1]*(len(graph))
    max_flow = 0

    
    while bfs(graph,source, sink, parent) :
        path_flow = float("Inf")
        v = sink
        #znajdowanie najmniejszego przeplywu na danej sciezce
        while(v !=  source):
            path_flow = min(path_flow, graph[parent[v]][v])
            v = parent[v]
        max_flow +=  path_flow
        v = sink
        #usuwanie / dodawanie najmniejszego przeplywu miedzy krawedziami na danej sciezce
        while(v !=  source):
            u = parent[v]
            graph[u][v] = graph[u].get(v) - path_flow
            graph[v][u] = graph[v].get(u) + path_flow #residual edge!!! czyli taka odwrotna! pozwala na cofanie sie!
            v = parent[v]
    return max_flow

def akademik( T ):
    maxNumOfAkad = 0
    count = 0
    newTab = []
    for tup in T:
        if tup[0] != None: maxNumOfAkad = max(maxNumOfAkad,tup[0])
        if tup[1] != None: maxNumOfAkad = max(maxNumOfAkad,tup[1])
        if tup[2] != None: maxNumOfAkad = max(maxNumOfAkad,tup[2])
        if tup[0] != None or tup[1] != None or tup[2] != None: 
            count +=1
            newTab.append(tup) #wszystkie dobre rzeczy
    
    
    #najwiekszyNrPokoju teraz mamy ustalony
    # teraz potrzebujemy wszystkie osoby, ktore posiadają jakies preferencje
    # musimy dodac jeszcze 2 wierzcholki oznaczajace zrodlo i ujscie
    zr = maxNumOfAkad + count + 1
    sink = zr + 1
    firstPerson = maxNumOfAkad + 1
    G = [{} for i in range(sink+1)]
    for i,tup in enumerate(newTab):
        if tup[0] != None:
            #z pokoju do ujscia:
            G[tup[0]][sink] = 1
            G[sink][tup[0]] = 0

            #z osoby do pokoju
            G[firstPerson+i][tup[0]] = 1
            G[tup[0]][firstPerson+i] = 0
            
            #ze zrodla do osoby 
            G[zr][firstPerson+i] = 1
            G[firstPerson+i][zr] = 0
        if tup[1] != None:
            #z pokoju do ujscia:
            G[tup[1]][sink] = 1
            G[sink][tup[1]] = 0

            #z osoby do pokoju
            G[firstPerson+i][tup[1]] = 1
            G[tup[1]][firstPerson+i] = 0
            
            #ze zrodla do osoby 
            G[zr][firstPerson+i] = 1
            G[firstPerson+i][zr] = 0
        if tup[2] != None:
            #z pokoju do ujscia:
            G[tup[2]][sink] = 1
            G[sink][tup[2]] = 0
    
            #z osoby do pokoju
            G[firstPerson+i][tup[2]] = 1
            G[tup[2]][firstPerson+i] = 0
            
            #ze zrodla do osoby 
            G[zr][firstPerson+i] = 1
            G[firstPerson+i][zr] = 0
    moneys = edmund_karp_adjacency(G,zr,sink) #to jest maxflow
    return count - moneys

runtests ( akademik )