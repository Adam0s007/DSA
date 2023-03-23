# Dany jest graf ważony z dodatnimi wagami G. Dana jest też lista E' krawędzi,
# które nie należą do grafu, ale są krawędziami między wierzchołkami z G.
# Dane są również dwa wierzchołki s i t. Podaj algorytm, który stwierdzi, którą jedną krawędź
# z E' należy wszczepić do G, aby jak najbardziej zmniejszyć dystans między s i t. 
# Jeśli żadna krawędź nie poprawi dystansu między s i t, to algorytm powinien to stwierdzić.



#rozwiazanie:
# kazdy wierzcholek rozbijamy na dwa:
# ten w ktorym wykorzystalismy krawedz z E' (bądź też nie, ale tutaj to dopuszczamy)
# ten w ktorym nie wykorzystalismy krawedzi z E'

# niech s e V dow. ust: s [s,s']
# s -> nie wykorzystalismy  krawedzi z E' 
# s' -> wykorzystalismy jakas krawedz z E'


#mamy dane dwa wierzcholki s,t ktore maja polaczenie nie nalezace do E':
# wtedy:
#s' -----> t' - tutaj relaksacja
#s-----> t - tutaj relaksacja

# mamy ten sam wierzcholek s' ktory posiada polaczenie z wierzch. 'o' nalezace do E'
#wtedy:
# s -----> o' - tutaj relaksacja! (jesli poprzednio byla uwzgledniona jakas krawedz z E, to tu zostanie nadpisana!)



def Bellam_ford(G,V,E,s,t): #V - nr of vertives
    d = [[float("inf"),float("inf")] for i in range(V)] # dla kazdego v istnieje v'
    parent = [[[-1,-1] for i in range(2)] for i in range(V)]
    d[s][0] = 0 
    d[s][1] = 0 
    Graph = []
    for u,v,w in G:
        Graph.append((u,v,w,False)) #False - to nie jest krawedz z E' 
    for u,v,w in E:
        Graph.append((u,v,w,True))
    
    for i in range(V-1):
        for u,v,w,f in Graph:
            if f == False: 
                if d[u][0] + w < d[v][0]:
                    d[v][0] = d[u][0] + w
                    parent[v][0][0] = u 
                    parent[v][0][1] = 0  
                if d[u][1] + w < d[v][1]: #nw czy tu powinny byc obie relaksacje, wiec dalem obydwie na wszelki wypadek
                    d[v][1] = d[u][1] + w
                    parent[v][1][0] = u 
                    parent[v][1][1] = 1 
            else:
                if  d[u][0] + w < d[v][1]: #sytuacja z dodatkową krawedzią! w to waga krawedzi dodatkowej!!
                    d[v][1] = d[u][0] + w 
                    parent[v][1][0] = u 
                    parent[v][1][1] = 0 
    ans = []
    if d[t][1] == d[t][0]: print("żadna krawędź nie poprawi dystansu między s i t")
    ind = 1
    while t != -1:
        ans.append([t,ind])
        t,ind = parent[t][ind]
    ans.reverse()
    print(ans)
    for i in range(1,len(ans)):
        if ans[i][1] != ans[i-1][1]:
            return (ans[i-1][0],ans[i][0]) 





G =  [(0,2,4),(2,1,7),(2,3,1),(3,4,5),(4,5,5)] 
''' (ui,vi,wi) -> ui - skad, vi - dokad,
wi - waga krawedzi '''
E = [(0,1,1),(0,2,3),(2,4,8),(2,5,2)]
print(Bellam_ford(G,6,E,0,5))