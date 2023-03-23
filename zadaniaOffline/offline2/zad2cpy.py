#from zad2testy import runtests


def depth(L):
    quicksort1(L)
    print(L)
    i = 0
    prevEnd = L[i][1]
    prevStart = L[i][0]
    actual = 0
    i +=1
    while i < len(L):
        if prevEnd >= L[i][1] and prevStart <= L[i][0]: #end
            actual+=1
        i+=1 
    return actual

def quicksort1(T): #O(nlogn)
    stos = []
    stos.append((0,len(T)-1)) #na stos juz trzeba coś wlozyc
    while len(stos)>0: #dopoki stos cokolwiek zawiera
        left,right = stos.pop()
        #powtorka kodu z quicksort_rek:
        i = left
        j = right
        pivot =T[(left+right)//2]
        while i <= j:
            while T[i][1] > pivot[1]:
                i+=1
            while T[j][1] < pivot[1]:
                j-=1
            if i<=j:
                T[j], T[i] = T[i], T[j]
                i+=1
                j-=1 
        if left < j: #tutaj ponizej zmieniamy:
            stos.append((left,j))
        if i < right: #tutaj ponizej zmieniamy:
            stos.append((i,right)) 

T = [[2,8],[3,4],[9,5],[2,3],[2,2],[9,12],[9,15]]
quicksort1(T)
print(T)    
#runtests( depth ) 
