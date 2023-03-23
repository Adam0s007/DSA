# W jednej z chińskich prowincji postanowiono wybudować serię maszyn
# chroniących ludność przed koronawirusem. Prowincję można 
# zobrazować jako tablicę wartości 1 i 0, gdzie arr[i] == 1 
# oznacza, że w mieście i można zbudować maszynę, a wartość 0,
# że nie można. Dana jest również liczba k, która oznacza, że jeśli
# postawimy maszynę w mieście i, to miasta o indeksach j,
# takich, że abs(i-j) < k są przez nią chronione.
# Należy zaproponować algorytm, który stwierdzi ile minimalnie maszyn
# potrzeba aby zapewnić ochronę w każdym mieście, lub -1 jeśli jest to niemożliwe.



#rozwiazanie:
#rzutujemy indeksy z wartosciami == 1 do tablicy indexy
# mamy zmienną startRange oraz i
# na poczatku nasz startRange wynosi 0 co oznacza poczatek naszej tablicy
#bedziemy sprawdzac indexy[i] - startRange < k - gdy pierwszy raz warunek w petli bedzie nieprawdziwy to musimy przejsc do indeksu o 1 mniejszego
# dla ktorego wywolanie jeszcze bylo prawdziwe i go oznaczyc, przy okazji jesli od tego indeksu do ostatniego jest odleglosc mniejsza niz k to juz zwracamy wynik


def covid(T,k):
    indexy = [i for i in range(len(T)) if T[i] == 1]
    startRange= 0 #poczatek range'a znajduje sie z lewej strony
    i = 0
    ans = 0
    verified = {}
    while True:
        while i < len(indexy) and indexy[i] - startRange < k: 
            if len(T)-1 - indexy[i] < k: # jesli jeszcze bedac w petli okaze sie ze inkrementujac nasz licznik bedziemy juz pokrywac koniec tablicy to zwracamy ans + 1
                return ans+1       
            i+=1
        if i == len(indexy): return ans #ten if sie chyba nigdy nie wykona :D
        else: 
            i-=1 #cofamy sie o jeden mniej, szukamy wlasciwego miejsca w tablicy indexy
            if i in verified: return -1 #jesli juz to oznaczylismy kiedys to oznacza ze mamy petle nieskonczoną bo nie mozemy dojsc dalej w tablicy indexes wiec zwracamy -1
            verified[i] = True #zawsze oznaczamy indeksy poprawne 
            ans+=1
            if len(T)-1 - indexy[i] < k:  #dodatkowo sprawdzimy, czy nasz punkt pokrywa juz zakonczenie tablicy, wsm nie wiem czy takie potrzebne
                return ans
            startRange = indexy[i]

             

T = [0,0,1,1,0]
k = 5
print(covid(T,k))