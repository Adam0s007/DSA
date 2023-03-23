# Python program to find bridges in a given undirected graph
#Complexity : O(V+E)

from collections import defaultdict

#This class represents an undirected graph using adjacency list representation
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
		self.Time = 0

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	'''A recursive function that finds and prints bridges
	using DFS traversal
	u --> The vertex to be visited next
	visited[] --> keeps track of visited vertices
	d[] --> Stores discovery times of visited vertices
	parent[] --> Stores parent vertices in DFS tree'''
	def bridgeUtil(self,u, visited, parent, low, d):
		visited[u]= True
		d[u] = self.Time #zawsze zapamietuj czas odwiedzenia...
		low[u] = self.Time #... i zapisuj wtedy to samo dla d[u] i low[u] (poczatkowo)
		self.Time += 1 #nastepnie zwieksz czas!
		for v in self.graph[u]:
			if visited[v] == False :
				parent[v] = u
				self.bridgeUtil(v, visited, parent, low, d)
				#po przetworzeniu wierzcholkow, tutaj aktualizujemy wartosc low patrząc na dziecko wierzchołka u
				low[u] = min(low[u], low[v])
			elif v != parent[u]: #sprawdzamy krawedz wsteczną (ona oznacza cykl, wiemy ze visited[v] == True)
				low[u] = min(low[u], d[v]) #krawedz wsteczna {u,v} - nie rodzic v i byla odwiedzona!
		if low[u] == d[u] and parent[u] != -1: #po przetworzeniu dzieci wierzcholka u, jesli jego low(u) okaze sie dalej byc taki sam jak d(u) to oznacza ze jest mostem! (uw. dla pierwszego wierzcholka (startowego) nie ma parenta, wiec nie bedzie tam mostu)
			print ("%d %d" %(u,parent[u]))


	# DFS based function to find all bridges. It uses recursive
	# function bridgeUtil()
	def bridge(self):

		# Mark all the vertices as not visited and Initialize parent and visited,
		# and ap(articulation point) arrays
		visited = [False] * (self.V)
		d = [float("Inf")] * (self.V)
		low = [float("Inf")] * (self.V)
		parent = [-1] * (self.V)

		# Call the recursive helper function to find bridges
		# in DFS tree rooted with vertex 'i'
		for i in range(self.V):
			if visited[i] == False:
				self.bridgeUtil(i, visited, parent, low, d)
		

# Create a graph given in the above diagram
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)


print ("Bridges in first graph ")
g1.bridge()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("\nBridges in second graph ")
g2.bridge()


g3 = Graph (7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print ("\nBridges in third graph ")
g3.bridge()


#This code is contributed by Neelam Yadav


G = [[1,3,9,11],[0,2,4],[1],[0,4,5],[3,1],[6,21,3],[5,7],[8,6],[7],[0,18],[0,13],[0,12],[11,14,13],[10,12],[12,15,17],[14,16],[17,15],[14,16],[9,19],[18,20],[19],[5]]

def find_bridges(G,s):
    d = [float("inf") for i in range(len(G))]
    low = [float("inf") for j in range(len(G))]
    parent = [-1 for j in range(len(G))]
    visited = [False for i in range(len(G))]
    counter = [0]
    bridges = []
    def mosty(G,s):
        low[s] = counter[0]
        d[s] = counter[0]
        counter[0] +=1
        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                parent[v] = s
                mosty(G,v)
                low[s] = min(low[s],low[v])
            elif parent[s] != v:
                low[s] = min(low[s],d[v])
        if low[s] == d[s] and parent[s] != -1:
            bridges.append((parent[s],s))
    mosty(G,s)
	

G = [[1,3,9,11],[0,2,4],[1],[0,4,5],[3,1],[6,21,3],[5,7],[8,6],[7],[0,18],[0,13],[0,12],[11,14,13],[10,12],[12,15,17],[14,16],[17,15],[14,16],[9,19],[18,20],[19],[5]]
find_bridges(G,0)