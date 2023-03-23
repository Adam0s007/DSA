#Adam Biśta 
#w funkcji SortH dokonuje sie wybor jednego z 3 algorytmow sortowania ze wzgl na parametry n (dlugosc listy) oraz k

#heapsort dziala na zasadzie ciągłego wstawania do stery rozmiaru k+1 nowych node'ow oraz ciaglym wyciaganiu z niej elementow najmniejszych,
#zlozonosc czasowa algorytmu wynosi O(nlogk). Lepszy od mergesorta dla malych wartosci k w porownaniu do n

#InsertionSort przechodzi przez linked liste i przy zauwazeniu nieporządku przenosi element maksymalnie o k miejsc wstecz i szuka odpowiedniego ustawienia
#Zlozonosc czasowa wynosi O(n*k).
#dziala sprawnie dla malych wartosci n oraz k oraz dla k << n

#merge sort posiada dwie tablice. Pierwsza zawiera podlisty uporzadkowane. 
# Druga jest pusta i do niej zostają przypisane podlisty tak, ze kazde dwie  trzeba  polaczyc w jedną 
# i przypisac do drugiej tablicy. Petla powtarza sie poki długosc tablicy nie bedzie rowna 1.
#zlozonosc czasowa wynosi O(n*logk) - (dla wiekszych n szybszy od heapsorta)

#k = 0(1) => O(n)
#k = 0(log*n) => O(n*log*n)
#k = 0(n) => O(n^2)

from zad1testy import Node, runtests


def SortH(p,k):
    
    if k ==0:
        return p
    if k <= 10:
        return insertion_sort(p,k)
    n = get_leng(p)
    if k >= n-1:
        return merge_sort(p)
    if (k <=100 and n <= 2000):
        return insertion_sort(p,k)
    if k < 5000 and n <= 100000:
        return heapsort(p,k)
    return merge_sort(p)

def get_leng(first):
    curr = first
    l = 0
    while curr is not None:
        curr = curr.next
        l +=1
    return l

def insert_and_go_up(heap,element):
    heap.append(element)
    index = len(heap) - 1 
    idParent = (index-1)//2
    while index > 0 and heap[index].val < heap[idParent].val:
        heap[index], heap[idParent] = heap[idParent], heap[index]
        index = idParent
        idParent = (index-1)//2

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
        go_down(heap,i)

def go_down(heap,index):
    l = 2*index + 1
    r = 2*index + 2
    minim_id = index
    if l < len(heap) and heap[l].val < heap[minim_id].val:
        minim_id = l
    if r < len(heap) and heap[r].val < heap[minim_id].val:
        minim_id = r
    if minim_id is not index:
        heap[index], heap[minim_id] = heap[minim_id], heap[index]
        go_down(heap,minim_id)  

def heapsort(p,k):
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

def merge_sort(first):
    s_lists = [first]
    if first is None: return None
    while first.next is not None:
        if first.next.val < first.val:
            s_lists.append(first.next)
            nextNode =first.next
            first.next = None
            first = nextNode
        else:
            first = first.next
    
    while len(s_lists) > 1:
        newSorted = []
        for i in range(1,len(s_lists),2):
            newSorted.append(merge(s_lists[i],s_lists[i-1]))
        if (len(s_lists) & 1) == 1:
            newSorted.append(s_lists[-1])
        s_lists = newSorted
    return s_lists[0]

def merge(first1,first2):
    wsk1 = first1
    wsk2 = first2
    first3 = None
    if wsk1 is None:
        return first2
    if wsk2 is None:
        return first1
    if wsk1.val > wsk2.val:
        first3 = wsk2
        wsk2 = wsk2.next
        first3.next = None
    else:
        first3 = wsk1
        wsk1 = wsk1.next
        first3.next = None
    currNode = first3
    while wsk1 is not None and wsk2 is not None:
        if wsk1.val > wsk2.val:
            currNode.next = wsk2
            wsk2 = wsk2.next
            currNode = currNode.next
        else:
            currNode.next = wsk1
            wsk1 = wsk1.next
            currNode = currNode.next
    if wsk1 is not None:
        currNode.next = wsk1
    if wsk2 is not None:
        currNode.next = wsk2
    return first3

def insertion_sort(first,k):
    guard = Node()
    guard.next = first
    prevNode = first
    currNode = prevNode.next
    i = 0
    edge = guard
    while currNode is not None:
        if i > k:
            edge = edge.next
        if currNode.val >= prevNode.val:
            prevNode = currNode
            currNode = currNode.next
        else:
            pos = edge
            while currNode.val > pos.next.val:
                pos = pos.next
            prevNode.next = currNode.next
            currNode.next = pos.next
            pos.next = currNode
            currNode = prevNode.next
        i +=1
    return guard.next
    

runtests( SortH ) 
