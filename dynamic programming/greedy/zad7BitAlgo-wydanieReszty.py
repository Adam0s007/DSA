# W problemie coin change mamy daną kwotę X i chcemy ją rozmienić
# na monety o wartości 1,5,10,25 i 100. Podaj algorytm, który 
# obliczy, ile minimalnie monet trzeba użyć do wydania reszty oraz
# ile sztuk każdej monety będzie trzeba użyć.

# Można założyć, że każdej monety mamy nieskończenie wiele sztuk.

# Czy algorytm zachłanny zadziała dla zestawu monet 1,2,7,10? Jeśli tak,
# uzasadnij dlaczego. Jeśli nie, podaj kontrprzykład.



#rozwiazanie: posortuj liczby malejaco. Bierz najwieksze liczby poki da sie i stopniowo je zmniejszaj
#przyklad: X = 96,: 3 razy 25 = 75, potem dwa razy 10 => 95  i + 1 => 96
# w sumie: 3 + 2 + 1 = 6 monet

# X = 96: 9 * 10 + 3* 2  => daje w sumie 12 monet  kontrprzyklad: 8*10 + 2*7 + 1*2 => daje w sumie 11 monet


#dlaczego wiec nasz algorytm dziala? 
# mamy wielokrotnosci liczby 5 (poza 1)
# 10 = 2 * 5 - maly konener dla 5
# 25 = 5 * 5 - sredni kontener dla 5
# 100 = 10 * 5 - jesli da sie upakować w liczbie 100 (ktora zawiera w sobie najwiecej 5) to robimy to
#              jesli juz nie damy rady upakowac w liczbe "kontenera" majacego najwiecej 5, to sprobujmy
#             upakowac mniejszy kontener zawierajacy tylko 5 piątek.
#              jak sie nie da to sprawdzamy dla jeszcze mniejszego (majacego 2 piątki)
#             jesli nie jestesmy juz upakowac wiecej 5 to juz dzialamy na 1

# dla liczb 1,2,7,10 mamy zawartą liczbę pierwszą 7, ktora ni jak nie dzieli sie przez 5 ani przez 2 wiec nie moze
# byc naszym kontenerem dla wybranej liczby z zestawu!


#zwraca krotke: (ilosc_danej_monety,dana_moneta)
#warunek zadzialania: kazda moneta musi być co najmniej 2 razy większa od poprzedniej!
def rozmien5(X): # musimy zasugerowac ze dziala tylko dla "kontenerow" zawierających wielokrotnosci danej liczby: np 1,2,4,16 itd.
    T = [100,25,10,5,1]
    ans = []
    for coin in T:
        mnoznik = 1
        while X - mnoznik*coin > 0:
            mnoznik +=1
        if X - mnoznik*coin == 0:   # to kiedys zawsze zajdzie bo mamy 1 !!
            ans.append((mnoznik,coin))
            return ans
        elif X - mnoznik*coin < 0 and mnoznik - 1 != 0:
            ans.append((mnoznik-1,coin))
            X -= ((mnoznik-1)*coin)

X = 97
print(rozmien5(X))
        

