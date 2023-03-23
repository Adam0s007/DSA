from zad5testy import runtests
from queue import PriorityQueue
#Adam Biśta

#Tworzymy tablice dp[] ktora zapamietuje ile mamy paliwa w danej chwili. 
#Do dzialania algorytmu stosujemy kolejkę priorytetową, do ktorej za kazdym razem wrzucamy elementy
# tablicy T, jesli wartosc elementu > 0. Aby nie było powtórzeń stosujemy tablicę memo[], w której
# zapisujemy jeden z 3 stanów dla kazdego elementu tablicy T:
# 0 - element nigdy nie został dodany do kolejki
# 1 - element znajduje się w kolejce
# 2 - element był w kolejce i został z niej usunięty

# zapis wartosci do tablicy dp[] odbywa sie w nastepujacy sposob:
# - jesli dla danego indeksu i element tablicy T[i] nie był wykorzystywany (czyli jego memo[i] =/= 2)
#to bierzemy poprzedni element zmniejszony o 1 i zapisujemy go do dp[i]
# - jeśli element tablicy T[i] został zabrany z kolejki (tzn zostal wykorzystany i jego memo[i] == 2)
# to wtedy do dp[i] dodajemy zmniejszoną wartość o 1 dp[i-1] oraz dodajemy T[i]

# jesli po zastosowaniu powyzszych operacji dp[i] jest rowne 0, to musimy wyciagnac z kolejki element
#o najwiekszej ilosci paliwa!, przestawiamy indeks na odpowiednie miejsce gdzie dodajemy najwiecej paliwa

#Zlozonosci:
#memory complexity: O(n)
#time complexity: O(n*N*logk) n - dlugosc tablicy T[i], k - dlugosc kolejki priorytetowej
# N  - ilosc operacji dequeue oraz enqueue na kolejce  

class Node:
    def __init__(self,val,priority):
        self.val = val
        self.priority = priority

def go_down(heap,index): 
    l = 2*index + 1
    r = 2*index + 2
    minim_id = index
    if l < len(heap) and heap[l].priority > heap[minim_id].priority: 
        minim_id = l
    if r < len(heap) and heap[r].priority > heap[minim_id].priority:
        minim_id = r
    if minim_id is not index:
        heap[index], heap[minim_id] = heap[minim_id], heap[index]
        go_down(heap,minim_id)

def dequeue(heap):
    minim = heap[0]
    heap[0] = heap[len(heap)-1]
    heap.pop()
    go_down(heap,0)
    return minim
    

def enqueue(heap,val,priority): #for maxheap
    element =Node(val,priority)
    heap.append(element)
    index = len(heap) - 1 
    idParent = (index-1)//2
    while index > 0 and heap[index].priority > heap[idParent].priority:
        heap[index], heap[idParent] = heap[idParent], heap[index]
        index = idParent
        idParent = (index-1)//2

def plan(T):
    heap = []
    maks_ind = T[0]
    ans = [0]
    prev_ind = 0
    while maks_ind < len(T)-1:
        for i in range(prev_ind+1, maks_ind+1):
            if T[i]: enqueue(heap,i,T[i])
        elem = dequeue(heap)
        ans.append(elem.val)
        prev_ind = maks_ind       
        maks_ind += elem.priority
    return sorted(ans)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )