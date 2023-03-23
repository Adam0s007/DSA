# Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu 
# ważonego, który odpowiada mapie drogowej (wagi przedstawiają odległości a liczba -1 oznacza brak 
# krawędzi). W niektórych wierzchołkach są stacje paliw, podana jest ich lista P. 
# Pełnego baku wystarczy na przejechanie odległości d.  Wjeżdżając na stację samochód zawsze 
# jest tankowany do pełna. Proszę zaimplementować funkcję jak_dojade(G,P,d,a,b) która szuka 
# najkrótszej możliwej trasy od wierzchołka a do wierzchołka b, jeśli taka trasa istnieje, 
# i zwraca listę kolejnych odwiedzanych na trasie wierzchołków (zakładamy, że w a też jest 
# stacja paliw; Samochód może przejechać najwyżej odległość d bez tankowania). 
# Zaproponowana funkcja powinna być możliwie najszybsza. Uzasadnij jej poprawność i oszacuj 
# złożoność obliczeniową.

# Przykład: Dla tablic:
# G = [[-1,6,-1,5,2],
#     [-1,-1,1,2,-1],
#     [-1,-1,-1,-1,-1],
#     [-1,-1,4,-1,-1],
#     [-1,-1,8,-1,-1]]
# P = [0,1,3]
# funkcja jak_dojade(G,P,5,0,2) powinna zwrócić [0,3,2]. Dla tych samych tablic 
# funkcja jak_dojade(G,P,6,0,2) powinna zwrócić [0,1,2], natomiast
# jak_dojade(G,P,3,0,2) powinna zwrócić None.


#rozw: 
# zawsze gdy wjezdzamy do wierzcholka znajdujacego sie P to tankujemy bo bedzie nam sie zawsze opłacać
# bedziemy do kolejki priorytetowej umieszczac informacje o aktualnym stanie baku
# bedziemy na tym bazowac w algorytmie i zaimplementowalem to ponizej:

#inne rozwiazanie:
# kazdy wierzcholek mozemy "rozmnozyc" tak aby zawieral dodatkowo ilosc paliwa np A0, A1, B1:
# A - wierzcholek w ktorym jestesmy
# 1 - paliwo ktore aktualnie mamy
# dodatkowo A1 -> Ad, B3 -> Bd, C2 -> Cd itd. (jest polaczenie z maksimem) ale tylko wtw gdy A e P, B e P, C e P itd.

from queue import PriorityQueue

def traverse(parent,t):
    ans = []
    while t != -1:
        ans.append(t)
        t = parent[t]
    return ans
    

def jak_dojade(G,P,d,a,b): #d - odleglosc jaka jestesmy w stanie przejechać!
    visited = [False for i in range(len(G))]
    parent = [-1 for i in range(len(G))]
    distance = [float("inf") for i in range(len(G))]
    distance[a] = 0
    if a not in P: P.append(a) #aby warunek dzialal

    q = PriorityQueue()
    q.put((0,[a,d])) #(dystans,(wierzcholek,ilosc_paliwa - czyli dystans jaki mozemy pokonac))
    while not q.empty():
        cost,tup = q.get()
        u,paliwo = tup
        if visited[u]: continue
        visited[u] = True
        if u in P: paliwo = d        
        for v in range(len(G[u])):
            if visited[v] or G[u][v] == -1 or paliwo - G[u][v]< 0: continue
            if distance[u] + G[u][v] < distance[v]:
                distance[v] = distance[u] + G[u][v]
                parent[v]  = u
                #if v == b: return traverse(parent,v) - tutaj tego nie mozemy zrobic, bo gdy pierwszy raz v -- b to nie musi oznaczac najlepszej trasy!
                q.put((distance[v],[v,paliwo-G[u][v]])) #paliwo zmniejszone o dystans 
    ans = traverse(parent,b)
    ans.reverse()
    return ans if a in ans else None

G = [[-1,6,-1,5,2],
     [-1,-1,1,2,-1],
     [-1,-1,-1,-1,-1],
    [-1,-1,4,-1,-1],
     [-1,-1,8,-1,-1]]
P = [0,1,3]

# funkcja jak_dojade(G,P,5,0,2) powinna zwrócić [0,3,2]. Dla tych samych tablic 
# funkcja jak_dojade(G,P,6,0,2) powinna zwrócić [0,1,2], natomiast
# jak_dojade(G,P,3,0,2) powinna zwrócić None.

print(jak_dojade(G,P,5,0,2))
print(jak_dojade(G,P,6,0,2))
print(jak_dojade(G,P,3,0,2))