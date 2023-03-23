from zad12testy import runtests


#robimy graf, wierzcholkami są początki krotek, natomiast z tych poczatkow wychodzą krawędzie do koncow krotek!

def intuse( newTab, start, end ):
    #slownik edges sie nie przyda jednak, ale warto dac co takiego aby nie bylo zdublowanych krawedzi
    # wiemy ze mogą wystapic w testach zdublowane krawedzie, ale to wszystko nam mapuje slownik indexes zawierajacy tablice
    # indeksow ktore mają te same przedzialy 
    G = {x[0]:[] for x in newTab}
    edges = {}
    indexes = {}
    for ind,(x,y) in enumerate(newTab):
        if(x,y) not in edges and (y,x) not in edges:
            edges[(x,y)] = 1
            G[x].append(y)
            indexes[(x,y)] = [ind]
        elif (x,y) in edges:
            edges[(x,y)] = edges.get((x,y)) + 1
            indexes[(x,y)].append(ind)
        elif (y,x) in edges:
            edges[(y,x)] = edges.get((y,x)) + 1
            indexes[(x,y)].append(ind)
    
    #edges - przedzialy
    #indexes - indeksy
    visited = {}
    #gdy dajemy 1 to oznajmiamy ze zostal wierzcholek odwiedzony, ale nie wiemy czy sie dostaniemy
    # gdy dajemy 2 to oznajmiamy ze dostaniemy sie do y
    # gdy wierzcholka nie ma w visited no to musimy go przetworzyc
    def dfs(u):
        if u not in visited:
            visited[u] = 1
         #dostajemy sie!
        #gdy osiagniemy end point!
        if u == end: 
            visited[u] = 2
            return True

        czyDaSie = False
        if u not in G: return False # z tego wierzcholka nie wychodzi zadna krawedz czyli go poprostu nie ma
        for v in G[u]:
            if v not in visited:
                dojdziemy = dfs(v)
                if dojdziemy: 
                    czyDaSie = True
            elif visited.get(v) == 2: 
                czyDaSie = True
        if czyDaSie: 
            visited[u] = 2
            return True
        return False
    
    dfs(start)
    ans = []
    for key,value in indexes.items():
        if visited.get(key[0])== 2 and visited.get(key[1]) == 2:    
            for elem in value:
                ans.append(elem)
    return ans


runtests( intuse )
#T = [
#print(intuse(T,1,10))

#T = [[3, 4], [2, 5], [1, 3], [4, 6], [1, 4]]
# T = [(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9), (7, 10), (8, 11), (9, 12)]
# print(intuse(T,0,13))