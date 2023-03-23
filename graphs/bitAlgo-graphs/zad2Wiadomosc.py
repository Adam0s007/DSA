# Otrzymujemy na wejściu listę par ludzi które się wzajemnie znają.
# Osoby są reprezentowane przez liczby 0 do n-1. 
# Dnia pierwszego osoba 0 przekazuje pewną wiadomość wszystkim swoim
# znajomym . Dnia drugiego każdy ze znajomych przekazuje tę wiadomość
# wszystkim swoim znajomym, którzy jej jeszcze nie znali, i tak dalej.

# Napisz algorytm, który zwróci dzień, w którym najwięcej osób poznało wiadomość 
# oraz ilość osób, które tego dnia ją otrzymały.


#Rozwiązanie: najzwyklejszy w świecie BFS z tablicą distance, wierzcholek 0 to osoba 0 i od niej liczymy distance - dni i zwrocimy 
# distanse, przy ktorym najwiecej osob dostalo wiadomosc!