# Dany jest zbiór N prostokątów o bokach równoległych do osi ukladu współrzędnych.
# Proszę zaimplementować funkcję:
#  def rect(D): 
#     ...
# która wskaże, który prostoką należy usunąć tak, żeby przecięcie pozostałych
# miało jak największe pole. Każdy prostoką opisuje czwórka liczb całkowitych
# (x1,y1,x2,y2) określających współrzędne lewego dolnego i prawego górnego rogu prostokąta.
# Funkcja otrzymuje listę takich czwórek i powinna zwrócić najmniejszy numer 
# prostokąta, który należy usunąć.

# 1. próg: O(NlogN)
# 2. próg: O(N)

#rozwiazanie O(N): 
# 1. wyznaczamy najbardziej wysuniety na prawo prostokąt, wyznaczamy przeciecie prostokątów bez tego jednego.
#2. robimy to samo dla wszystkich pozostałych 3 kierunków ( lewa, dolu, góry) maksymalne przecięcie aktualizujemy jesli sie zmieni


#drugie rozwiazanie O(N):
#L[i] - cz wspolna wszystkich prostokatow od 0 do i-1
#P[i] - cz wspolna wszystkich prostokątow od i do n-1

#jak to zrobic by nam sie nie kwadratowilo?
# L[i] = L[i-1] oraz przeciecie prostokata i {operacja O(1)} 
# P[i] = P[i+1] oraz przeciecie prostokąta i {operacja O(i)}

#potem liniowo idziemy przez obydwie tablice od [0, n-1] 
# i liczymy w O(1) przeciecie L[i] i P[i] 