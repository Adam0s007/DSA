# W Krakowie w godzinach szczytu są korki, dlatego kierowcom bardziej zależy na czasie 
# niż na realnej odległości między dwoma punktami. Mamy mapę Krakowa, między
# skrzyżowaniami na ulicach są zaznaczone odległości i czasy przejazdu.
# W Krakowie (jak wszyscy wiemy ;)) są ulice jedno i dwukierunkowe.
# Kierowcy potrzebują aplikacji, która pomoże im znajdować drogi, które pozwalają dotrzeć 
# ze skrzyżowania A do B w jak najkrótszym czasie, a spośród tych o najmniejszym czasie 
# wybiera i zwraca najkrótszą pod względem odległości.

# Mamy przetworzyć Q zapytań w postaci (skrzyżowanieA, skrzyżowanieB) 
# i na każde z nich odpowiedzieć parą (czas,dystans) najlepszej drogi.
# Wszystkie zapytania odnoszą się do tego samego grafu. 

#jakie rozwiązanie daje najlepszą klasę złożoności w każdym z poniższych przypadków?
# Q = O(1), E = O(V) 
# Q = O(1), E = O(V^2)
# Q = O(V), E = O(V)
# Q = O(V), E = O(V^2)

#analogia do zadania o ścieżkach super fajnych zad 18
#rozw:
# Q = O(1), E = O(V)   - stosujemy dijkstre zmodyfikowana (to juz robilem w sciezkach superfajnych): O(VlogV)
# Q = O(1), E = O(V^2) - jak wyzej: ale zlozonosc bedzie: O(V^2logV) dla reprezentacji listowej, ale dla macierzowej bedzie stale rowne O(V^2)!!!!
# Q = O(V), E = O(V)   - jak wyzej: O(V^2logV)
# Q = O(V), E = O(V^2) -  Floyd Warshall O(V^3)