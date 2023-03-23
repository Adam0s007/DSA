# W miasteczku są sklepy i domy. Trzeba sprawdzić jak daleko do najbliższego sklepu mają mieszkańcy.
# struct Vertex {
#     bool shop;
#     int* distances; // tablic odleglosci do innych wierzcholkow
#     int* edges; // numery wierzcholkow opisanych w distances;
#     int edge; // rozmiar tablicy distances (i edges)
#     int d_store; // odleglosc do najblizszego sklepu
# }
# Zaimplementować funkcję distanceToClosestStore(int n, Vertex* village) 
# uzupełniającą d_store dla tablicy Vertexów i oszacować złożoność algorytmu

#rozwiazanie: puscic jeden algorytm dijkstry, wlozyc
# wszystkie sklepy do kolejki z ich distance[si] = 0 (gdzie i to ity sklep) pozniej relaxacja sprawi, ze odpowiednie
# pola sie zaaktualizują dla wybranych domów.

#wrzucic od razu wszystkie sklepy do kolejki priorytetowej i to tyle jesli chodzi o zmiany  w zwyklym algo dijkstry