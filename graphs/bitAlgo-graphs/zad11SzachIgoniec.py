# Algocja leży na wielkiej pustyni  i składa sie z miast oraz oaz połączonych drogami.
# Kazde miasto jest otoczone murem i ma tylko dwie bramy. Z każdej bramy prowadzi dokładnie 
# jedna droga do jednej oazy (ale do danej oazy może dochodzić dowolnie wiele dróg: 
# oazy mogą też być połączone drogami między sobą). Prawo Algocji wymaga, że jeśli ktoś wjechał do miasta
# jedną bramą, to musi go opuścić drugą. 

# Szach Algocji postanowił wysłać gońca, który w każdym mieście odczyta zakaz formułowania zadań 
# "o szachownicy" ( obraz majestatu). Szach chce, żeby goniec odwiedził każde miasto dokładnie raz 
# (ale nie ma ograniczeń na to ile razy odwiedzi każdą z oaz). Goniec wyjeżdża ze stolicy Algocji, miasta x,
# i  po odwiedzeniu wszystkich miast ma do niej wrócić. 
# Proszę przedstawić algorytm, który stwierdza, czy odpowiednia trasa gońca istnieje. 
# Proszę uzasadnić poprawność algorytmu oraz oszacować jego złożoność czasową.


#rozwiazanie:
#tworzymy cykl Eulera! W ktorym nasze miasta będą krawędziami!
#krawdzie miedzy oazami mogą zostać bo nich mozemy jezdzic wiele razy
#mozna scalic oazy polaczone ze sobą!!!

#najpierw scalamy oazy połączone ze sobą w jedną bfsem!
# potem miasta zamieniamy na krawędzie
# robimy cykl eulera