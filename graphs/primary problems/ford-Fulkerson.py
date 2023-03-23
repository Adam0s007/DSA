# Python program for implementation
# of Ford Fulkerson algorithm
from collections import defaultdict
from queue import SimpleQueue
# This class represents a directed graph
# using adjacency matrix representation
class Graph:
 
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self. ROW = len(graph)
        # self.COL = len(gr[0])
 
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
 
    def BFS(self, s, t, parent):
        # Mark all the vertices as not visited
        visited = [False]*(self.ROW)
        # Create a queue for BFS
        queue = SimpleQueue()
        # Mark the source node as visited and enqueue it
        queue.put(s)
        visited[s] = True
         # Standard BFS Loop
        while not queue.empty():
            # Dequeue a vertex from queue and print it
            u = queue.get()
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                      # If we find a connection to the sink node,
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.put(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        # We didn't reach sink in BFS starting
        # from source, so return false
        return False
    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
        max_flow = 0 # There is no flow initially
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
            # Add path flow to overall flow
            max_flow +=  path_flow
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow #residual edge!!! czyli taka odwrotna! pozwala na cofanie sie!
                v = parent[v]
        return max_flow
 
  
# Create a graph given in the above diagram
 
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
 
g = Graph(graph)
 
source = 0; sink = 5
  
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
 
# This code is contributed by Neelam Yadav

# The above implementation of Ford Fulkerson Algorithm is called Edmonds-Karp Algorithm. 
# The idea of Edmonds-Karp is to use BFS in Ford Fulkerson implementation as 
# BFS always picks a path with minimum number of edges. When BFS is used,
#  the worst case time complexity can be reduced to O(VE2). 
#  The above implementation uses adjacency matrix representation though where BFS takes O(V2) time, 
# the time complexity of the above implementation is O(EV3)

from queue import SimpleQueue
def BFS(graph, s, t, parent):
    visited = [False]*(len(graph))
    queue = SimpleQueue()
    queue.put(s)
    visited[s] = True
    while not queue.empty():
        u = queue.get()
        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                queue.put(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == t:
                    return True
    return False

def edmund_karp(graph,source, sink):
    parent = [-1]*(len(graph))
    max_flow = 0
    while BFS(graph,source, sink, parent) :
        path_flow = float("Inf")
        v = sink
        #znajdowanie najmniejszego przeplywu na danej sciezce
        while(v !=  source):
            path_flow = min (path_flow, graph[parent[v]][v])
            v = parent[v]
        max_flow +=  path_flow
        v = sink
        #usuwanie / dodawanie najmniejszego przeplywu miedzy krawedziami na danej sciezce
        while(v !=  source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow #residual edge!!! czyli taka odwrotna! pozwala na cofanie sie!
            v = parent[v]
    return max_flow

#Okej mamy na macierzowej reprezentacji edmonda karpa, ale przydaloby sie tez dla listy sąsiedztwa
#musi byc to graf skierowany, tak czy siak, powyzej rowniez
def bfs(graph, s, t, parent):
    visited = [False]*(len(graph))
    queue = SimpleQueue()
    queue.put(s)
    visited[s] = True
    while not queue.empty():
        u = queue.get()
        for v,w in graph[u].items(): # [{v1:w1, v2:w2, v3:w3,...},{....}]
            if not visited[v] and w > 0:
                queue.put(v)
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True
    return False

def edmund_karp_adjacency(graph,source, sink): #graph -> lista sąsiedztwa [v,w]
    parent = [-1]*(len(graph))
    max_flow = 0

    G = [{} for i in range(len(graph))]  #[[]..] => [{}...]
    for i in range(len(graph)):
        for v,w in graph[i]: 
            G[i][v] = w
            G[v][i] = 0 if i not in G[v] else G[v][i] #moze byc sytuacja u -- w1 --> v oraz u <-- w2 -- v jednoczesnie!
    
    while bfs(G,source, sink, parent) :
        path_flow = float("Inf")
        v = sink
        #znajdowanie najmniejszego przeplywu na najkrotszej danej sciezce
        while(v != source):
            path_flow = min(path_flow, G[parent[v]][v])
            v = parent[v]
        max_flow +=  path_flow
        v = sink
        #usuwanie / dodawanie najmniejszego przeplywu miedzy krawedziami na danej sciezce
        while(v !=  source):
            u = parent[v]
            G[u][v] = G[u].get(v) - path_flow #G = [{},{},{},..]
            G[v][u] = G[v].get(u) + path_flow #residual edge!!! czyli taka odwrotna! pozwala na cofanie sie!    
            v = parent[v]
    return max_flow
    
''' [[(u1,w1),(u2,w2),(u3,w3)...],[(ui,wi),(uj,wj)...]...]  u - wierzcholek docelowy, w - waga krawedzi '''
graph = [[(1,2),(5,3)],[(2,2)],[(6,3)],[(1,2),(4,3),(2,3)],[(6,8),(7,3),(8,5)],[(3,3)],
        [],[(6,4)],[(7,3)]]

print(edmund_karp_adjacency(graph,0,6))


#oznakowanie wszystkich krawedzi od u do v o wadze w : values[(u,v)] = w

def getEdges(graph): #graph to lista sąsiedztwa skierowana!
    values = {} #przechowywac bedziemy tu informacje o wartosciach miedzy krawedziami
    visited = [False for i in range(len(graph))]
    def dfs(u):
        visited[u] = True
        for v,w in graph[u]:
            if (u,v) not in values:
                values[(u,v)] = w
                values[(v,u)] = 0
            if not visited[v]:
                dfs(v)
    for i in range(len(graph)):
        if not visited[i]: dfs(i)
    return values