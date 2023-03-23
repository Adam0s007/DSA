#A = {a(1),...,a(n)} - posortowany ciąg liczb naturalnych
#|A| = n, dla kazdego i: a(i) nalezy do zbioru {0,...,m} gdzie: n < m
#Znajdz najmniejszą liczbę x nalezacą do liczb naturalnych, takie ze x nie nalezy do zbioru A
 

def find_min_not_belonging(arr):
    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] > 1:
            return arr[i-1]+1
#print(find_min_not_belonging(arr))
arr = [1,2,3,4,6,7,8,9,12,13,14]
print(find_min_not_belonging(arr))

        
            
                    

        