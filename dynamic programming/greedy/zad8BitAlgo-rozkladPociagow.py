# Mamy dany pewien rozkład pociągów, dany jako tablica n krotek
# (arrival_time, departure_time), przy czym są one posortowane niemalejąco 
# według arrival_time. Chcemy wiedzieć, czy nasza stacja mająca m peronów 
# jest w stanie bezkonfliktowo obsłużyć te pociągi, tzn. w żadnym momencie 
# nie będzie "rywalizacji " pociągów o dostępne perony.
# Przedstaw algorytm, który poda odpowiedź True lub False na powyższe pytanie

#przyklad:
# m = 3
# [(0,2),(0,4),(0,1),(1,3),(2,4)]


#robimy kolejke priorytetową
#do niej wsadzamy rozklady (rozmiescimy je na m peronow)
# bedzie to heap typu min ze względu na departure time
import heapq
def timetable(T,m):
    q = []
    
    right = T[0][1] #najpierw dodajemy pierwszy pociag na jeden jakis peron (dodanie na peron - dodanie do heapa)
                                                                        # ( usuniecie z peronu - usuniecie z heapa)
    heapq.heappush(q,right)                                            # (ilosc zajetych peronow - dlugosc heapa)
    for arrival,departure in T[1:]:
        
        earliest_departue = q[0] #musimy podpatrzec jaka godzina jest na najwczesniej wyjezdzajacym pociagu, nie wydobywamy na razie z heapa
        if arrival < earliest_departue and len(q) == m: return False
        elif  arrival < earliest_departue: #jesli godzina najwczesniejszego wyjazdu jakiegos pociagu pokrywa sie z przyjazdem nowego to dodajemy na kolejny peron pociag
            heapq.heappush(q,departure)
        else:
            while len(q) and q[0] < arrival: # jesli czas naszego przyjazdu jest duzy, to usuwamy z peronow pociagi dopoki nie pozostanie taki, ktorego dep_time > nowy_arrival
                heapq.heappop(q) # jesli nasz nowy arrival time jest wiekszy lub rowny najwczesniejszemu departure time'owi
                            #to pozbywamy sie ostatniego departure time'a, oraz inne ktore maja mniejszy czas i umieszczamy nowy
            heapq.heappush(q,departure)

    return True


T = [(0,1),(0,3),(0,2),(1,3),(2,4),(3,5),(4,5),(5,7),(8,10)]
m = 3
print(timetable(T,m))

        
