# Dana jest tablica liczb rzeczywistych wielkości n reprezentująca
# kopiec minimum (array-based heap). Mając daną liczbę rzeczywistą x sprawdź, czy k-ty 
# najmniejszy element jest większy lub równy x.
#n - wielkosc kopca

#1) rozw to wyciaganie k elementow extractem, zlozonosc czasowa O(klogn)
# 2) rozw to przechodzenie przez caly kopiec i liczenie elementow mniejszych od x -> O(n)
# 3) rozw to wykorzystanie kopca, przechodzimy (rekurencyjnie) od gory i zliczamy elementy 
# jesli natrafimy na element wiekszy rowny x to konczymy zliczanie w danej czesci -> O(k)

#O(k)
def check_siftdown(arr,x,index,k):
    stack = [0]
    count = 0
    while len(stack) >0:
        index = stack.pop()
        if arr[index] < x:
            count+=1
            p1 = 2*index + 1
            p2 = 2*index + 2
            if p1 < len(arr):
                stack.append(p1)
            if p2 < len(arr):
                stack.append(p2)            
    return count < k #jesli k-ty elemen jest wiekszy lub rowny x to wczesniej musi byc count elementow mniejszych!

t = [2,3,4,6,5,8,12]
x = 5
print(check_siftdown(t,x,0))



