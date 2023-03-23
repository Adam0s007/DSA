# Alicja chce zorganizować przyjęcie i zastanawia się,
# kogo zaprosić spośród n znajomych. Stworzyła już listę
# par osób które się znają. Chce wybrać możliwie jak najwięcej osób,
# tak aby spełnione były dwa warunki: na przyjęciu każda osoba powinna znać 
# przynajmniej 5 osób oraz co najmniej 5 osób nie znać.

# Zaproponuj algorytm, który przyjmuje na wejściu listę 
# n osób oraz listę par osób które się znają a na wyjściu daje 
# możliwie nadłuższą listę gości


#Rozwiazanie:
# zrobmy graf w ktorym osoba to wierzcholek a znajomosc to krawedz i to jest nieskierowane
# czyli graf reprezentuje nam ilosc osob na imprezie
# z grafu usuwamy osoby nie spelniajace warunki w zadaniu
# usuwamy krawedzie do wierzcholka i na koncu nasz sam wierzcholek u sasiadkow i u nas
#zmniejszamy liczbe wszystkich gosci o i
#nastepnie:
# wydaje mi sie ze najlepiej bfsem isc do kolejnych osob u ktorych usunelismy juz krawedzie do poprzedniego
# wierzcholka (wiec sie nie cofniemy i nie bedzie petli), ponieważ dfs moglby zrobic nieco zamieszania
# moze dzialalby ale tego nie widzę wiec zrobilem bfs i btw nie wiem czy moj kod dziala bo nie chce mi sie
#wymyslac przypadkow juz, ale koncepcyjnie jest okej.
from collections import deque
def przyjecie(osoby,znajomosci):
    graph = {elem:[] for elem in osoby}
    #liczba osob ktorych dana osoba nie zna: ilosc osob na przyjeciu -1 - ilosc swoich znajomosci
    for osoba1,osoba2 in znajomosci:
        graph[osoba1].append(osoba2)
        graph[osoba2].append(osoba1)
    n = len(osoby)
    #musimy usunac osoby z tego grafu, ktore znają mniej niz 5 osob oraz więcej niz n - 1 - len(graph[i]) (sam siebie czlowiek zna ale nie mozna tego traktowac jak dodatkowa znajomosc)
    print(graph)
    arr = [n] #lista wszystkich osob znanych, bedzie aktualizowana wraz z usuwaniem nowych ludzi
    #musimy robic bfsa bo najpierw musimy usunac wszystkie krawedzie z naszego wierzch i z wierzch naszych sasiadow a potem dopiero przejsc do nich
    def bfs(u):
        queue = deque()
        queue.append(u)
        
        while queue:
            u = queue.popleft()
            if u not in graph: continue
            visited[u] = True #jesli warunek nizej jest okej, to poprostu nie idziemy juz nigdzie
            if len(graph[u]) < 5 or(arr[0] - 1 - len(graph[u]) < 5):
                arr[0] -=1
                tmp = graph[u].copy()
                for v in tmp:
                    graph[v].pop(graph[v].index(u))
                    graph[u].pop(graph[u].index(v))
                    queue.append(v)
                graph.pop(u) # na koncu usuwamy wierzcholek
                verified[u] = False

    visited = {}
    lista_os = list(graph.keys())
    #potrzebujemy liste_os aby zawierala po pierwsze wierzcholki a po drugie ilosc znajomosci z wierzcholkami
    #uwaga! prawdopodobnie tego nie trzeba sortować, ci co mają zostać wywaleni i tak zostaną bo zmieniamy liczę wszystkich gosci
    lis = []
    for elem in lista_os:
        lis.append((elem,len(graph[elem])))
    lis.sort(key=lambda x: x[1],reverse=True) #malejaco! niech najpierw pozbedzie sie osob, ktore mają za duzo znajomych

    verified = {elem:True for elem in osoby}
    for u,l in lis:
        if verified[u] == True and u not in visited:
            bfs(u)

    return arr[0] 







osoby = [0,1,2,3,4,5,6,8,10,11]
znajomosci = [(5,4),(5,10),(5,0),(2,0),(3,2),(8,3),(8,2),(8,11),(0,11),(11,2),(6,1),
(6,11),(6,8),(6,3),(6,10),(1,0),(1,11),(0,4),(2,4),(3,10),(3,4),(2,6),(4,8),(4,10)]

print(przyjecie(osoby,znajomosci))