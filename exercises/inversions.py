
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

#fajna funkcja:
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


#using merge-sort
def inversions(first):
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
    inversions = 0
    while len(sorted_lists) > 1: #dopoki istnieje wiecej niz 1 przedzial 
        new_sorted_lists = []
        for i in range(1,len(sorted_lists),2):
            p, counter = merge_(sorted_lists[i-1],sorted_lists[i])
            inversions += counter 
            new_sorted_lists.append(p)

        if (len(sorted_lists) & 1) == 1:
            new_sorted_lists.append(sorted_lists[-1])
        sorted_lists = new_sorted_lists #dlatego przedzialy beda sie zmniejszac!
    return sorted_lists[0],inversions #gdy zostanie juz jeden przedzial, to bedzie on rosnacy!!!




def merge_(head1,head2): #guarantee memory O(1)
    inv = 0
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
        inv+=1
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
            inv+=1
            k.next = wsk2
            wsk2 = wsk2.next
            k = k.next
    if wsk1 is not None:
        k.next = wsk1
    if wsk2 is not None:
        k.next = wsk2
    return new_list,inv

first = make_linked_list([1, 3, 2, 7, 5, 6],0)

sec, inv = inversions(first)
display(sec)
print(inv)