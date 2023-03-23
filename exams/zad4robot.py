# Robot porusza sie po dwuwymiarowym labiryncie i ma dotrzeć 
# z pozycji A = (xa,ya) na pozycję B = (xb,yb). Robot może wykonać 
# następujące ruchy:
# 1. ruch do przodu na kolejne pole.
# 2. obrót o 90 stopni zgodnie  z ruchem wskazówek zegara.
# 3. obrót o 90 stopni przeciwnie do ruchów wskazówek zegara.

# Obrót zajmuje robotowi 45 sekund. W trakcie ruchu do przodu robot 
# się rozpędza i pokonanie pierwszego pola zzajmuje mu 60 sekund. pokonanie drugiego 40 sekund.
# A kolejnych po 30 sekund na pole. Wykonanie obrotu zatrzymuje robota i następujące 
# po nim ruchy do przodu ponownie go rozpędzają. Proszę zaimplementować funkcję:
# def robot(L,A,B):...

# która oblicza ile minimalnie sekund robot potrzebuje na dotarcie z punktu A do punktu B 
# (lub zwraca None jeśli jest to nie możliwe).
# Funkcje powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową 
# użytego algorytmu.

# Labirynt reprezentowany jest przez tablicę w wierszy, z których każdy jest napisem składającym się z k kolumn.
# Pusty znak oznacza pole po którym robot może się poruszać, a znak 'X' oznacza ścianę labiryntu.
# Labirynt zawsze otoczony jest ścianami i nie da się opuścić planszy.

# Pozycja robota: Początkowo robot znajduje się na pozycji A = (xa,ya) i obrócony w prawo 
# (tj. znajduje sięw wierszu ya i kolumnie xa, skierowany w stronę rosnących numerow kolumn)


# rozwiazanie:
#dijkstra algo:
    #musimy dodac 4 wartosci flagi:
    #0 -> idzie do gory
    #1 -> idzie w lewo
    #2 -> idzie w dol
    #3 -> idzie w prawo

#in_motion:
    # 0 - poczatkowa wartosc, oznacza ze dopiero wystartuje przed siebie 
    # 45 - ozn ze obrocil sie dopiero co
    # 60 - oznacza ze przejechal przez pole w 60 sek
    # 40 - ozn ze przejechal przez pole w 40 sek
    # 30 - ozn ze przejechal przez pole w 30 sek 
    #co przesylamy do kolejki priorytetowej: (distance[Point[1]][Point[0]],[Point,in_motion,wektor,kierunek])
#moves = (...) 0 - bez obrotu, 90 - obrot zgodnie ze wsk zegara, -90 - obrot przeciwnie do wsk zeg.
#jesli move == 0 to wector i direct pozostaną te same
#q.put((distance[1][A[1]][A[0]],[A,in_motion,(1,0),1]))  = wektor dajemy taki bo w taka strone jest skierowany
from zad4testy import runtests
from queue import PriorityQueue

def oblicz_kierunek(wektor,obrot,kierunek):
    if obrot == 0: return wektor,kierunek
    elif obrot == 90:
        if wektor[0] == 1 and wektor[1] == 0: return [0,1],2
        elif wektor[0] == 0 and wektor[1] == 1: return [-1,0],1
        elif wektor[0] == -1 and wektor[1] == 0: return [0,-1],0
        else: return [1,0],3
    elif obrot == -90:
        if wektor[0] == 1 and wektor[1] == 0: return [0,-1],0
        elif wektor[0] == 0 and wektor[1] == -1: return [-1,0],1
        elif wektor[0] == -1 and wektor[1] == 0: return [0,1],2
        else: return [1,0],3

def oblicz_predkosc(motion):
    if motion == 60: return 40
    elif motion == 40 or motion == 30: return 30
    elif motion == 0 or motion == 45: return 60
    

def robot(L,A,B):
    w  = len(L)
    k = len(L[0])
    G = [[' ' for i in range(len(L[0]))] for j in range(len(L))]
    
    distance = [[[float("inf") for i in range(len(G[0]))] for j in range(len(G))] for k in range(4)]#mamy 4 kierunki!
    visited = [[[False for i in range(len(G[0]))] for j in range(len(G))] for k in range(4)]
    q = PriorityQueue()
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] != ' ':
                G[i][j] = L[i][j]

    

    distance[3][A[1]][A[0]] = 0
    in_motion = 0
    
    moves = (0,90,-90) 
    q.put((distance[3][A[1]][A[0]],[A,in_motion,(1,0),3])) 
    while not q.empty(): #newPosition to pozycja na którą wejdziemy!
        time, tup = q.get()
        P = tup[0]
        in_motion = tup[1]
        wector = tup[2]
        direct = tup[3]
        if visited[direct][P[1]][P[0]]: continue 
        visited[direct][P[1]][P[0]] = True  
        for move in moves:
            
            if move == 0:  # jesli jestesmy w trybie ruszania w danym kierunku: 
                newPosition = (P[0]+wector[0],P[1]+wector[1])
                if  newPosition[0] < 0 or newPosition[0] >= len(G[0]) or\
                newPosition[1] < 0 or newPosition[1] >= len(G) or\
                    G[newPosition[1]][newPosition[0]] == 'X': continue
                newMotion = oblicz_predkosc(in_motion)  
                if time + newMotion < distance[direct][newPosition[1]][newPosition[0]]:      
                    distance[direct][newPosition[1]][newPosition[0]] = time + newMotion
                    q.put((distance[direct][newPosition[1]][newPosition[0]],[newPosition,newMotion,wector,direct]))
            else: 
                newWector,newDirect = oblicz_kierunek(wector,move,direct)
                if distance[newDirect][P[1]][P[0]] > time + 45:
                    distance[newDirect][P[1]][P[0]] = time + 45         
                    q.put((distance[newDirect][P[1]][P[0]],[P,45,newWector,newDirect]))
    minim = float("inf")
    
    for i in range(4):
        if minim > distance[i][B[1]][B[0]]: 
            minim = distance[i][B[1]][B[0]]

    return minim if minim != float("inf") else None

    
# T = ["XXXXXXXXXX",
#      "X X      X",
#      "X XXXXXX X",
#      "X        X",
#      "XXXXXXXXXX"
#     ]
# A = (1,1)
# B = (8,3)
# print(robot(T,A,B))



runtests( robot )
