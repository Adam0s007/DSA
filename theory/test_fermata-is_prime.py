#1) Jezeli p jest liczba pierwszą, to dla dowolnej liczby calkowitej a:
#(a^p - a) mod p == 0 !! (liczba a^p - a jest podz przez p)

# 2) Jezeli a jest niepodzielne przez p to:
#  a^(p-1) mod p == 1 (to zastosujemy do algorytmu przy wyborze wybranej liczby n elementow)

#Niech a,p bedą liczbami naturalnymi, takimi że 1 < a<p
#Jezeli a^(p-1) mod p != 1 to p NIE JEST liczbą pierwszą, 
#liczbe a nazywamy "świadkiem zlozonosci" liczby p

#Jesli p ma jednego swiadka zlozonosci, to ma ich co najmniej
# (n-1)/2

from random import randint
from math import gcd

def power(a,k,n): #potegowanie modulo n: (a^k mod n) - w pythonie wbudowana funkcja pow(a,k,n)

    r = 1 #result
    x = a%n #przypisywanie wartosci a mod n do x: x = a mod n
    while k>0:
        if k%2==1: r = r*x%n #jesli wykladnik jest nieparzysty to zwieksz result razy x%n
        #ogolnie zawsze robimy:
        x **=2  #podnos x do kwadratu
        x %= n # do x przypisz: x = x%n (podobnie jak przy ifie)
        k //= 2 #do k przypisz: podziel k przez 2
    return r

def NWD(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def fermat(p,n=100):
    if p < 2: return False
    if p==2 or p ==3: return True
    if p%2==0: return False
    for i in range(n):
        a = randint(2,p-1) #testowana liczba, wybierzemy ich z 100 
        if gcd(a,p) != 1: return False
        if pow(a,p-1,p) != 1: return False
    return True

#dla n liczb prawdopodobienstwo pomylki:
#1/2 * 1/2 * 1/2 ... = 1/(2^n) - dla n==100:
#1/(2^100) ~ 10^-33 - jak widac baaardzo male
        

if __name__=="__main__":
    pass