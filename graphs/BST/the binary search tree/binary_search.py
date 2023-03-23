#Jesli elementy w tablicy zdublowane, zwroci losowy element ze zdublowanych
#jest szybki
def find(tab,el):
    p = 0
    k = len(tab)-1
    while p <=k:
        sr = (p+k)//2
        if el==tab[sr]:
            return sr
        elif el>tab[sr]:
            p = sr + 1
        else:
            k = sr-1
    return -1

#gdy mamy przedzialy i majac startingPoint przedzialu pod indeksem init_ind
#  chcemy znalezc ending point innego przedzialu takiego ze ending_point < startingPoint:
# zalozenie: tablica jest posortowana rosnaco ze wzgledu na konce przedzialu
 
def binary_search(T,value,init_index): #bedziemy szukac po starting Pointcie Akademika! Najblizszy ending point innego akademika!
    l,r = 0,len(T)-1
    middle = None
    while l <= r:
        middle = (r+l)//2
        if T[middle][1] > value: r = middle - 1
        elif T[middle][1] < value: l = middle + 1
        else: return middle
    if middle == None: return -1
    if middle == init_index and init_index == 0: return -1
    if middle < 0 or middle > len(T): return -1
    if T[middle][1] < value: return middle
    return middle-1


#algorytm zwraca pierwsze wystapienie danego elementu!
#jest porownywalnie szybki jak wczesniejszy (a moze nawet szybszy)
def find2(tab,el):
    p= 0
    k = len(tab)-1
    while p<=k: #jesli chcemy wyznaczyc ostatnie wystapienie elem, nalezy zmienic nierownosc slaba na silna: <= na <
        sr = (p+k)//2
        if el > tab[sr]:  #jesli chcemy wyznaczyc ostatnie wystapienie elem, nalezy zmienic nierownosc silną na slabą: > na >=
            p = sr + 1
        else:
            k = sr - 1
    if p < len(tab) and el == tab[p]: return p
    return -1

tab = [2,5,5,5,7,13,17,17,19,23]
print(find2(tab,5))
print(find(tab,5))

