#sortowanie listy jednokierunkowej

class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

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

def insert(first,newNode):
    if first == None: #jesli lista jest pusta
        return newNode
    if newNode.val < first.val: #jesli wartosc pierwsza jest wieksza od zadanej
        newNode.next = first
        first = newNode
        return first
    curr = first
    while(curr.next != None and newNode.val > curr.next.val): #zauwaz ze nie uzywamy preva!
        curr = curr.next
    if curr.next is None:
        curr.next = newNode
        return first
    currNext = curr.next #ostatni przypadek to taki w ktorym znaleznismy sie pomiedzy elementami i tam trzeba wpiąć nowego node'a
    curr.next = newNode
    newNode.next = currNext

    return first


#newNode = Node(89)
#first = insert(first,newNode)    

def remove(first,elem):
    if first == None:
        return first
    if first.val == elem.val:
        first = first.next
        return first
    curr = first
    while curr.next != None and curr.next.val < elem.val:
        curr = curr.next
    if curr.next == None:
        return first
    if curr.next.val == elem.val:
        nextNode = curr.next.next #jesli to bedzie None to nic sie nie dzieje
        curr.next = nextNode
        return first

#main insertion function!:
def insertion_sort(first):
    output = None
    while first is not None:
        tmp = first
        first = remove(first,first) #pierwszy first -> z jakiej link listy usuwamy, drugi first to element do usuniecia jest firstem!
        tmp.next = None #to trzeba dac aby usunac stare powiazanie!!!
        output = insert(output,tmp)
    return output




#-------------------------------------------------------------------
#a tu kod z geeksforgeeks:
# Python implementation of above algorithm
# Node class
class Node:
	# Constructor to initialize the node object
	def __init__(self,val=None):
		self.val =val
		self.next = None
# function to sort a singly linked list using insertion sort
def insertionSort(head_ref):

	# Initialize sorted linked list
	sorted = None
	# Traverse the given linked list and insert every
	# node to sorted
	current = head_ref
	while (current != None):
		# Store next for next iteration
		next = current.next #potrzebne gdyz w sortedInsert usuwamy polaczenia
		# insert current in sorted linked list
		sorted = sortedInsert(sorted, current)
		# Update current
		current = next
	# Update head_ref to point to sorted linked list
	head_ref = sorted
	return head_ref

# function to insert a new_node in a list. Note that this
# function expects a pointer to head_ref as this can modify the
# head of the input linked list (similar to push())
def sortedInsert(head_ref, new_node):
	current = None	
	# Special case for the head end */
	if (head_ref == None or (head_ref).val >= new_node.val):
	
		new_node.next = head_ref
		head_ref = new_node
	
	else:
	
		# Locate the node before the point of insertion
		current = head_ref
		while (current.next != None and
			current.next.val < new_node.val):
			current = current.next
		new_node.next = current.next
		current.next = new_node
	return head_ref

# BELOW FUNCTIONS ARE JUST UTILITY TO TEST sortedInsert

# Function to print linked list */
def printList(head):
	temp = head
	while(temp != None):
		print( temp.val, end = " ")
		temp = temp.next
	
# A utility function to insert a node
# at the beginning of linked list
def push(head_ref, new_val):

	# allocate node
	new_node = Node(0)

	# put in the.val
	new_node.val = new_val

	# link the old list off the new node
	new_node.next = (head_ref)

	# move the head to point to the new node
	(head_ref) = new_node
	return head_ref

# Driver program to test above functions


# This code is contributed by Arnab Kundu

#best version of insertion sort on LL when k-sorted linked-list is set

#for k-sorted
def insertionSortList(head,k):
    guardian = Node()
    guardian.val = None
    guardian.next = head
    prev,cur = head,head.next
    i = 0
    while cur:
        if i == k:
            edge = guardian
        elif i > k:
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

first = make_linked_list([0,1,2,4,3,8,9,6,5,7,11,12,10,13],0)
first = insertionSortList(first,3)
display(first)

def insertionSortList(head):
    if head is None: return
    guardian = Node()
    guardian.val = None
    guardian.next = head
    prev,cur = head,head.next
    while cur:
        if cur.val >= prev.val:
            prev,cur = cur, cur.next
            continue     
        tmp = guardian
        while cur.val > tmp.next.val:
            tmp = tmp.next
        prev.next = cur.next #odpinanie node'a w zlym miejscu
        cur.next = tmp.next 
        tmp.next = cur      
        cur = prev.next #now we change our cur positon to prev.next
    return guardian.next,prev
