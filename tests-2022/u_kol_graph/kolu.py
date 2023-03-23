#from kolutesty import runtests

from collections import deque
def swaps( disk, depends ):
    #G - depends
    visited = set()
    parents_counter = [0 for i in range(len(depends))] #to tak naprawde reversed graph
    #nie mozemy wejsc bfsem do wierzcholka jest jego ilosc rodzicow jest wieksza od 2
    
    #zadziala bo graf jest nieskierowany
    for i in range(len(depends)):
        for v in depends[i]:
            parents_counter[v] +=1
    
    border_vertices = []
    new_border_vertices = []
    def bfs(u):# 
        #przetwarzamy wierzcholek
        q = deque()
        q.append(u)
        while q:
            u = q.popleft()
            if u not in visited: 
                visited.add(u)  
                for v in depends[u]:
                    if v in visited: continue #jesli juz go przetworzylismy to nie ma sensu tam isc
                    if disk[v] == disk[u] and parents_counter[v] == 1: #czyli zalezy wierzcholek juz tylko od naszego!
                        parents_counter[v] -=1 #zmniejszamy 
                        q.append(v)
                    elif parents_counter[v] > 1: #bez wzgledu na to czy jest to wierzcholek innego koloru czy tego samego
                        # nie mozemy tam wejsc bo zalezy od jeszcze innego wierzcholka, wiec musimy tylko zmniejszyc licznik parentow
                        parents_counter[v] -=1
                        #jednak nie wolno nam wejsc do wierzcholka! gdyz zalezy on jeszcze od innego ktory musi byc wczesniej
                    elif disk[v] != disk[u] and parents_counter[v] == 1: # jesli tak jest, to dodajemy wierzcholek innego koloru
                        # do listy z wierzcholkami granicznymi (pierwsze o innym kolorze)
                        new_border_vertices.append(v)
                        parents_counter[v]-=1
 
    #co na poczatku wybieramy dla border_vertices? wszystkie wierzcholki ktore nie mają parentow!
    
    for i in range(len(parents_counter)):
        if not parents_counter[i]: border_vertices.append(i)
    changes = 0
    

    while len(border_vertices): #dopoki istnieją jakiekolwiek wierzcholki graniczne  to algorytm musi dzialac
        for u in border_vertices:
            bfs(u) #bfs
        if len(new_border_vertices):  #jesli dodajemy tutaj cokolwiek to oznacza ze bedziemy robic change! wiec dodajemy 1 do changes
            changes += 1
        border_vertices = new_border_vertices.copy()
        new_border_vertices = []
    return changes
    




depends = [[4,1],[3,4,2],[],[],[3,5,6],[],[]]
disk = ['A','A','B','B','B','A','A']
print(swaps(disk,depends))
depends = [[2,1],[4,5,6],[3,4],[7,8],[9],[10,11],[11],[],[],[],[],[]]
disk =  ['A','A','B','A','B','A','A','A','A','A','B','A']
print(swaps(disk,depends))


# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( swaps, all_tests = True )

