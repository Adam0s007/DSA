from math import log2
from math import log10
from math import floor
import unicodedata

def dwojkowy(liczba):
    strin=""
    #robimy dlugosc liczby binarnej jesli nie znamy log2 w ten sposob:
    l = 0
    temp = liczba
    while temp > 0:
        temp //=2
        l+=1
    #albo mozna tak:    
    dl = floor(log2(liczba))+1
    for i in range(dl):
        strin =  chr(liczba%2+48) + strin 
        liczba//=2
    return strin




#print(12.3)
#num  = 2e-23 
#print(num)

#print(~13)
#print(3+4j)

#zespolone = [3+4j,3.0+4.0j,2j]
#for i in zespolone:
#    print(i)

#print(16>>2)
print(dwojkowy(6))
print(dwojkowy(6*2))
print(dwojkowy(6<<1))
print(dwojkowy(6<<2))
print(dwojkowy(6<<3))
print(dwojkowy(6<<4))
print(dwojkowy(6>>1))
print(dwojkowy(6>>2))


#123 * 10^3 --> 123 - mantysa, 10^3 , 3 -> cecha

print(round(2.49)) #zwroci 2
print(round(2.50)) #zwroci i tak 2!!!
print(round(2.501)) #zwroci 3
print(round(2.51)) #zwroci 3

#priorytety: w praktycznie wszystkich jezykach programowania jest uwzgledniania kolejnosc wyk dzialan

#1) potegowanie
#2) dzielenie, modulo
#3) dodawanie, odejmowanie

#caly bajt - 256 - bo 8 bitow, bit - 2 a tu mamy:
#2 - 2 - 2 - 2 - 2 - 2 - 2 - 2 => 2^8 = 256
#w ascii - numerowane od 0 do 255 -> lacznie: 256 znakow

# 0 - 10: 48-57
# a- z: 97 - 122
# A-Z: 65-90
#spacja = 32

# rozszerzony ascii: ma do 256 
#znak diakretyzowany - ą, ę
#te ogonki = znaki diakretyczne


#UNICODE - to tylko tablica znakow
#zapis tych znakow to: UTF-8, UCS-2, UCS-4 itd.

napis = '''Ala i ola
Ida do domu ''' #dzieki 3 cudzyslowia/apostrofa to mozliwe
print(napis)

a = 'ala'
b = a #kopia
print(a)
print(b)
a = 'OLA'
print(a)
print(b) #kopia

c = a[:]
print(c)