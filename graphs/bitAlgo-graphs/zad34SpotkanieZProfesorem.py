# Pewien znany profesor zaprosił cię na spotkanie w Magicznym Mieście. W mieście tym niektóre 
# drogi mogą być uczęszczane tylko przez ludzi poniżej 30 roku życia (w tym Ciebie), inne tylko 
# przez ludzi w wieku od 30 lat ( w tym profesora). Są też drogi, które mogą być uczęszczane
# przez każdego. Każda z dróg ma określoną długość, wyrażoną dodatnią liczbą naturalną, może być 
# jedno lub dwukierunkowa.
# Drogi te łączą możliwe lokalizacje spotkania. Wśród nich wyróżniamy mieszkanie Twoje i mieszkanie profesora.
# Profesor prosi Cię, być wybrał takie miejsce na spotkanie, aby łączna droga, którą musicie pokonać 
# Ty i profesor była jak najmniejsza. Jeżeli jest więcej niż jedno takie miejsce, podaj je wszystkie. 
# Jeżeli takie miejsce nie istnieje, algorytm również powinien to stwierdzić.


#rozwiazanie:
#robimy dwie dijkstry: najpierw od domu profesora, a potem od domu studenta
# potem dla kazdego wierzcholka sprawdzamy distProf (dystans od profesorka) oraz distStudent ( dystans od studenta)
# sumujemy je dla kazdego wierzcholka i wybieramy minimum