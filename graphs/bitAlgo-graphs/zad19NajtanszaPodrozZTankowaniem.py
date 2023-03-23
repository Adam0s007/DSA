# Dostajemy na wejściu graf, w którym wierzchołkami są miasta,
# a krawędziami drogi między nimi. Dla każdego miasta znamy cenę paliwa w złotych na litr, 
# a dla każdej drogi jej długość w kilometrach. 
# Nasz samochód ma zbiornik pojemności 100 litrów i pali jeden litr na kilometr.
# Startujemy z miasta A z pustym zbiornikiem. Ile minimalnie musimy zapłacić za paliwo,
# aby dotrzeć do miasta B? 



#Rozwiazanie:
# Ogolnym rozwiazaniem bedzie zastosowanie dijkstry, ale to bedzie ciekawe.
# definiujemy wierzchołki A0,A1,A2....A100 - gdzie:1) A -> nr danego wierzcholka (miasto w ktorym jestesmy), 
#                                                  2) 0..100 -> ilosc paliwa jaką aktualnie posiadamy
#  wiemy ze krawedz ma daną wagę, ktora oznacza utratę paliwa - a wiec jesli krawedz miedzy miastami
# A oraz B miala wagę 2, to wtedy robimy odpowiednie polaczenia: A0 - [] , A1 - [], A2 - B0 , A3 - B1 ... A100 - B98 
# w naszym nowym grafie definiujemy od nowa wagi krawędzi:
# np miedzy miastami (z przykladu wyzej: A0 - [] , A1 - [], A2 - B0 , A3 - B1 ... A100 - B98 ) - wagi wynoszą 0 
# w miescie mozemy tankowac ale nie wiemy do ilu. Przyjmijmy ze koszt to 7zl/litr, tak więc: B0 -> B1 waga: 7
# B0 -> B2 waga: 2*7 to 14, ale zauwazmy, że to to samo co B0 -> B1 -> B2 waga: 14

# na takim grafie puszczamy dijkstrę

#dla potrzeb implementacyjnych zalozmy ze mamy 10-litrowy bak
from queue import PriorityQueue
def samochod(G,a,b,max_capacity):
    minkoszt = [[float("inf") for i in range(max_capacity)] for j in range(len(G))] #tablica dwuwymiarowa!
    visited = [[False for i in range(max_capacity)] for j in range(len(G))]
    parent = [[[-1,-1] for i in range(max_capacity)] for j in range(len(G))]
    # w miescie a musimy zatankowac bak, a wiec musimy zaplacic 
    #initializing:
    q = PriorityQueue()
    for i in range(max_capacity):
        minkoszt[a][i] = G[a][1] + G[a][1]*i
        q.put((minkoszt[a][i],(a,i))) #np A0, A1, itp. tak jak przyjalem w oznaczeniach: i to ilosc paliwa!

    while not q.empty():
        cost, tuple = q.get()
        u, paliwo = tuple #np A2 - z niego mozemy sie dostac np do B0 lub C0.. z koncowką 0 gdy km = 2
        if visited[u][paliwo]: continue
        visited[u][paliwo] = True
        
        for v,km in G[u][0]:
            if paliwo - km < 0 or visited[v][paliwo-km]: continue #czyli na danym paliwie nie dojedziemy do pewnego wierzcholka
            #jesli tam juz bylismy to nie wchodzimy tam juz
            # zapamietajmy jedno: A2 -> B0 jesli dla drogi waga wynosi 2 itd
            if minkoszt[v][paliwo-km] > minkoszt[u][paliwo]:
                
                parent[v][paliwo-km][0] = u
                parent[v][paliwo-km][1]= paliwo

                minkoszt[v][paliwo-km] = minkoszt[u][paliwo]
                q.put((minkoszt[v][paliwo-km],(v,paliwo-km)))
        #sprawdzilismy polaczenia do innych miast, ale teraz musimy sprawdzic
        # polaczenia takie jak B0->B1->B2 itd.
        for i in range(paliwo+1,max_capacity):
            if visited[u][i]: continue #przetworzony juz aktualnie
            cost += G[u][1]
            if minkoszt[u][i] > cost:
                parent[u][i][0] = u
                parent[u][i][1]= paliwo
                minkoszt[u][i] = cost
                
                q.put((minkoszt[u][i],(u,i)))
    
    min_c = float("inf")
    indx = 0
    for i in range(len(minkoszt[b])):
        if min_c > minkoszt[b][i]: 
            indx = i 
            min_c = minkoszt[b][i]
    tab=[]
    while b != -1:
        tab.append(str(chr(b+ ord('A'))))
        tab.append(str(indx))
        print("".join(tab),end=" ")
        tab.clear()
        b,indx = parent[b][indx]
    
    return min(minkoszt[b])

    
        







G = [([(1,1),(2,2)],8),([(0,1),(2,3),(3,2)],8),([(0,2),(1,3),(3,1),(4,3)],4),([(1,2),(2,1),(4,2),(5,4)],6),([(2,3),(3,2),(5,1),(6,2)],3),([(3,4),(4,1),(6,1)],2),([(4,2),(5,1)],3)]
print(samochod(G,0,6,100))
