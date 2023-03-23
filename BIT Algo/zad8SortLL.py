# dana jest klasa: 
# class Node:
#     val = 0
#     next = None
# reprezentująca węzeł jednokierunkowego łancucha odsyłaczowego, w którym wartości val
# poszczególnych węzłów zostały wygenerowane zgodnie z rozkładem jednostajnym na przedziale [a,b].
# Napisz procedurę sort(first),ktora sortuje taką listę. Funkcja powinna być jak najszybsza
import math

class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next


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
        return False
    while currNode != None:
        print(currNode.val,end=" ")
        currNode = currNode.next
    print()
    return True

def getProperties(first):
    maksim = 0
    minim = None
    leng =0
    curr = first
    while curr:
        if minim == None or curr.val < minim:
            minim = curr.val
        if curr.val > maksim:
            maksim = curr.val
        leng+=1
        curr = curr.next
    return maksim,minim,leng

def add(first,newNode):
    if  first == None:
        return newNode
    newNode.next = first
    first = newNode
    return first


def traverse(first):
    p = first
    while p.next:
        p = p.next #nie trzeba tworzyc preva, bo po co skoro while wykona sie dopoki nie osiagniemy ostatniego elementu
    return p #zwraca pierwszy o ostatni!

def bucketSort_LL(first): #zalozmy ze znamy przedzial wartosc [minim,maksim]
    maksim,minim,n = getProperties(first)
    buckets = [None for _ in range(minim,maksim+1)]
    curr = first
    for i in range(n):
        nextNode = curr.next
        curr.next = None
        buckets[curr.val-minim] = add(buckets[curr.val-minim],curr)
        curr = nextNode
    ans = buckets[0]
    p = ans
    while p.next:
        p = p.next
    last = p
    for i in range(1,maksim+1-minim):
        if buckets[i]:
            last.next = buckets[i]
            last = traverse(last)
    return ans
            
from random import randint


first = make_linked_list([randint(25,50) for i in range(30)],0)
display(first)
print()
first = bucketSort_LL(first)
display(first)
def insertionSortList(head):
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
        prev.next = cur.next
        cur.next = tmp.next 
        tmp.next = cur      
        cur = prev.next #now we change our cur positon to prev.next
    return guardian.next,prev
