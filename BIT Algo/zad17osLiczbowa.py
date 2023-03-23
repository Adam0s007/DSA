# Dane jest n punktow na osi liczbowej jednowymiarowej.
# Napisz algorytm, ktory stwierdzi, w ktorym z nich należy wybudować dom,
#  tak aby suma euklidesowych odleglosci od tego punktu 
#  do wszystkich pozostalych byla minimalna. Nalezy zwrocic rowniez tę sumę.
#  Algorytm powinien być jak najszybszy. 

#quickselectem znalezc wartosc kryjącą się pod srodkowym indeksem tablicy w posortowanej tablicy!
#uw - nie sortujemy tablicy quickselectem!!!

def quickSelect(nums): #O(n), pessimistic: O(n^2)
    k = len(nums)//2 #finding the middle in sorted arr (nums is unsorted)
    def qSelect(l,r):
        #partition:
        pivot, p = nums[r],l
        for i in range(l,r):
            if nums[i] <= pivot: #ascending order preserved
                nums[p], nums[i] = nums[i], nums[p]
                p+=1
        nums[p], nums[r] = nums[r], nums[p]
        if p > k: return qSelect(l, p-1)
        elif p < k: return qSelect(p+1,r)
        else: return nums[p]

    value = qSelect(0,len(nums)-1)
    suma = 0
    for i in range(len(nums)):
        suma += abs(nums[i] - value) #for the same point we have zero so everything is ok
    return suma

t = [5,8,9,3,1,34,6,7,6,42,-3,5,64,-3,445,7]

import math
def brute_force(t):
    minim = math.inf
    for i in t:
        suma = 0
        for j in t:
            suma += abs(i - j)
        minim = min(suma,minim)
    return minim

print(brute_force(t))
print(quickSelect(t))