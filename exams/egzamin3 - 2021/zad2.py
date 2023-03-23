from zad2testy import runtests
#1. prog: O(dnlogn), gdzie n to liczba sekwencji zas d to dlugosc pojedynczej sekwencji
#2. prog O(D) to sumaryczna dlugosc wszystkich sekwencji 

#Dana jest lista L parami roznych napisow skladajacych sie z symboli 0 i 1. Mowimy, ze pewien 
#napis a jest fajny, jesli jest prefiksem co najmniej dwoch napisow z L(przy czym jesli w L znajduje sie
# napis identyczny z a, to napis a wciaz traktujemy jako jego prefix). Dalej mowimy, ze napis a jest 
# bardzo fajny jesli jest fajny i zarazem zadne jego rozszerzenie (poprzez dodanie dowolnego symbolu na koncu)
# nie jest napisem fajnym. 
#zaproponuj i uzasadnij poprawnosc i zaimplementuj algorytm, ktory otrzymuje liste napisow z L (skladajacych sie z 0 i 1)
#i zwraca wszystkie bardzo fajne napisy dla tej listy.

#L to tablica zawierajaca wejsciowe napisy ( jako napisy w jezyku pythona). Funkcja powinna zwrocic listę prefiksów
#spelniajacych warunki zadania (rowniej jako liste napisow w jezyku Pythona). Mozna zwrocic w dowolnej kolejnosci.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.counter = 0
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True #ending point
        cur.counter +=1 #zwiekszamy counter
    
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return 0,None
            cur = cur.children[c]
        
        if cur.endOfWord: 
            return cur.counter,word #zwracamy dany prefix oraz ilosc wystapien!
        return 0,None
          
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

#nawet na egzaminie bez mozliwosci korzystania z wbudowanego slownika przydaloby sie do rozwiazania zadania
# zaimplementować taki słownik, z dobrą funkcją hashującą. 
#korzystając ze struktury TieTree musielibysmy dodatkowo przechodzic liniowo przez node'y, korzystajac tylko ze slownikow
# w O(1) mamy dostęp do danych napisow.
def double_prefix( L ):
    """tu prosze wpisac wlasna implementacje"""
    slowniczek = {} 
    for word in L:
        for i in range(1,len(word)+1):
            prefix = word[:i]
            slowniczek[prefix] = slowniczek.get(prefix,0) + 1 #dict.get(key,default=value)
                                                             # dict[key] = [value1,value2,...]
                                                             #.get ==> dict[key].append(costam)
    ans = []

    for prefix,counter in slowniczek.items(): # for keys in slownik.keys() , for values in slownik.values()
        if counter >= 2: #prefix - fajny
            if (prefix + "0" not in slowniczek and prefix + '1' not in slowniczek):
                ans.append(prefix)
            elif (prefix + "0" in slowniczek and prefix + '1' in slowniczek):
                if slowniczek.get(prefix + "0") < 2 and slowniczek.get(prefix + "1") < 2:
                   ans.append(prefix)
            #teraz wiemy ze jednego nie ma w slowniku!
            elif (prefix + "0" in slowniczek and slowniczek.get(prefix + "0") < 2) or (prefix + "1" in slowniczek and slowniczek.get(prefix + "1") < 2):
                ans.append(prefix)
    return ans



runtests( double_prefix )

