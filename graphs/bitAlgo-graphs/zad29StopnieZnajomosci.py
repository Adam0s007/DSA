# Definiujemy relację znajomości między osobami jako symetryczną.
# Znajomość:
#  - pierwszego stopnia to bezpośrednia znajomość osoby 
#  - drugiego stopnia to bycia "znajomym znajomego" osoby, ale nie 
#  bezpośrednim znajomym osoby.
#  - trzeciego,czwartego,piątego stopnia itd.
#  - nieskonczonego stopnia zachodzi wtedy gdy nie ma ciagu znajomosci, ktory laczylby
#  dwie osoby.

# Majac na wejsciu listę osób i znajomości pierwszego stopnia między nimi, 
# chcemy znalezc najwiekszy stopien znajomosci wsrod kazdej z mozliwych par.
# Znajdz optymalne rozwiazanie zarówno dla grafow rzadkich (|E| -- O(|V|)),
# jak i gęstych (|E| == O(|V|^2))


#tutaj nie szukamy srednicy bo to nie jest drzewo!

#rozwiazanie:
#1) dla grafow rzadkich:
# zrobic bfs z kazdego wierzcholka Bfs: V * O(V+E) = O(V*V) = O(V^2)

#2) dla grafow gestych: najlepiej Floyda Warshalla! bedzie w O(V^3), i mnialoby najmniejszą stałą.
# wieksza stałą by mial bfs z kazdego wierzcholka bo: V * O(V+E) = V *O(V + V^2) = O(V^3)

#trzeba tez sprawdzic czy graf jest spojny