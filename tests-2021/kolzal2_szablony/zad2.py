from telnetlib import GA
from zad2testy import runtests
# Pierwszy prog zlozonosci: O(N+M^2)
# Drugi próg zlozonosci: O(N + M)

# Na osi liczbowej znajduje się N punktów większych od M = 10^K. 
# Z punktu A mozna przeskoczyc na punkt B wtedy i tylko wtedy ggdy A%10^k == B//10^K. 
# Proszę zaimplementować funkcję: def order(L,K):... 
# porządkującą punktu, tak aby możliwe było przejście od najwcześniejszego punktu w tym
# porządku, kolejno przez wszystkie punkty, do ostatniego. Funkcja otrzymuje wartości
# określającą położenie punktów na osi liczbowej i powinna zwrócić listę punktów w kolejności ich odwiedzania.
# Jeżeli uporządkowanie punktów nie jest możliwe, funkcja powinna zwrócić None.
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność  czasową i pamięciową
# użytego algorytmu.

#rozwiazanie:
#algorytm eulera
#musimy w nim stworzyć krawędzie (a,b) takie, ze A%10^k == B//10^K

#GFG
def eulerianCircuit(G,v): # O(ElogV)
    curr_path = [v]
    circuit = [] #wlasciwa sciezka Eulera
    while curr_path:
        curr_v = curr_path[-1] #stos

        if G[curr_v]: 
            next_v = G[curr_v].pop()
            curr_path.append(next_v)
        else:
            circuit.append(curr_path.pop()) #cofamy sie jak w dfsie
    return circuit


def order(L,K):
    """tu prosze wpisac wlasna implementacje"""
    edges = [] #graf krawędziowy
    
    hashed = {} #(prefix,sufix) = [num1,num2,...] 102 ,132,...

    maksim = 0

    firstVertice = 0 #od ktorego droga eulera sie zacznie
    for num in L:
        if num//(10**K) != num%(10**K): edges.append((num//(10**K),num%(10**K))) #inaczej to nie mialoby sensu!
        firstVertice = L[0]//(10**K)
        if (num//(10**K),num%(10**K)) in hashed: #moze byc wiele wartosci zaczynajace sie i konczace sie tak samo ( np 151 lub 171)
             hashed[(num//(10**K),num%(10**K))].append(num)
        else:
            hashed[(num//(10**K),num%(10**K))] = [num]

        maksim = max(maksim,num%(10**K),num//(10**K)) 
    G = [[] for i in range(maksim+1)] #skierowany
     # [1,2,4],[2],[],[2,3]
    vertices = {} # wszystkie wierzcholki
    inputed = {} # vertice : countOfEdgesToThisVertice
    outputed = {} # vertice: countOfEdgesFromThisVertice
    for x,y in edges:
        G[x].append(y)
        outputed[x] = outputed.get(x,0) + 1
        inputed[y] = inputed.get(y,0) + 1
        vertices[x] = True
        vertices[y] = True
    
    for u in vertices.keys():
        if outputed.get(u,0) > inputed.get(u,0): #szukamy takiego wierzcholka, do ktorego prowadzi mniej krawedzi niz z niego wyplywa
            firstVertice = u
            
            
    path = eulerianCircuit(G,firstVertice)  
    #suffixy, prefixy,suf...
    ans = []
    
    path = list(reversed(path))
    # pref,suf,pref..
    
    for i in range(1,len(path)): # przetwarzamy krawedzie na liczby
            # [1,3,5,7,9] 1 --> 3 -> 11, 13, 33, 35 , 99 ,79
        if ((path[i],path[i])) in hashed: # prefix == suffixowi
            tab = hashed.get((path[i],path[i])) #gdy mamy np 139491 lub 139391 lub (1...1 poprostu)
            for num in tab:  #10011 ,10201, 12291
                ans.append(num)
        
        
        tab = hashed.get((path[i-1],path[i])) #10102, 10302, 
        ans.append(tab.pop()) # sufix, pref  tab[suf1 == suf2, pref1 == pref2, ale niekoniecznie suf == pref]
        # 103 , 133  3-costam  
        hashed[(path[i-1],path[i])] = tab
        

    #w naszej tablicy path ostatni prefix/sufix moze byc taki ze np 1 a nasza liczba => 10001
    if ((path[-1],path[-1])) in hashed:
        tab = hashed.get((path[-1],path[-1])) #gdy mamy np 139491 lub 139391 lub (1...1 poprostu)
        for num in tab:
            ans.append(num)
    return ans


    #skoro mamy juz caly graf stworzony, to teraz mozemy zastosowac algorytm Eulera
    

    
runtests( order )


