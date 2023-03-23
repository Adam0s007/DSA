class Node:
    def __init__(self,val,priority):
        self.val = val
        self.priority = priority

def sift_down(heap,i,position):
	l = 2*i + 1
	r = 2*i + 2
	min_id = i
	if l < len(heap) and heap[l].priority < heap[min_id].priority:
		min_id = l
	if r < len(heap) and heap[r].priority < heap[min_id].priority:
		min_id = r
	if min_id is not i:
		position[heap[i].val] = min_id
		position[heap[min_id].val] = i
		heap[i], heap[min_id] = heap[min_id], heap[i]
		sift_down(heap,min_id,position)

def get(heap,position):
	if len(heap) != 0:
		minim = heap[0]
		position[heap[0].val] = None #jesli danego wierzcholka nie ma w heapie to przypisz mu None
		heap[0] = heap[-1]
		position[heap[0].val] = 0

		heap.pop()
		sift_down(heap,0,position)
		return minim
	return None


def heapify(heap,position):
    for i in range((len(heap)-2)//2,-1,-1):
        sift_down(heap,i,position)


def insert(heap,val,priority,position): 
	elem = Node(val,priority)
	heap.append(elem)
	position[heap[-1].val] = len(heap)-1  #pozycja tej wartosci
	index = len(heap)-1
	idParent = (index-1)//2
	while index > 0 and heap[index].priority < heap[idParent].priority:
		position[heap[index].val] = idParent
		position[heap[idParent].val] = index

		heap[index],heap[idParent] = heap[idParent], heap[index]
		index = idParent
		idParent = (index-1)//2

def sift_up(heap,i,position): #for min-heap
	parent = (i-1)//2
	while i > 0 and heap[i].priority < heap[parent].priority:
		position[heap[i].val] = parent
		position[heap[parent].val] = i
		heap[i], heap[parent] = heap[parent], heap[i]
		i = parent
		parent = (i-1)//2


def decrease_key(heap,position,v,new_priority):
	#trzeba znac pozycje wierzcholka w kolejce!
	pos = position[v]
	heap[pos].priority = new_priority
	sift_up(heap,pos,position)




def PrimsAlgorithm(G):
	''' G postaci: [[[u1,w1],[u2,w2],[u3,w3]...],[...],[...]] 
	gdzie: u1,u2,u3 - dotarcie do wierzcholkow u1,u2,u3 przez wierzcholek G[i]
		   w1,w2,w3 - wagi krawedzi   '''
	position = [None for i in range(len(G))] #bedzie okreslala pozycję wierzcholka w heapie!
	# jesli wierzcholka nie ma w heapie to position[v] = None!
	parent = [-1 for i in range(len(G))]
	heap  = []
	#na poczatek zapelniamy nasz heap wszystkimi wierzcholkami! (nasze drzewo rozpinajace jest puste w tej sytuacji)

	insert(heap,0,0,position)
	for i in range(1,len(G)):
		elem = Node(i,float("inf"))
		heap.append(elem)
		position[i] = i
		#insert(heap,i,float("inf"),position)
	#heapify(heap,position) - z racji ze elementy są w pewnym sensie ulozone prawidlowo w heapie, nie trzeba korzystac z heapify
	#for elem in heap: print(elem.val,end=" ")
	#print(position)

	#za kazdym razem bedziemy wyciagac z heapu wierzcholek z minimalną wagą 
	# (do czasu gdy go wyjmiemy, wczesniej juz okreslimy
	# w petli for v,w in G[u] jego najlepszego rodzica! i stad ta waga minimalna)
	while len(heap) > 0:
		elem = get(heap,position)
		u = elem.val
		for v,w in G[u]:
			if position[v] != None and w < heap[position[v]].priority: #jesli wierzcholek nie byl przetwarzany (czyli jest w heapie) 
				parent[v] = u
				#musimy wierzcholkowi v przypisac nowy "key", czyli nowy priorytet! zmniejszony do wartosci "w"
				#gdy to zrobimy, to w heapie musimy podmienic jego priorytet
				decrease_key(heap,position,v,w)
	#wyniki:
	for i in range(1,len(G)): 
		print(parent[i]+1,i+1)


G = [[[1,28],[5,10]],[[0,28],[6,14],[2,16]],[[1,16],[3,12]],[[2,12],[6,18],[4,22]],[[5,25],[6,24],[3,22]],[[4,25],[0,10]],[[1,14],[4,24],[3,18]]]
PrimsAlgorithm(G)
