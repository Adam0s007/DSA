# Dana jest tablica zawierajaca n liczb z zakresu [0... n^2-1]. Napisz algorytm, ktory
# posortuje taką tablicę w czasie O(n).

# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.

def sortbyKey(tab,n,key):
    count = [0 for _ in range(n)]
    res = [0] * n
    for elem in tab:
        count[key(elem)] +=1
    for i in range(1,n):
        count[i] += count[i-1]
    for i in range(n-1,-1,-1):
        res[count[key(tab[i])]-1] = tab[i]
        count[key(tab[i])]-=1
    print(res)
    return res

def sort_this(tab,n):
    sorteD =sortbyKey(tab,n,lambda x: x%n) 
    return sortbyKey(sorteD,n,lambda x: x//n)

t = [5,8,9,7,5,32,5,5,120,67,6,54]
sort_this(t,len(t))
