from egzP9btesty import runtests

def eulerianCircuit(G):
    curr_path = [0]
    circuit = []
    while curr_path:
        curr_v = curr_path[-1]
        if G[curr_v]:
            next_v = G[curr_v].pop()
            curr_path.append(next_v)
        else:
            circuit.append(curr_path.pop())
    return circuit



def dyrektor( G, R ):
	#Tutaj proszę wpisać własną implementację
	overhauled = {} # droga: ich_ilosc
	for u in range(len(R)):
		if len(R[u]):
			for v in R[u]:
				overhauled[(u,v)] = overhauled.get((u,v),0) + 1 #droga z u do v jest remontowana, moze byc wiele drog z u do v wiec je zliczamy

	graph = [[] for i in range(len(G))]
	for u in range(len(G)):
		for v in G[u]:
			if (u,v) not in overhauled: 
				graph[u].append(v) 
			else:
				overhauled[(u,v)] = overhauled.get((u,v)) - 1
				if overhauled.get((u,v)) == 0:
					overhauled.pop((u,v))

	
	path = list(reversed(eulerianCircuit(graph)))
	return path
	
runtests(dyrektor, all_tests=True)
