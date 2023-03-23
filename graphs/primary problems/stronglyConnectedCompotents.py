# Python implementation of Kosaraju's algorithm to print all SCCs
# Following is detailed Kosaraju’s algorithm.
# 1) Create an empty stack ‘S’ and do DFS traversal of a graph. 
# In DFS traversal, after calling recursive DFS for adjacent 
# vertices of a vertex, push the vertex to stack. 
# In the above graph, if we start DFS from vertex 0,
#  we get vertices in stack as 1, 2, 4, 3, 0.
# 2) Reverse directions of all arcs to obtain the transpose graph.
# 3) One by one pop a vertex from S while S is not empty. 
# Let the popped vertex be ‘v’. Take v as source and do DFS 
# (call DFSUtil(v)). The DFS starting from v prints 
# strongly connected component of v. 
# In the above example, we process vertices in order 0, 3, 4, 2, 1 
# (One by one popped from stack).

# Kosaraju's algorithm to find strongly connected components in Python


from collections import defaultdict

class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i) # na odwrot niz w graph
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()


## better:

def StronglyConnectedComponents(G):
    maks = 0
    for x,y in G:
        maks = max(maks,x,y)
    #zamiana z postaci krawedziowej na listy sąsiedztwa grafu:
    Graph = [[] for i in range(maks+1)]
    verified = [False for i in range(maks+1)] #dane wierzcholki muszą byc w tym grafie! nie ma zmiluj sie!
    for x,y in G:
        Graph[x].append(y)
        verified[x] = True
        verified[y] = True
    visited = [False for i in range(len(Graph))]
    
    stack = []
    counter = 0
    
    def topological_sort(u,Graph):
        visited[u] = True
        for v in Graph[u]:
            if not visited[v]:
                topological_sort(v,Graph)
        stack.append(u)

    def transpose(G):
        inverted_Graph = [[] for i in range(maks+1)]
        for i in range(len(G)):
            if verified[i] == False: continue
            for elem in G[i]:
                inverted_Graph[elem].append(i)
        return inverted_Graph
    
    #damy na koniec tą wersję dfsa
    def dfs(u,Graph): 
        visited[u] = True
        print(u,end=" ")
        for v in Graph[u]:
            if not visited[v]:
                dfs(v,Graph)

    for i in range(len(G)):
        if verified[i] == False: continue
        if not visited[i]:
            topological_sort(i,Graph)
    
    inverted_Graph = transpose(Graph)
    # print(Graph)
    # print(inverted_Graph)
    counter = 0
    # print(stack)
    visited = [False for i in range(len(Graph))]
    while stack:
        u = stack.pop()
        if not visited[u]:
            dfs(u,inverted_Graph) # wybrany wierzcholek ze stosu bedzie rootem grafu przemienionego!
            print("")
            counter +=1
    return counter


G = [[1,2],[3,4],[5,6],[7,7],[6,5],[10,11],[2,3],[4,1],[5,11]]
print(StronglyConnectedComponents(G))
#zwroci ich ilosc!