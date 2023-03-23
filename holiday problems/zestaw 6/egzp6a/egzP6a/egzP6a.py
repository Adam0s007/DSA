from egzP6atesty import runtests 


def zlicz_litery(haslo):
    counter= 0
    for zn in haslo:
        if ord(zn) >= 48 and ord(zn) <=57:
            continue
        counter+=1
    return counter

def compute(pass1,pass2,slowniczek):
    if len(pass1) > len(pass2): return 0 #pierwszy napis silniejszy
    elif len(pass1) < len(pass2): return 1 #drugi napis silniejszy
    else: 
        if pass1 not in slowniczek:
            counter1 = zlicz_litery(pass1)
            slowniczek[pass1] = counter1
        else: counter1 = slowniczek.get(pass1)
        if pass2 not in slowniczek:
            litery_piwota = zlicz_litery(pass2)
            slowniczek[pass2] = litery_piwota
        else: litery_piwota = slowniczek.get(pass2)
        return counter1 < litery_piwota #pierwszy napis silniejszy
        #drugi napis silniejszy
        
def quickSelect(tab,k):
    slowniczek = {} #slowo : ilosc_liter -> slozy spamietaniu niektorych slow, aby dla nich ponownie nie trzeba bylo obliczać ilosci liter
    def qSelect(l,r,k):
        pivot,p = tab[r],l
        for i in range(l,r):
            #if tab[i] <= pivot: # powoduje rosnaca kolejnosc
            if compute(tab[i],pivot,slowniczek):
                tab[i],tab[p] = tab[p],tab[i]
                p+=1
        tab[p],tab[r] = tab[r],tab[p]
        if p > k: return qSelect(l,p-1,k)
        elif p < k: return qSelect(p+1,r,k)
        else: return tab[p]
    return qSelect(0,len(tab)-1,k)

def google ( H, s ):
    return quickSelect(H,len(H)-s)

runtests ( google, all_tests=True)
# T = ['aba', 'abc', 'ab1', 'abab', 'a1a1', 'aa12a']
# google(T,4)