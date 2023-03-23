# Dany jest graf ważony G oraz drzewo rozpinające T 
# zawierające wierzchołek s. Podaj algorytm, który sprawdzi, czy T jest drzewem 
# najkrótszych ścieżek od wierzchołka s.


#rozwiazanie:
#w grafie G mozna zastosowac algorytm bellama Forda, c
# w pierwszym kroku trzeba wszystkie dystanse do wierzcholkow w grafie T
# przepisac i pozamieniac z dystansami w grafie G. 
# teraz robimy relaksacje krawedzi. Jesli okaze sie ze jakas krawedz w G ktora 
# rowniez nalezy do T moze zostac podana relakacji, to nie bedzie drzewo wlasciwe!
# jesli zadna krawedz w drzewie G nalezaca tez do T nie zostanie zrelaksowana, to
# drzewo T jest odpowiednie!



