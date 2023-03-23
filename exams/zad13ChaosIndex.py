from zad13testy import runtests
import time
import random

class Node:
    def __init__(self,val,index):
        self.index = index
        self.val = val
        self.next = None



def merge_sort(head):
	if (head == None or head.next == None):
		return head
	mid = findMid(head) #O(N) nigdy nie wlozymy tam Node'a bedącego Nonem przez ifa wyzej
	head2 = mid.next
	mid.next = None #wskazanie sie zmienia jedynie!
	newHead1 = merge_sort(head)
	newHead2 = merge_sort(head2)
	finalHead = merge(newHead1, newHead2)
	return finalHead

# Function to merge two linked lists
def merge(head1,head2):
	merged = Node(-1,-1) #wartownik
	
	temp = merged
	while (head1 != None and head2 != None):
		if (head1.val <= head2.val):
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

def makeLL(T):
    head = Node(T[0],0)
    curr = head
    for i in range(1,len(T)):
        curr.next = Node(T[i],i)
        curr = curr.next 
    return head

def traverse(first):
    curr = first
    while curr:
        print(curr.val,curr.index,end=" , ")
        curr = curr.next
#trzeba zastosowac sortowanie stabilne!
def chaos_index( T ):
    first = makeLL(T)
    first = merge_sort(first)
    traverse(first)
    k = 0
    curr = first
    for i in range(len(T)):
        k = max(k,abs(curr.index - i))
        curr = curr.next

    return k



runtests( chaos_index )
