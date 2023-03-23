# Python3 program to print Eulerian circuit in given
# directed graph using Hierholzer algorithm
def printCircuit(adj):
	# adj represents the adjacency list of
	# the directed graph
	if len(adj) == 0:
		return # empty graph
	# Maintain a stack to keep vertices
	# We can start from any vertex, here we start with 0
	curr_path = [0]
	# list to store final circuit
	circuit = []
	while curr_path:
		curr_v = curr_path[-1]	
		# If there's remaining edge in adjacency list
		# of the current vertex
		if adj[curr_v]:
			# Find and remove the next vertex that is
			# adjacent to the current vertex
			next_v = adj[curr_v].pop()
			# Push the new vertex to the stack
			curr_path.append(next_v)
		# back-track to find remaining circuit
		else:
			# Remove the current vertex and
			# put it in the circuit
			circuit.append(curr_path.pop())
	# we've got the circuit, now print it in reverse
	for i in range(len(circuit) - 1, -1, -1):
		print(circuit[i], end = "")
		if i:
			print(" -> ", end = "")

# Driver Code
if __name__ == "__main__":

	# Input Graph 1
	adj1 = [[] for _ in range(3)]

	# Build the edges
	adj1[0].append(1)
	adj1[1].append(2)
	adj1[2].append(0)
	printCircuit(adj1)
	print()

	# Input Graph 2
	adj2 = [[] for _ in range(7)]

	adj2[0].append(1)
	adj2[0].append(6)
	adj2[1].append(2)
	adj2[2].append(0)
	adj2[2].append(3)
	adj2[3].append(4)
	adj2[4].append(2)
	adj2[4].append(5)
	adj2[5].append(0)
	adj2[6].append(4)
	printCircuit(adj2)
	print()

  
# This code is contributed by
# sanjeev2552


def printEulersCircuit(G): # Graf ten jest listą sąsiedztwa i jest nieskierowany
	#zrobmy postac inną naszego grafu(niech krawedzie wierzcholkow bedą polaczone z krawedziami w slowniku zamiast liscie)
    eulers_path = []
    def dfs(u):
        tmp = G[u].copy() #zawsze kopiujemy liste z sasiednimi wierzcholkami wierzcholka u
        for v in tmp: 
            if len(G[u]) == 0: break #robimy breaka gdy nie ma juz wierzcholkow sasiednich w u
            G[u].pop(G[u].index(v)) #albo poprostu .pop(0)
            G[v].pop(G[v].index(u)) 
            dfs(v)
        eulers_path.append(u)
        #path.pop()        
    dfs(0)
    print(eulers_path)
G = [[1,2],[0,2,3,5],[0,1,3,5],[1,2,4,5],[3,5],[2,3,4,1]]
printEulersCircuit(G)

#dla grafu nieskierowanego:
def betterEulersCircuit(G):
	graph = [{} for i in range(len(G))]
	for u in range(len(G)):
		for v in G[u]:
			graph[v][u] = 1
			graph[u][v] = 1 #istnieje krawedz
	eulers_path = []

	def dfs(u):
		tmp = G[u].copy()
		for v in tmp.keys():
			if not len(G[u]): break
			G[u].pop(v)
			G[v].pop(u)
			dfs(v)
		eulers_path.append(u)
	dfs(0)
	return eulers_path

G = [[1,2],[0,2,3,5],[0,1,3,5],[1,2,4,5],[3,5],[2,3,4,1]]
printEulersCircuit(G)


#---------------------------- VALID
#these above program were doing circuit and what if we want eulerian path not circuit?
#dla grafu skierowanego
def eulerianCircuit(G,v):
    curr_path = [v]
    circuit = []
    while curr_path:
        curr_v = curr_path[-1]
        if G[curr_v]:
            curr_path.append(G[curr_v].pop())
        else:
            circuit.append(curr_path.pop())
    return circuit


def euler_path(edges):
    maksim = 0
    for x,y in edges:
        maksim = max(maksim,x,y)
    G = [[] for i in range(maksim+1)]
    vertices = {}
    inputed = {} # vertice : countOfEdgesToThisVertice
    outputed = {} # vertice: countOfEdgesFromThisVertice
    for x,y in edges:
        G[x].append(y)
        outputed[x] = outputed.get(x,0) + 1
        inputed[y] = inputed.get(y,0) + 1
        vertices[x] = True
        vertices[y] = True
    
    for u in vertices.keys():
        if outputed.get(u,0) > inputed.get(u,0): #szukamy takiego wierzcholka, do ktorego prowadzi mniej krawedzi niz z niego wyplywa
            firstVertice = u       
    circuit = eulerianCircuit(G,firstVertice)  
    circuit = list(reversed(circuit))
    return circuit