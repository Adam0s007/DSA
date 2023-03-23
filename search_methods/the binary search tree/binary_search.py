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

