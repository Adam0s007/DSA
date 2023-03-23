# Wyobraźmy sobie podziemny labirynt, złożony z ogromnych jaskiń połączonych wąskimi 
# korytarzami. W jednej z jaskiń krasnoludy zbudowały swoją osadę, a w każdej z pozostałych 
# jaskiń mieszka znana krasnoludom ilość trolli. Krasnoludy chcą zaplanować swoją obronę
# na wypadek ataku ze strony trolli. Zamierzają w tym celu zakraść się i podłożyć ładunek wybuchowy pod jeden 
# z korytarzy, tak aby trolle mieszkające za tym korytarzem nie miały żadnej ścieżki, którą 
# mogłyby dotrzeć do osady krasnoludów. 
# Który korytarz należy wysadzić w powietrze, aby odciąć dostęp do krasnoludzkiej osady największej liczbie trolli?


#rozwiazanie: musimy wysadzić most, znajdujemy krawedzie ktore są mostami!
# po odnalezieniu wszystkich mostow bfsem wyruszymy zaczynajc od wierzcholka z osadą krasnoludków.
# gdy odnajdziemy krawędź mostową to wtedy liczymy wszystkie trolle znajdujace sie za tym mostem.
#zwrócimy krawędź mostową, przy ktorej najwiecej trolli nie dotrze do miasta
# uwaga - optymalizacja - gdy znajdziemy pierwszą krawędź mostową - najblizszą wierzcholkowi s - to 
#stosując np pole visited oznaczymy wszystkie wierzcholki za tym mostem jako odwiedzone, wiec nie bedziemy juz sprawdzac
#wszystkich mostow znajdujących się za tym najblizszym wierzcholkowi s
#inna optymalizacja - stosując dfs mozemy od razu dla wierzcholka mostowego zwrocic ilosc wszystkich troli znajdujących się znajdujących się za mostem


#bedziemy zamiast listy przechowywac w slowniku wartosci bool
from queue import SimpleQueue
class slownik():
    def __init__(self,size):
        self.tab = [[] for i in range(size)]
        self.size = size
    def _hash(self,key): #to bedzie string
    
        total = 0
        prime = 103511  
        #key bedzie intem!
        minim = min(len(key),23)
        for i in range(minim):
            total = (total * prime + i + ord(key[i])) % self.size
        return abs(total)
    
    def _set(self,key,value): #separate chainings 
        index = self._hash(key)
        if len(self.tab[index]) == 0:
            self.tab[index].append([key,value])
        for i in range(len(self.tab[index])):
            if self.tab[index][i][0] == key:
                self.tab[index][i][1] =  value
    
    def _append(self,key,value):
        index = self._hash(key)
        if len(self.tab[index]) == 0:
            self.tab[index].append([key,value])
            return
        for i in range(len(self.tab[index])):
            if self.tab[index][i][0] == key:
                self.tab[index][i][1].append(value)
                return
        #jesli nie znajdziemy klucza, czyli doszlo do kolizji!
        self.tab[index].append([key,[value]])
    
    def _get(self,key):
        index = self._hash(key)
        for i in range(len(self.tab[index])):
            if self.tab[index][i][0] == key:
                return self.tab[index][i][1]
        return False
    
    def _traverse(self):
        for i in range(len(self.tab)):
            for elem in self.tab[i]:
                print((elem[0]," ->",elem[1]))
        print()
        for i in range(len(self.tab)):
            print(self.tab[i])






G = [
[[1,3,9,11],[7]],
[[0,2,4],[7]],
[[1],[7]],
[[0,4,5],[4]],
[[3,1],[6]],
[[6,21,3],[5]],
[[5,7],[8]],
[[8,6],[8]],
[[7],[2]],
[[0,18],[4]],
[[0,13],[4]],
[[0,12],[7]],
[[11,14,13],[5]],
[[10,12],[6]],
[[12,15,17],[9]],
[[14,16],[6]],
[[17,15],[8]],
[[14,16],[9]],
[[9,19],[3]],
[[18,20],[1]],
[[19],[4]],
[[5],[9]]]

def find_best_edge(G,s):
    d = [float("inf") for i in range(len(G))]
    low = [float("inf") for j in range(len(G))]
    parent = [-1 for j in range(len(G))]
    visited = [False for i in range(len(G))]
    
    counter = [0]
    bridges = slownik(len(G)*2)
    def mosty(G,s,counter):
        low[s] = counter[0]
        d[s] = counter[0]
        counter[0] +=1
        visited[s] = True
        for v in G[s][0]:
            if not visited[v]:
                parent[v] = s
                mosty(G,v,counter)
                low[s] = min(low[s],low[v])
            elif parent[s] != v:
                low[s] = min(low[s],d[v])
        if low[s] == d[s] and parent[s] != -1:
            bridges._append(str((parent[s],s)),True)
     
    mosty(G,s,counter)

    def policz(s):
        visited[s] = False
        counter = G[s][1][0]
        for v in G[s][0]:
            if visited[v]:
                counter += policz(v)
        return counter

    #bfs - tym razem nieodwiedzony - true, odwiedzony - False
    maksim = 0
    q = SimpleQueue()
    q.put(s)
    #visited[s] = False
    while not q.empty():
        u = q.get()
        if not visited[u]: continue
        visited[u] = False
        for v in G[u][0]:
            if visited[v]: 
                if bridges._get(str((u,v))):
                    maksim = max(maksim,policz(v))
                else:
                    q.put(v)
    return maksim

    
    #teraz juz mamy te mosty
print(find_best_edge(G,0))

        
