# Carol musi przewieźć pewne niebezpieczne substancje z laboratorium x do laboratorium y.
# Podczas gdy Max musi zrobić to  samo, ale w przeciwną stronę. Problem polega na tym, że
# jeśli substancje te znajdą się zbyt blisko siebie, to nastąpi reakcja w wyniku której
# absolutnie nic się nie stanie ( ale szefowie Carol i Max nie chcą do tego dopuścić, by nie okazało się,
# że ich praca nie jest nikomu potrzebna). Zaproponuj, uzasadnij i zaimplementuj algorytm
# planujący jednocześnie trasy Carol i Maxa tak, by odległość między nimi zawsze wynosiła 
# co najmniej d. Mapa połączeń dana jest jako graf nieskierowany, w którym każda krawędź 
# ma dodatnią wagę (x i y to wierzchołki w tym grafie). W jednostce czasu Carol i Max pokonują
# dokładnie jedną krawędź. Jeśli trzeba, dowolne z nich może się w danym kroku zatrzymać
# (wówczas pozostaje w tym samym wierzchołku). Carol i Max nie mogą równocześnie poruszać się
# tą samą krawędzią ( w przeciwnych kierunkach).
# Rozwiązanie należy zaimplementować w postaci funkcji: def keep_distance(M,x,y,d):...
# która przyjmuje numery wierzchołków x oraz y, minimalną odległość d i graf reprezentowany
# przez kwadratową, symetryczną macierz sąsiedztwa M. Wartość M[i][j] == M[j][i] to dlugosc
# krawędzi między wierzchołkami i oraz j, przy czym M[i][j] == 0 oznacza brak krawędzi między
# wierzchołkami. W macierzy nie ma wartości ujemnych. Funkcja powinna zwrócić listę krotek postaci:
# [(x,y),(u1,v1),(u2,v2),...,(uk,vk),(y,x)]
# reprezentującą ścieżki Carol i Max. W powyższej liście element (ui,vi) oznacza ze Carol 
# znajduje się w wierzchołku u1, zaś Max w wierzchołku vi. Można założyć, że rozwiązanie istnieje.


#rozwiazanie:
# Najpierw robimy graf dp zawierajace najkrotsze odleglosci miedzy wszystkimi wierzcholkami
# bfsem/dfsem przechodzimy przez nasz oryginalny graf, za kazdym razem bedziemy opertowac na krotce (u,v)
# jeden wierzcholek reprezentuje Carol a drugi Max.
# robimy trzy petne w tym jedna zagnieżdżona:
# zagniezdzona: staramy sie znalezc jednoczesne przemieszczenie carol i max
# dwie normalne: gdy carol stoi i max sie przemieszcza i gdy max stoi i carol idzie

# Gdy mamy jednoczesne przemieszczenie jakies to nie sprawdzamy warunku gdy jeden z nich stoi bo nie musi stać
# jeśli mogą się ruszyć jednoczesnie to ruszają się, jesli nie, to wtedy dopiero jeden z nich stoi 

from zad6testy import runtests 
from queue import SimpleQueue
def floyd_warshall(G):
    nV = len(G)
    dp = [[0 for i in range(len(G))]for j in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
           dp[i][j] = G[i][j] 
    # Adding vertices individually
    for k in range(nV): # nV - nr of vertices
        for i in range(nV):
            for j in range(nV):
                if (dp[i][j] == 0 and dp[i][k] > 0 and dp[k][j] >0 and i != j) or\
                    (dp[i][j] != 0 and  dp[i][k] > 0 and dp[k][j] >0 and dp[i][j] > dp[i][k] + dp[k][j] and i != j):
                    dp[i][j] = dp[i][k] + dp[k][j]
    return dp

def keep_distance(M,x,y,d):
    #najpierw tworzymy macierz najkrotszych odleglosci z wszystkich wierzcholkow
    dp = floyd_warshall(M)
    # for i in range(len(dp)):
    #     for j in range(len(dp[0])):
    #         print(dp[i][j],end=" ")
    #     print()
    parent = [[[-1,-1]for i in range(len(M))] for j in range(len(M))] # bedzie parent[carol][max]
    q = SimpleQueue()
    visited = [[False for i in range(len(M))] for i in range(len(M))] #bedzie visited[carol][max]
    
    q.put((x,y)) #Carol i Max
    visited[x][y] = True
    flag = 1
    while not q.empty() and flag: 
        carol,max = q.get()
        flag = 1
        if not((carol == y and max != x) or (max == x and carol != y)):
            for vCarol,w1 in enumerate(M[carol]):
                if w1 == 0: continue
                for vMax,w2 in enumerate(M[max]): # w tych podwojnych petlach szukamy sposobu na pokonanie przez obydwie dziewczyny jakiejs odleglosci
                    if dp[vCarol][vMax] < d or visited[vCarol][vMax] or \
                        (carol == vMax and vCarol == max) or w2 == 0: continue
                    if visited[vCarol][vMax]: continue 
                    #print("vCarol:",vCarol," vMax:",vMax)
                    visited[vCarol][vMax] = True
                    #flag = 2 #jesli nie zrobimy zadnego przejscia to flag pozostanie 1 i bedziemy musieli 
                    # skorzystac z pozostalych petli
                    parent[vCarol][vMax][0] = carol
                    parent[vCarol][vMax][1] = max
                    q.put((vCarol,vMax))
                    if vCarol == y and vMax == x: 
                        flag = 0
                        break
                if flag == 0: break
            if flag == 0: break
        #wariant dla jednej dziewczyny stojącej w miejsciu a drugiej idącej dalej
        #1) Carol stoi w miejscu a Max idzie: 
        if flag == 1: # nie wykonalismy zadnebo ruchu w jednoczesnym przejsciu carola i maksa -> ktos z nich musi stać!
            for vMax,w2 in enumerate(M[max]):
                if dp[carol][vMax] < d or visited[carol][vMax] or vMax == carol or w2==0: continue
                #print("vCarol:",carol," vMax:",vMax)
                visited[carol][vMax] = True
                parent[carol][vMax][0] = carol
                parent[carol][vMax][1] = max  
                q.put((carol,vMax))
                if carol == y and vMax == x: 
                        flag = 0
                        break
            if flag == 0: break
            #2) Max stoi w miejscu a Carol idzie:
            for vCarol,w1 in enumerate(M[carol]):
                if dp[vCarol][max] < d or visited[vCarol][max] or max == vCarol or w1 == 0: continue
                #print("vCarol:",vCarol," vMax:",max)
                visited[vCarol][max] = True
                parent[vCarol][max][0] = vCarol
                parent[vCarol][max][1] = max  
                q.put((vCarol,vMax))
                if vCarol == y and max == x: 
                        flag = 0
                        break
        if flag == 0: break
    ans = []
    while x != -1:
        #print(y,x)
        ans.append((y,x))
        y,x = parent[y][x]
    
    return list(reversed(ans))


# G = [[0,1,0,0,0,0],
#      [1,0,2,0,0,0],
#      [0,2,0,3,0,5],
#      [0,0,3,0,4,0],
#      [0,0,0,4,0,1],
#      [0,0,5,0,1,0]]

# print(keep_distance(G,0,5,1))
runtests( keep_distance )