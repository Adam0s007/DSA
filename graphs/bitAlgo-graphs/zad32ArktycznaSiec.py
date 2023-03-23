# W Arktyce osady są oddalone od siebie na ogromne odległości. Otrzymujemy je jako pary
# współrzędnych (x,y). 
# Niektóre z nich posiadają odbiorniki satelitarne - z takiej osady można bezpośrednio komunikować się
# z każdą inną osadą, która ma odbiornik satelitarny. 
# Chcemy teraz w każdej osadzie umiejscowić radioodbiorniki o tym samym ograniczonym zasięgu D (liczba calkowita). 
# Aby mozna bylo sie komunikowac ( posrednio lub bezposrednio) między każdą parą osad. Jakie jest minimalne D, ktore pozwoli 
# osiagnac ten cel?


#rozw:
# robimy graf, wierzcholki to miasta
#algorytm kruskala
# krawedzie pomiedzy mmiastami to odleglosci miedzy miastami w metryce euklidesowej zaokr. w gore
#szukamy MST lacząc już wszystkie wierzchołki, które już mają radioodbiorniki.
#szukamy MST aby polaczyc juz wszystkie wierzcholki. Wyciagnieta ostatnia krawedz bedzie o najwiekszej wadze.
# ta waga bedzie reprezentowala minimalny zasieg radioodbiornika.
import math

class Node:
    def __init__(self,val):
        self.parent= self 
        self.val = val 
        self.rank = 0

def make(x):
    return Node(x)

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent 

def union(x,y):
    x = find(x)
    y = find(y)
    if x.rank > y.rank: y.parent = x
    else: 
        x.parent = y
        if x.rank == y.rank: 
            y.rank +=1



def metric(x1,y1,x2,y2):
    return math.ceil(math.sqrt((x1-x2)**2 + (y1-y2)**2))




def network(Points):
    Edges = []
    for i in range(len(Points)):
        x1 = Points[i][0]
        y1 = Points[i][1]
        flag1 = Points[i][2]
        for j in range(i+1, len(Points)):
            x2 = Points[j][0]
            y2 = Points[j][1]
            flag2 = Points[j][2]
            boole = True if flag2 == flag1 == True else False
            Edges.append((i,j,metric(x1,y1,x2,y2),boole))
    Edges.sort(key=lambda x: x[2])
    #print(Edges)
    Nodes = [make(x) for x in range(len(Points))]
    maksim_w = 0
    ans = []
    for u,v,w,flag in Edges:
        if flag == True:
            if find(Nodes[u]) != find(Nodes[v]):
                union(Nodes[u],Nodes[v])
                #maksim_w = max(maksim_w,w) tu tego nie robimy! tam juz są odbiorniki a my musimy wiedziec, jaki dodac
                # odbiornik do miast w ktorych nie ma, aby dotarl do innych miast! 
                ans.append((u,v,w))
    
    for u,v,w,flag in Edges:
        if flag == False:
            if find(Nodes[u]) != find(Nodes[v]):
                union(Nodes[u],Nodes[v])
                maksim_w = max(maksim_w,w)
                ans.append((u,v,w))
    return maksim_w,ans
    


Points = [(1,1,False),(5,2,False),(4,6,True),(2,5,False),(2,9,True),(9,9,False),(11,4,True),(1,12,False),(6,13,True),(13,13,False)]

print(network(Points))