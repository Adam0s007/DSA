# W problemie tankowania paliwa nasz pojazd musi przemieścić się
# z punktu 0 do punktu F, a po drodze ma stacje tankowania paliwa si,
# przy czym 0 < s1 < s2 < ... < sn < F. Każda stacja jest identyfikowana
# przez jej odległość od punktu 0, tzn. si to odległość pomiędzy
# i-tą stacją a punktem 0. Pojazd potrafi przejechać odległość d
# bez potrzeby tankowania.
# Podaj algorytm, który obliczy, na ilu minimalnie stacjach musi sie
# pojazd zatrzymać na drodze od punktu 0 do pktu F.
# Uwaga: Jeśli zdarzy się, że odległość d jest zbyt mała, żeby dojechać
# do kolejnej stacji, to należy zwrócić wartość None. 


#T = [3,6,12,15,19,21,26] F = 30 d = 5

#rozwiazanie: jedziemy do najdalszej stacji do jakiej mozemy dojechać
def stacje(T,d,F):
    T = [0] + T + [F] # ["0",3,6,12,15,19,21,26,"30"]
    i = 0 #nasza pozycja startowa
    ans = 0
    index = 1 #staramy sie dojechac do stacji kolejnej
    while True: 
        while index < len(T) and T[index] - T[i] <= d: 
            index+=1
        if index == len(T): # a wiec nie trzeba juz zatrzymywać się na zadnej stacji!
            return ans
        elif index-1 != i: #jesli petla wykona sie chociaz raz, to ostatnie wywolanie dla index o 1 mniejszego bedzie prawdziwe!
            ans+=1
            i = index-1 
        elif index -1 == i: return None #brak wyniku!

# T = [3,6,10,12,15,19,21,26] 
# F = 30 
# d = 5
# print(stacje(T,d,F))


T = [3,6,10,12,15,19] 
F = 22 
d = 10
print(stacje(T,d,F))