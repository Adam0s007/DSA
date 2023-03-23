class Node:
	
	def __init__(self,key=None):
		self.val=key
		self.next=None

#for k sorted arr
def bubbleSort(first,n,k):
    guardian = Node()
    guardian.next = first
    prev  = guardian
    for i in range(k):
        prev  = guardian
        curr = guardian.next
        swapped = 0
        for j in range(n-i-1):
            if curr != None: 
                p1 = curr
                p2 = p1.next
                if p2 != None:    
                    if(p1.val > p2.val):
                        tmp = p2.next
                        swapped = 1
                        prev.next = p2
                        p2.next = p1
                        p1.next = tmp
                        curr = p2 #nalezy przestawic curr
            prev = curr
            curr = curr.next
        if swapped == 0:
            break
    return guardian.next


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

def get_leng(first):
    curr = first
    l = 0
    while curr != None:
        curr = curr.next
        l +=1
    return l

first = make_linked_list([2,4,1,6,4,1],0)
n = get_leng(first)
first = bubbleSort(first,n,6)
display(first)