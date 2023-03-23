# from re import T


# Dany jest zbiór N zadań, gdzie niektóre zadania muszą być wykonane przed innymi zadaniami.
# Wzajemne kolejności zadań opisuje tablica dwuwymiarowa T[N][N]. Jeżeli T[a][b] = 1, to
# wykonanie zadania a musi poprzedzać wykonanie zadania b. W przypadku gdy T[a][b] = 2
# zadanie b musi być wykonane wcześniej, a gdy T[a][b] = 0 to kolejność zadań
# a i b jest obojętna. Proszę zaimplementować funkcję tasks(T), która dla danej tablicy T,
# zwraca tablicę z kolejnymi numerami zadań do wykonania.

# Przykład: Dla tablicy T = [[0,2,1,1],[1,0,1,1],[2,2,0,1],[2,2,2,0]] wynikiem jest tablica
# [1,0,2,3].


#rozwiazanie: tworzymy graf bedący listą sasiedztwa
# w nim jesli T[a][b] = 1 to a ---> b
# gdy T[a][b] = 2 to b --> a
# gdy T[a][b] = 0 to nie tworzymy zadnej krawedzi! wywolujac sortowanie topologiczne
# (czyli w skrocie mowiac dfs) to wtedy wywolamy go dla kazdego wierzcholka i tak czy siak
# te wierzcholki znajdą się w zadaniach ale w dowolnej kolejności (jeśli zostały związane
# kolejnością przez inne wierzchołki to tak czy siak sortowanie topologiczne odwali robote)

def tasks(T):
    G = [[] for i in range(len(T))]
    for i in range(len(T)):
        for j in range(i+1,len(T[0])):
            if T[i][j] == 1: G[i].append(j)
            elif T[i][j] == 2: G[j].append(i)
            #nie rozpatrujemy warunku dla T[i][j] == 0 - to oznacza poprostu brak krawedzi!
            # natomiast jak wiemy jak dziala sortowanie  topol (dfs) to wiemy ze wszystkie wierzcholki
            # zostaną rozpatrzone 
    print(G)
    stack = []
    visited = [False for i in range(len(T))]
    def topologicalSort(u):
        visited[u] = True
        for v in G[u]:
            if visited[v]: continue
            topologicalSort(v)
        stack.append(u)
        
    for i in range(len(T)):
        if not visited[i]:
            topologicalSort(i)
    return list(reversed(stack))



T = [[0,2,1,1],[1,0,1,1],[2,2,0,1],[2,2,2,0]]
print(tasks(T))