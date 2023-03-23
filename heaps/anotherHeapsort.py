def swap(lst,i,j):
    lst[i], lst[j] = lst[j], lst[i]
#maxHeap
def siftdown(lst,i,upper):
    while True:
        l,r = i*2 + 1, i*2 + 2
        if max(l,r) < upper:
            if lst[i] >= max(lst[l],lst[r]): break
            elif lst[l] > lst[r]:
                swap(lst,i,l)
                i = l
            else:
                swap(lst,i,r)
                i = r
        elif l < upper:
            if lst[l] > lst[i]:
                swap(lst,i,l)
                i = l
            else: break
        elif r < upper:
            if lst[r] > lst[i]:
                swap(lst,i,r)
                i = r
            else: break
        else: break

#better version of siftdown
def _siftdown(heap, i,upper):
        left = 2*i + 1
        right = 2*i + 2
        while (left < upper and heap[i] < heap[left]) or\
             (right < upper and heap[i] < heap[right]):
            biggest = left if (right >= len(heap) or heap[left] > heap[right]) else right
            heap[i], heap[biggest] = heap[biggest], heap[i]
            i = biggest
            left = 2*i + 1
            right = 2*i + 2
        
def heapsort(lst): #time complexity: O(nlogn), memory: O(1)
    #we do not have to check any leaf node so we start with parent node (we have to -1 in addition due to len())
    for j in range((len(lst)-2)//2, -1,-1): #heapify
        _siftdown(lst,j,len(lst))
    
    for end in range(len(lst)-1,0,-1): #we ignore 0-element because he is already sorted!!!!
        swap(lst,0,end)
        _siftdown(lst,0,end)
    return lst

#arr = [1,2,6,984,2,3,5,75,2,21,5,3,5,7,42,23]
#heapsort(arr)
#print(arr)

def sortH(arr,k):
    n = len(arr)
    for i in range(0,n-k+1):
        arr[i:k+i+1] = heapsort(arr[i:k+i+1])
        print(arr[i:k+i+1]) # np dla k = 2: trzeba dodac 1 gdyz kazdy element moze byc przesuniety o 2 miejsca czyli 1 el -> (2) to wsm daje 3 pozycje

arr = [2,4,1,6,3,5]
sortH(arr,2)   
print(arr)


#arr = [i for i in range(900000)]
#for i in range(1,900000):
#    arr[i-1],arr[i] = arr[i], arr[i-1]
#sortH(arr,1)
#print(arr)

