# Dana jest lista zleceń, każde zlecenie wymaga
# pewnego kapitału początkowego C, który należy mieć,
# żeby zacząć zlecenie oraz zysk P, który doda się do
# naszego calkowitego kapitału, gdy wykonamy zlecenie.
# Mając kapitał początkowy W i liczbę k wybierz co 
# najwyżej k zleceń tak, że skończysz z maksymalnym
# możliwym kapitałem. 
# Przykład k = 2, W = 0, P = [1,2,3], C =[0,1,1].
# Rozwiazanie: na początku mamy kapitał 0, więc możemy
# wybrać albo zlecenie 2 albo 3. Zlecenie 3 ma większy profit,
# więc wybieramy zlecenie 3, ponieważ możeby wybrać już 
# tylko 1 zlecenie (k = 2). Kończymy z kapitałem 4.



#rozwiazanie: mając dany stan pieniędzy wybieramy zlecenie z najwiekszym zyskiem P z wymaganiem
# stanu kwoty nie większego od naszego aktualnego

#wystarczy posortować krotke (C[i],P[i]) rosnaco po C[i]. najpierw majac aktualnie W kwoty
# wybieramy stopniowo zlecenia (czyli wkladamy do kolejki priorytetowej) dopoki C[i] tych zlecen jest
# <= od naszego W
# gdy dokonamy wyboru, to wyciagamy z naszej kolejki jedno zlecenie z najlepszym zyskiem
# gdy to zrobimy to mozemy dokonac wkladania do kolejki priorytetowych nowych zlecen, do ktorych teraz
# bedziemy miec juz dostęp. zapamietalismy ostatni indeks ostatniego zlecenia do ktorego juz nie mielismy dostepu
# i od niego idziemy dopoki nie wyjdziemy poza tablicę lub nie znajdziemy innego zbyt wymagajcego zlecenia
# robimy tak dopoki nie przejdziemy calej tablicy lub liczba spelnionych naszych zlecen sie nie wykona.

#czesto przejdziemy przez cala tablice a dalej bedziemy musieli wykonac kilka zlecen, ale ta sytuacja 
# poprostu oznacza, ze mamy dostep do wszystkich zlecen, wiec mozemy wybrac ostatnie k - i - 1 zlecen 
# gdzie i to ostatnia liczba spelnionych zlecen

import heapq

def binary_search(array, searchValue):
    """
    Binary search for the closest value less than or equal to the search value
    :param array: The given sorted list
    :param searchValue: Value to be found in the array
    :param startIndex: Initialized with 0
    :param endIndex: Initialized with 2**32
    :return: Returns the index closest value less than or equal to the search value
    """
    left = 0
    right = len(array)

    while left < right:
        mid = (left + right) // 2

        if array[mid] < searchValue + 1:
            left = mid + 1
        else:
            right = mid

    return left - 1


# T = [3,5,7,8,12,16] 
# print(binary_search(T,8))


def kapital(k,W,P,C):
    kroteczki = [(C[i],P[i]) for i in range(len(P))]
    kroteczki.sort(key=lambda x:x[0])

    q = [] #kolejka priorytetowa
    dodatek = 0
    iter =0
    for i in range(k):
        while iter < len(kroteczki) and kroteczki[iter][0] <= W:
            heapq.heappush(q,-1*kroteczki[iter][1])
            iter+=1
        if not len(q): return "Nie da sie" 
        zysk =  (-1) * heapq.heappop(q)
        W +=zysk
        if iter == len(kroteczki): 
            dodatek = k - i -1 #moze sie zdazyc ze iteratorem przejdziemy przez calą tablicę ale bedzie nam brakowac dodatkowych zleceń do zrobienia
            # bedzie sie tak dzialo gdy nasze W bedzie bardzo duze
            break
    for i in range(dodatek):
        if not len(q): return "Nie da sie" 
        zysk =  (-1) * heapq.heappop(q)
        W +=zysk
    return W
    
    

    



    
k = 2
W = 0
P= [7,5,6,9,8,25,8,8,10,25]
C = [0,0,1,3,2,5,4,2,2,5]


P = [1,2,3]
C = [0,1,1]
print(kapital(k,W,P,C))


        