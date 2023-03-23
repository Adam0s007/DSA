# Oprócz długości krawędzi graf ma przypisane koszty wierzchołków.
# Zdefiniujmy koszt ścieżki jako sumę kosztów jej krawędzi oraz sumę kosztów
# wierzchołków (wraz z końcami!). 

# Jak znaleźć najtańsze ścieżki między wierzchołkiem startowym a wszystkimi pozostałymi?

# Podaj rozwiązanie zarówno dla grafu skierowanego, jak i nieskierowanego.


#rozwiazanie:
#1) robimy dijkstre ale dodatkowo w relaxacji wliczamy wage wierzcholka
# koncowego, lub z ktorego wyszlismy (dla grafu skierowanego)

#2) dla grafu nieskierowanego krawedzie miedzy wierzcholkami traktujemy jako dwie
# w jedną stronę i w drugą stronę - to co w 1) punkcie