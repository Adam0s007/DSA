from zad5testy import runtests
#Adam Biśta
#mamy dwie zmienne: prev_ind oraz maks_ind. poczatkowo ustawiamy sobie prev_ind na 1 oraz maks_ind na wartosc w T[0].
# maks_ind informuje nas, jak daleko jestesmy w stanie sie przemiesic (maksymalny indeks do ktorego mozemy przejsc), natomiast prev_ind przechowuje poprzedni maks_ind. 
#algorytm działa tak, że mamy dwie petle: w zewnetrznej istnieje warunek, ze poki maks_ind jest mniejszy od indeksu ostatniego w tablicy, wykonuj instrukcje.
#zadaniem drugiej petli jest wlozenie do kolejki priorytetowej wartosci z tablicy T[i] od prev_ind+1 do maks_ind wlacznie
# priorytetem w kolejce jest maksymalna wartosc T[i], druga zmienna w krotce informuje o indeksie i.
# zamiast cofania sie na pozycję i poprostu do aktualnego maks_ind dodajemy maksymalną aktualną wartość z kolejki priorytetowej,
# dzięki czemu symulujemy maksymalne przemieszczanie sie do przodu. Uwaga! Do kolejki wsadzamy tylko wartosci, ktore mają sens - nie wsadzamy wartosci zerowych, 
# poniewaz nigdy nie spowodują przemieszczenia.

#memory complexity O(k), k - maksymalna dlugosc kolejki priorytetowej ( jesli jest stosunkowo mala to O(1))
# time complexity: O(nlogk) gdzie n - dlugosc tablicy T, a k - dlugosc kolejki priorytetowej 
# from queue import PriorityQueue
import heapq
def plan(T):
    #heap = PriorityQueue()
    heap = []
    maks_ind = T[0]
    ans = [0]
    prev_ind = 0
    while maks_ind < len(T)-1:
        for i in range(prev_ind+1, maks_ind+1):
            if T[i]: heapq.heappush(heap,(-1*T[i],i))
        elem = heapq.heappop(heap)
        ans.append(elem[1])
        prev_ind = maks_ind       
        maks_ind += -1*elem[0]
    return sorted(ans)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )