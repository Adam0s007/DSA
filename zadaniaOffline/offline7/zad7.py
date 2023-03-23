from zad7testy import runtests
#Adam Biśta

#Algorytm opiera się na zasadzie odnajdywania ścieżki Hamiltona, jednak ze zwracaniem uwagi na bramy z których wyjeżdżamy
# z poszczególnych wierzchołków.
# za kazdym razem musimy miec dostęp do poprzedniego wierzcholka, aby wskazać przez którą bramę wjechaliśmy (prev)
#  Pierwszy wierzchołek musi mieć zapisaną bramę tzw. primaryGate z której wyjeżdża, po to, aby
# z ostatniego wierzcholka na naszej sciezce wjechać przez drugą bramę do wierzcholka startowego. Bedziemy szukać tej możliwości, 
# startując z każdego wierzchołka. Jesli nie znajdziemy takiej ścieżki to zwracamy None.
# time Complexity: O(v!) v - ilosc wierzcholkow
 
def SciezkaHamiltona(G, u, visited, proper_path,prev,ancestor,primaryGate):
    if len(proper_path) == len(G):
        gate = 0
        if prev in G[u][0]: gate = 1 #brama z ktorego mozemy wyjechac do ostatniego wierzcholka
        if ancestor in G[u][gate] and u in G[ancestor][not primaryGate]: #do poczatkowego weirzcholka trzeba wjechac drugą bramą!
        #- jesli dojedziemy do poczatkowego wierzcholka "ancestor" z odpowiedniej bramy z koncowego wierzcholka
        # ORAZ
        # w poczatkowym wierzcholku, z bramy z KTOREJ NIE WYRUSZYLISMY (primaryGate) znajduje sie ostatni wierzcholek
        # to zwroc sciezke i prawde bo istnieje ta sciezka!
            return proper_path,True
        return proper_path,False
    if prev == -1: #jestesmy w pierwszym wierzcholku, sprawdzamy wszystkie jego drogi bez wzgledu na brame!
        Nodes = [] #zapiszemy wszystkie bezposrednie wierzcholki do ktorych mozemy dojsc, z wierzcholka startowego
        counter = 0 #bedzie nam mowil, do ilu miast dojdziemy przez brame nr. 0 (ją zapiszemy w primaryGate)
        for v in G[u][0]:
            Nodes.append(v)
            counter +=1
        for v in G[u][1]:
            Nodes.append(v)
        iter = 0 #iter oraz counter nam wskazują z której bramy wyruszamy początkowego wierzchołka, zostaje to zapisane w zmiennej "primaryGate"
        for v in Nodes:
            primaryGate = 1
            if iter < counter: primaryGate  = 0
            if not visited[v]:
                visited[v] = True
                proper_path.append(v)
            tmp = prev
            prev = u
            ans = SciezkaHamiltona(G,v,visited,proper_path,prev,ancestor,primaryGate)
            if ans[1]: return proper_path,True
            #jesli ans[1] == False to musimy cofnąć wierzcholek i skorzystac z innej sciezki
            prev = tmp
            visited[v] = False
            proper_path.pop()
            iter +=1
        return proper_path,False
    else:
        gate = 0
        if prev in G[u][0]: gate = 1 

        for v in G[u][gate]: #bedziemy szukać miast w bramie innej niz ta, przez którą dotarlismy do miasta
            if not visited[v]:
                visited[v] = True
                proper_path.append(v)
                tmp = prev
                prev = u
                ans = SciezkaHamiltona(G, v, visited, proper_path,prev,ancestor,primaryGate)
                if ans[1]: return proper_path,True
                #jesli ans[1] == False to musimy cofnąć wierzcholek i skorzystac z innej sciezki
                visited[v] = False
                proper_path.pop()
                prev = tmp
        return proper_path,False
 
def droga( G ):
    for s in range(len(G)):
        proper_path = [s]
        prev = -1 #bedzie sygnalizowal z ktorej strony weszlismy do nowego miasta, wtedy musimy wybrac nowe miasto z drugiej strony
        #poczatkowo prev = -1 bo nie mamy poprzedniego zadnego wierzcholka
        visited = [False for i in range(len(G))]
        visited[s] = True
        primaryGate = -1 #mowi nam, z ktorej bramy wyjezdzamy w sowym wierzcholku!
        ans = SciezkaHamiltona(G, s, visited, proper_path,prev,s,primaryGate)
        if ans[1]: return ans[0]
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )