# Python program for the above approach
#UWAGA!!!!! TO NIE JEST STABILNE SORTOWANIE!

# Node Class
class Node:
	def __init__(self,key):
		self.val=key
		self.next=None

# Function to merge sort
def merge_sort(first):
    sorted_lists = [first] #tu juz zapisujemy pierwszy jakis przedzial
    if first is None: return
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
            new_sorted_lists.append(merge(sorted_lists[i],sorted_lists[i-1]))
        if (len(sorted_lists) % 2) == 1: #poza petlą!
            new_sorted_lists.append(sorted_lists[-1]) #na pewno ostatni element zostanie zachowany jesli tablica jest nieparzystego rozmiaru
        sorted_lists = new_sorted_lists #dlatego przedzialy beda sie zmniejszac!
    return sorted_lists[0] #gdy zostanie juz jeden przedzial, to bedzie on rosnacy!!!


# Function to merge two linked lists


def merge(head1,head2):
    p1 = head1
    p2 = head2
    new_list = None
    if p1 is None:
        return head2
    if p2 is None:
        return head1
    if p1.val <= p2.val:
        new_list = p1
        p1 = p1.next
        new_list.next = None #wazne, potem okreslimy co bedzie nextem
    else:
        new_list = p2
        p2 = p2.next
        new_list.next = None #wazne, potem okreslimy co bedzie nextem
    k = new_list
    while p1 is not None and p2 is not None:
        if p1.val <= p2.val:
            k.next = p1
            p1 = p1.next
        else:
            k.next = p2
            p2 = p2.next
        k = k.next
    if p1 is not None:
        k.next = p1
    if p2 is not None:
        k.next = p2
    return new_list



# Function to print list
def printList(head):
	while (head != None):
		print(head.val,end=" ")
		head=head.next

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
from random import randint
# Driver Code
head = make_linked_list([-i for i in range(40)],0)
head = merge_sort(head)
display(head)

# This code is contributed by avanitrachhadiya2155
