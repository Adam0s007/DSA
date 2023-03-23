from re import L
from zad1testy import Node, runtests
class Node:
	
	def __init__(self,key=None):
		self.val=key
		self.next=None


def SortH(p,k):
    if k == 0:
        return p
    if k <= 10:
        print("insertionsort")
        return insertionSortList(p,k)
    n = get_leng(p)
    
    if k >= n-1 and n <= 100:
        print("insertionsort")
        return insertionSortList(p,k)
    if k >= n-1 and n > 100:
        print("mergesort")
        return merge_sort(p)
    if ((k <=3000) and n <= 5000):
        print("insertionsort")
        return  insertionSortList(p,k)
    if n >= 100000:
        print("mergesort")
        return merge_sort(p)
    print("heapsort")
    return heapsort(p,k)
    



def get_leng(first):
    curr = first
    l = 0
    while curr != None:
        curr = curr.next
        l +=1
    return l

def go_up(heap,i):
    parent = (i-1)//2
    while i > 0 and heap[i].val < heap[parent].val:
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
        parent =  (i-1)//2

def insertH(heap,element):
    heap.append(element)
    go_up(heap,len(heap)-1)


def extr_min(heap):
    if len(heap) == 0: return None
    minim = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    go_down(heap,0)
    return minim

def heapsort(p,k): 
    guardian = Node()
    guardian.next = p
    prev = guardian
    curr = p 
    heap = []
    iter= 0
    while curr is not None and iter <= k: 
        iter+=1
        tmp = curr.next
        curr.next = None
        insertH(heap,curr) 
        curr = tmp
    while prev is not None: 
        prev.next = extr_min(heap) 
        prev = prev.next
        if curr is not None:
            tmp = curr.next
            curr.next = None
            insertH(heap,curr)
            curr = tmp         
    return guardian.next


def go_down(Arr,i):
    l = 2*i+1
    r = 2*i + 2
    max_id = i
    n = len(Arr)
    if l < n and Arr[l].val < Arr[max_id].val:
        max_id = l
    if r < n and Arr[r].val < Arr[max_id].val:
        max_id = r
    if max_id is not i:
        Arr[i], Arr[max_id] = Arr[max_id], Arr[i]
        go_down(Arr,max_id)


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


# Function to merge two linked lists


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


def insertionSortList(head,k):
    guardian = Node()
    guardian.next = head
    prev = head
    cur = prev.next
    i = 0
    edge = guardian
    while cur:
        if i > k:
            edge = edge.next
        if cur.val >= prev.val:
            prev = cur
            cur = cur.next
        else:     
            pos = edge
            while cur.val > pos.next.val:
                pos = pos.next
            prev.next = cur.next #odpinanie
            cur.next = pos.next #przypinanie
            pos.next = cur      
            cur = prev.next #now we change our cur positon to prev.next
        i+=1
    return guardian.next


runtests( SortH ) 
