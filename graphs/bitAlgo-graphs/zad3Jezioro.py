# Dana jest dwuwymiarowa tablica N x N, w ktorej każda komórka 
# ma wartość "W" - reprezentującą wodę lub "L" - ląd.
# Grupa komórek wody połączonych ze sobą brzegami nazywamy jeziorem.

# a) policz ile jezior jest w tablicy 
# b) Policz, ile komórek zawiera największe jezioro.

#a) i b) znajde rozwiazanie w folderze neetCode zad4 i zad6


# c) zakladajac, że pola o indeksach [0][0] i [n-1][n-1] są lądem,
# sprawdź czy da się przejsć drogą lądową z pola [0][0] do pola[n-1][n-1].
# Można chodzićtylko na boki, nie na ukos. 

# d) znajdź najkrótszą ścieżkę między tymi punktami. 
# Wypisz po kolei indeksy pól w tej ścieżce.

#do c) i d) stosujemy bfsa, bo on od razu zwróci tą najkrószą ścieżkę
