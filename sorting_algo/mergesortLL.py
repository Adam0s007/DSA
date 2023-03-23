# Python program for the above approach
#UWAGA!!!!!!!!!!!! TO JEST STABILNE
# Node Class
class Node:
	
	def __init__(self,key):
		self.val=key
		self.next=None

# Function to merge sort
def mergeSort(head):
	if (head == None or head.next == None):
		return head
	mid = findMid(head) #O(N) nigdy nie wlozymy tam Node'a bedącego Nonem przez ifa wyzej
	head2 = mid.next
	mid.next = None #wskazanie sie zmienia jedynie! Rozdzial na dwie listy
	newHead1 = mergeSort(head)
	newHead2 = mergeSort(head2)
	finalHead = merge(newHead1, newHead2)
	return finalHead

# Function to merge two linked lists

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
	elif head2:
		temp.next = head2
	return merged.next

# Find mid using The Tortoise and The Hare approach
def findMid(head):
	slow = head
	fast = head.next
	while (fast != None and fast.next != None):
		slow = slow.next
		fast = fast.next.next
	return slow

# Function to print list
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

# Apply merge Sort
head = make_linked_list([-i for i in range(10000)],0)
head = mergeSort(head)
print("\nSorted Linked List is: \n")

display(head)

# This code is contributed by avanitrachhadiya2155
