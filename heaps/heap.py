class Node:
    def __init__(self,val,priority):
        self.val = val
        self.priority = priority

def enqueue(values,val,priority):
    newNode = Node(val,priority)
    values.append(newNode)
    idx = len(values) - 1
    parentIdx = (idx - 1)//2
    #bubbling up
    while parentIdx >=0 and values[idx].priority > values[parentIdx].priority:
        values[idx],values[parentIdx] = values[parentIdx], values[idx]
        idx = parentIdx
        parentIdx = (idx - 1)//2
    return values

def dequeue(values):
    if(not(len(values))): return None
    oldMax = values[0]
    values[0] = values[len(values)-1]
    values.pop()
    if(not(len(values))): return oldMax
    #initializing useful variables:
    element = values[0]
    leng = len(values)
    idx = 0
    leftChild,rightChild = None,None
    while True:
        leftChildIdx = 2*idx + 1
        rightChildIdx = 2*idx + 2
        swap = None
        if leftChildIdx < leng:
            leftChild = values[leftChildIdx]
            if leftChild.priority > element.priority:
                swap = leftChildIdx
        if rightChildIdx < leng:
            rightChild = values[rightChildIdx]
            if (swap == None and rightChild.priority > element.priority) or \
                (swap != None and rightChild.priority > leftChild.priority):
                swap = rightChildIdx
        if swap == None: return oldMax
        #changing
        values[idx] = values[swap]
        values[swap] = element
        idx = swap

def display_heap(values):
    for elem in values:
        print(elem.val, end=" ")

def heap_init(values,lis): #works only for value being a character (due to ord() method)
    for elem in lis:
        priority = ord(elem)
        enqueue(values,elem,priority)


#----------------------------------------------------------------------
#for heap-min: #inside code:
def _siftup(heap,i):
    parent = (i-1)//2
    while i != 0 and heap[i] < heap[parent]:
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
        parent =  (i-1)//2
#for heap-min:
def _siftdown(heap,i,upper=None):
    left = 2*i + 1
    right = 2*i + 2
    if upper is None:
        upper = len(heap)
    while (left < upper and heap[i] < heap[left]) or \
        (right < upper and heap[i] < heap[right]):
        smallest = left if (right >= upper or heap[left] > heap[right]) else right
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
        left = 2*i + 1
        right = 2*i + 2

def insert(heap,element):
    heap.append(element)
    _siftup(heap,len(heap)-1)

def get_min(heap): #for min-heap
    return heap[0] if len(heap) > 0 else None

def extract_min(heap):
    if len(heap) == 0:
        return None
    minval = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    _siftdown(heap,0)
    return minval

def update_by_index(heap,i,new):
    old = heap[i]
    heap[i] = new
    if new < old:
        _siftup(heap,i)
    else:
        _siftdown(heap,i)

def update(heap,old,new):
    i = 0
    for elem in heap:
        if elem == old:
            update_by_index(heap,i,new)
            break
        else:
            i+=1
def heapify(arr): #time complexity: O(n)
    for i in range((len(arr)-1)//2,-1,-1):
        _siftdown(arr,i)
    


def heapsort(lst): #time complexity: O(nlogn), memory: O(1)
    #we do not have to check any leaf node so we start with parent node (we have to -1 in addition due to len())
    heapify(lst) #o(n)
    for end in range(len(lst)-1,0,-1): #we ignore 0-element because he is already sorted!!!!
        lst[0],lst[end] = lst[end],lst[0]
        _siftdown(lst,0,end)
    return lst

lst =[6,7,34,2,3,5,63,2,1,4,5,7,9,8,6]
heapsort(lst)
print(lst)




