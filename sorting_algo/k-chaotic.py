
class Node:
	
	def __init__(self,key=None):
		self.val=key
		self.next=None


def get_leng(first):
    curr = first
    l = 0
    while curr != None:
        curr = curr.next
        l +=1
    return l


#bubble sort for k sorted LL:
def bubbleSort(first,n,k):
    guardian = Node()
    guardian.next = first
    prev  = guardian
    for i in range(k):
        prev  = guardian
        curr = guardian.next
        swap = None
        for j in range(n-i-1):
            if curr is not None: 
                wsk1 = curr
                wsk2 = curr.next
                if wsk2 is not None:    
                    if(wsk1.val > wsk2.val):
                        tmp = wsk2.next
                        swapped = 1
                        prev.next = wsk2
                        wsk2.next = wsk1
                        wsk1.next = tmp
                        curr = wsk2 #nalezy przestawic curr
            prev = curr
            curr = curr.next
        if swapped is None:
            break
    return guardian.next



def _siftup(heap,i):
    parent = (i-1)//2
    while i != 0 and heap[i].val < heap[parent].val:
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
        parent =  (i-1)//2

def _siftdown(heap,i):
    left = 2*i + 1
    right = 2*i + 2
    leng = len(heap)
    while (left < leng and heap[i].val > heap[left].val) or \
        (right < leng and heap[i].val > heap[right].val):
        smallest = left if (right >= leng or heap[left].val < heap[right].val) else right
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

#heapsort for k-sorted LL
def LL_heapsort(p,k): #Time: O[ (2N + 1)logk ] 
    guardian = Node()
    guardian.next = p
    prev = guardian
    curr = p
    #k+1-size heap initialization    
    heap = []
    iter= 0
    while curr is not None and iter <= k: #O(K) - heapify
        iter+=1
        tmp = curr.next
        curr.next = None
        insert(heap,curr) 
        curr = tmp
    #curr is out of the k-size-heap
    while prev is not None: #time : O[ (n-3(k+1)log(k+1) ]
        prev.next = extract_min(heap) #(n-(k+1))log(k+1)
        prev = prev.next
        if curr is not None:
            tmp = curr.next
            curr.next = None
            insert(heap,curr) ##(n-2(k+1))log(k+1)
            curr = tmp         
    return guardian.next


#merge sort k-sorted LL
#----------------------------------------------------------------
def merge_sort(first):
    sorted_lists = [first] #tu juz zapisujemy pierwszy jakis przedzial
    if first is None: return None
    while first.next is not None: #szukamy przedzialow rosonacych
        if first.next.val < first.val: #jesli nastepny jest mniejszy od poprzedniego (to robimy przedzial)
            sorted_lists.append(first.next) #dodajemy kolejny przedzial 
            tmp = first.next#zapisujemy nast element
            first.next = None #zrywamy polaczenie poprzedniego przedzialu
            first = tmp #przesuwammy first na nowy przedzial!
        else:
            first = first.next #rozpatrujemy kolejne elementy

    #gdy juz mamy tablice z przedzialami:
    while len(sorted_lists) > 1: #dopoki istnieje wiecej niz 1 przedzial 
        new_sorted_lists = []
        for i in range(1,len(sorted_lists),2):
            new_sorted_lists.append(merge_(sorted_lists[i],sorted_lists[i-1]))
        if (len(sorted_lists) & 1) == 1:
            new_sorted_lists.append(sorted_lists[-1])
        sorted_lists = new_sorted_lists #dlatego przedzialy beda sie zmniejszac!
    return sorted_lists[0] #gdy zostanie juz jeden przedzial, to bedzie on rosnacy!!!




def merge_(head1,head2): #guarantee memory O(1)
    wsk1 = head1
    wsk2 = head2
    new_list = None
    if wsk1 is None:
        return head2
    if wsk2 is None:
        return head1
    if wsk1.val <= wsk2.val:
        new_list = wsk1
        wsk1 = wsk1.next
        new_list.next = None
    else:
        new_list = wsk2
        wsk2 = wsk2.next
        new_list.next = None
    k = new_list
    while wsk1 is not None and wsk2 is not None:
        if wsk1.val <= wsk2.val:
            k.next = wsk1
            wsk1 = wsk1.next
            k = k.next
        else:
            k.next = wsk2
            wsk2 = wsk2.next
            k = k.next
    if wsk1 is not None:
        k.next = wsk1
    if wsk2 is not None:
        k.next = wsk2
    return new_list

#insertion sort k-sorted LL
def insertionSortList(head,k):
    guardian = Node()
    guardian.val = None
    guardian.next = head
    prev,cur = head,head.next
    i = 0
    edge = guardian
    while cur:
        if i > k:
            edge = edge.next
        
        if cur.val >= prev.val:
            prev = cur
            cur = cur.next
        else:     
            tmp = edge
            while cur.val > tmp.next.val:
                tmp = tmp.next
            prev.next = cur.next #odpinanie
            cur.next = tmp.next #przypinanie
            tmp.next = cur      
            cur = prev.next #now we change our cur positon to prev.next
        i+=1
    return guardian.next

