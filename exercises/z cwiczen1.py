# Składanie dwóch posortowanych list

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def merge(first1, first2):
    if first1 is None:
        return first2
    if first2 is None:
        return first1
    if first1.val > first2.val:
        first1, first2 = first2, first1
    First = first1
    first1 = first1.next
    p = First
    p.next = None
    val1 = first1
    val2 = first2
    while val1 is not None and val2 is not None:
        if val1.val > val2.val:
            first1, first2 = first2, first1
        p.next = first1
        first1 = first1.next
        p = p.next
        p.next = None
    if val1 is None:
        p.next = val2
    elif val2 is None:
        p.next = val1
    return First
#[18:49]
 # MergeSort na seriach naturalnych (na linked listach ze wskaźnikami na pierwszy element w serii)
# 1, 2, 5, 3, 6, 4 ,2, 3, 4, 1, 5
# (1, 2, 5) (3, 6) (4) (2, 3, 4) (1, 5)
#          \/         \/            |
#            \        /             |
#              \    /               |
#                \/                 |
#                 |_________________|
#                         |

def MergeSort(L): #L wskaznik do linked listy
    heads = []
    heads.append(L)
    if L.next is None:
        return L
    curr = L.next
    while curr is not None:
        if curr.val >= L.val:
            L = L.next
            curr = curr.next
        else:
            heads.append(curr.val)
            L.next = None
            L = curr
            curr = curr.next
# Tutaj kompletujemy tablice wskaznikow na poczatek serii naturalnych
    while len(heads) > 1:
        heads2 = []
        while len(heads) > 1:
            merged = merge(heads[0], heads[1])
            heads2.append(merged)
            heads = heads[2]
            heads2.extend(heads)
            heads = heads2
    return heads[0]
#[18:49]
 # Zliczanie wszystkich inwersji (np. dla 1, 3, 2, 7, 5, 6 jest inwersja dla 3 i 2, 7 i 5, 7 i 6), czyli sytuacje gdy wartość na większym indeksie jest mniejsza niz ta na mniejszym)
# MODYFIKACJE DO FUNKCJI MERGE: 
# if L1.val > L2.val:
#   merged.append(L2)
#   inwersje += 1
# else:
#   merged.append(L1)
# Dodajemy licznik inwersji w funkcji merge gdy zmienia się wskaźnik na mniejszą wartosć i zliczamy wtedy inwersję tylko najpierw musimy liste podzielic na serie naturalne albo ogolnie tak jak w MergeSorcie (chyba) niby mozna dowolnie podzielic ale idk co miał na myśli

# Mamy prostokątne pojemniki z woda na płaszczyźnie (mozemy wybobrazać to sobie jako pojemniki w trzech wymiarach gdzie kazdy ma trzeci wymiar jako jedna jednostka), które na siebie nie zachodzą i kazdy z kazdym jest połączony rurami i woda między nimi swobodnie przepływa. Kazdy pojemnik jest zapisany jako współrzędne lewego górnego wierzchoła, szerokość i wysokość. Pojemniki wypełniają sie od dołu i zastanawiamy się jak policzyć jak najwydajniej ile pojemników jest w pełni zalanych. W danych mamy ilość wlanej do układu wody.

#   ____            _______
#  |    |          |       |
#  |____|          |       |
#    |             |_______|
#    |    ___          |
#    |---|   |---------|
#        |   |       __|___
#        |   |------|______|
#        |___|

# Idziemy co 1 zdarzenie (poczatek albo koniec zbiornika) najpierw je sortując (idąc w górę) i trzymamy informacje o aktywnych (zalewanych) zbiornikach oraz o tych juz zalanych az nasza wykorzystana na tej wysokosci objetosc nie osiagnie wartosci większej od nalanej wody (wtedy rozwazamy stan z poprzedniego zdarzenia) lub gdy się zrówna. Gdy znajdziemy poziom wody to zliczamy wszystkie w pelni zalane zbiorniki. Liniowo logarytmiczna zlozonosc

# A - tablica z n liczbami
# Czy istnieje x (lider ciągu) taki, ze wystepuje w A co najmniej n/2 razy. (O(n)!)