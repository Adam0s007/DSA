class Node:
    def _init__(self,val=None,next=None):
        self.val = val
        self.next = next


def go_down(heap,index):  #max-heap
    l = 2*index + 1
    r = 2*index + 2
    minim_id = index
    if l < len(heap) and heap[l] > heap[minim_id]: 
        minim_id = l
    if r < len(heap) and heap[r] > heap[minim_id]:
        minim_id = r
    if minim_id is not index:
        heap[index], heap[minim_id] = heap[minim_id], heap[index]
        go_down(heap,minim_id)

def extr_min(heap):
    if len(heap) != 0:
        minim = heap[0]
        heap[0] = heap[len(heap)-1]
        heap.pop()
        go_down(heap,0)
        return minim
    return None


def heapify(heap):
    for i in range((len(heap)-2)//2,-1,-1):
        _siftdown(heap,i,len(heap))



def insert_and_go_up(heap,element): #for maxheap
    heap.append(element)
    index = len(heap) - 1 
    idParent = (index-1)//2
    while index > 0 and heap[index] > heap[idParent]:
        heap[index], heap[idParent] = heap[idParent], heap[index]
        index = idParent
        idParent = (index-1)//2


def _siftup(heap,i): #for max-heap
    parent = (i-1)//2
    while i != 0 and heap[i] > heap[parent]:
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
        parent =  (i-1)//2

def _siftdown(heap,index,n): #for max-heap
    l = 2*index + 1
    r = 2*index + 2
    swap = index
    if l < n and heap[l] > heap[swap]:
        swap = l
    if r < n and heap[r] > heap[swap]:
        swap = r
    if swap is not index:
        heap[index], heap[swap] = heap[swap], heap[index]
        _siftdown(heap,swap,n)



def heapsort(lst): #time complexity: O(nlogn), memory: O(1)
    #we do not have to check any leaf node so we start with parent node (we have to -1 in addition due to len())
    heapify(lst) #o(n)
    for end in range(len(lst)-1,0,-1): #we ignore 0-element because he is already sorted!!!!
        lst[0],lst[end] = lst[end],lst[0]
        _siftdown(lst,0,end)
    return lst


t = [1,7,4,2,4,0,13,2,2,2,5,7,89,9]
print(heapsort(t))


def update_by_index(heap,i,new): #for max-heap
    old = heap[i]
    heap[i] = new
    if new < old:
        _siftdown(heap,i,len(heap))
    elif new > old:
        _siftup(heap,i)

def update(heap,old,new):
    i = 0
    for elem in heap:
        if elem == old:
            update_by_index(heap,i,new)
            break
        else:
            i+=1

#for k-sorted arr with LL
def heapsortK(p,k):
    guard = Node()
    guard.next = p
    prevNode,currNode = guard,p
    heap = []
    iter = 0
    while currNode is not None and iter <=k:
        iter += 1
        nextNode = currNode.next
        currNode.next = None
        heap.append(currNode)
        currNode = nextNode
    heapify(heap)
    while prevNode is not None: 
        prevNode.next = extr_min(heap) #jednoczenie zabieramy z heapu
        prevNode = prevNode.next
        if currNode is not None: 
            nextNode = currNode.next
            currNode.next = None
            insert_and_go_up(heap,currNode) #jednoczenie wkladamy do heapu
            currNode = nextNode
    return guard.next