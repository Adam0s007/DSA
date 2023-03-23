from egzP2atesty import runtests 

def quickSelect(tab,k): #O(n)
    def qSelect(l,r,k):
        pivot,p = tab[r],l
        for i in range(l,r):
            if tab[i][1] >= pivot[1]:
                tab[p],tab[i] =  tab[i],tab[p]
                p+=1

        tab[r],tab[p] = tab[p], tab[r]
        if p > k: return qSelect(l,p-1,k)
        elif p < k: return qSelect(p+1,r,k)
        else: return tab[p]
    return qSelect(0,len(tab)-1,k)


def zdjecie(T, m, k): #pierwsza pozycja do rozpatrywania w quick select'cie: n - k- 1
    newT = [(elem[0],elem[1]) for elem in T]
    n = len(T)
    pos = n - 1 #pozycja poczatkowa (ostatni element)
    punkty = [] # przydadzą się na później

    #szukamy pierwszych pozycji z kazdego rzędu (pierwsza pozycja w kazdym rzedzie to pos+1 natomiast
    #ostatnia pozycja z kazdego rzędu do pos
    '''na poczatku chcemy aby tablica newT byla postaci: [obszar najwiekszych liczb..., mniejsze liczby..., najmniejsze] 
    - takich rzędów ma być m'''
    for i in range(m): # o(m)
        pos -=(k+i) #poniewaz kazdy nastepny rząd jest wiekszy o 1 to k jest zwiekszane w kazdej iteracji o 1 
        punkty.append(pos+1) #tutaj wkladamy pierwsze pozycje z kazdego rzędu!
        if pos < 0: break # ostatnia pozycja wyniesie -1
        quickSelect(newT,pos) #O(n) #wiemy ze element na ostatniej pozycji danego wiersza jest wiekszy
        # w stosunku do wszystkich elementow w wierszu pod nim
    '''teraz chcemy te wszystkie liczby z tablicy newT uporządkować zgodnie z warunkami zadania'''
    punkty.reverse() #nasze punkty zostaly wpisane w malejącej kolejności wiec stosujemy reverse
    x = 0 #bedziemy do oryginalnej tablicy przypisywac na inkrementowanej pozycji x elementy z tablicy newT
    for i in range(k+m-1): #k+m-1 to jest dlugosc najdluzszego wiersza
        for punkt in punkty: 
            if punkt + i < len(newT): #kazdy punkt poczatkowy z kazdego wiersza jest inkrementowany
                T[x] = newT[punkt+i]
                x+=1
                if x == len(newT): break 
        if x == len(newT): break
    
    return T


runtests ( zdjecie, all_tests=True)