class Node:
	
	def __init__(self,key=None):
		self.val=key
		self.next=None

def _siftup(heap,i):
    parent = (i-1)//2
    while i != 0 and heap[i].val < heap[parent].val:
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
        parent =  (i-1)//2

def _siftdown(heap,i):
    left = 2*i + 1
    right = 2*i + 2
    upper = len(heap)
    while (left < upper and heap[i].val > heap[left].val) or \
        (right < upper and heap[i].val > heap[right].val):
        smallest = left if (right >= upper or heap[left].val < heap[right].val) else right
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
        left = 2*i + 1
        right = 2*i + 2

def insert(heap,element):
    heap.append(element)
    _siftup(heap,len(heap)-1)


def extract_min(heap):
    if len(heap) == 0:
        return None
    minval = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    _siftdown(heap,0)
    return minval

def LL_heapsort(p,k):
    guardian = Node()
    guardian.next = p
    prev = guardian
    curr = p
    #k+1-size heap initialization    
    heap = []
    iter= 0
    while curr is not None and iter <= k:
        iter+=1
        tmp = curr.next
        curr.next = None
        insert(heap,curr)
        curr = tmp
    #last is out of the k-size-heap
    while prev is not None:
        prev.next = extract_min(heap)
        prev = prev.next
        if curr is not None:
            tmp = curr.next
            curr.next = None
            insert(heap,curr)  
            curr = tmp         
    return guardian.next

def make_linked_list(tab,flag=1):
    n = len(tab)
    if flag == 0: #bez wartownika
        first = None
        for i in range(n-1,-1,-1): #unshift
            temp = Node(tab[i]) 
            temp.next =first
            first = temp
        return first
    else:
        first =Node(None)
        for i in range(n-1,-1,-1):
            currNode = Node(tab[i])
            nextNode = first.next
            first.next = currNode
            currNode.next =nextNode
        return first


def display(first):
    currNode = first
    if currNode == None:
        print(" ")
        return False
    while currNode != None:
        print(currNode.val,end=" ")
        currNode = currNode.next
    print()
    return True

def display_tab(arr):
    for i in range(len(arr)):
        print(arr[i].val, end=" ")
    print()

first = make_linked_list([2,4,0,1,3,8,9,6,5,7,11,12,10,13],0)
first = LL_heapsort(first,3)
display(first)