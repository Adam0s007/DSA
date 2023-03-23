from zad1testy import Node, runtests

def SortH(p,k):
    guardian = Node()
    guardian.next = p
    prev1 = guardian
    curr1 = p
    while curr1:
        curr2 = curr1
        count = 0
        while count < k and curr2.next:
            curr2 = curr2.next
            count+=1
        tmp = curr2.next #zapis kolejnej wartosci
        curr2.next = None
        prev1.next = None
        curr1,curr2 =  insertionSortList(curr1)
        prev1.next = curr1
        curr2.next = tmp
        prev1 = curr1
        curr1 = curr1.next
        
    return guardian.next


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

def selectionSort(head):
    temp = head
    # Traverse the List
    prev = temp
    while (temp):
        minn = temp
        r = temp.next
        # Traverse the unsorted sublist
        while (r):
            if (minn.val > r.val):
                minn = r    
            r = r.next   
        # Swap val
        x = temp.val
        temp.val = minn.val
        minn.val = x
        prev = temp
        temp = temp.next
    return head,prev


runtests( SortH ) 
