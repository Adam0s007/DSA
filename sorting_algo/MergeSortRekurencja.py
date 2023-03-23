from typing import final


class Node:
	
	def __init__(self,key):
		self.val=key
		self.next=None

def MiddleOfLinkedList(first):   #znajdujemy środek linked_listy
    a=first
    b=first.next
    while b is not None and b.next is not None:
        a=a.next
        b=b.next.next
    
    return a




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


def MergeSort(first):   #sortujemy jedną listę

    if first is None or first.next is None:
        return first

    middle=MiddleOfLinkedList(first)
    
    beginning_right=middle.next
    middle.next = None
    first = MergeSort(first)
    beginning_right = MergeSort(beginning_right)
    
    return merge(first,beginning_right)

def merge(head1,head2):
	merged = Node(-1) #wartownik
	
	temp = merged
	while (head1 != None and head2 != None):
		if (head1.val < head2.val):
			temp.next = head1
			head1 = head1.next
		else:
			temp.next = head2
			head2 = head2.next
		temp = temp.next
	
	if head1:
		temp.next = head1
	if head2:
		temp.next = head2

	return merged.next

first = make_linked_list([6,3,7,8,5,3,4,6,8,5,3423,6,7,432,3532,3443],0)
first = MergeSort(first)
display(first)