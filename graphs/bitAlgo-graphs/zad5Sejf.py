# Dostales sejf, ktory odblokowuje sie czterocyfrowym PINem (000 - 999). 
# Pod wyswietlaczemjest kilka przyciskow z liczbami od 1 - 999 - przykladowo (13,223,782,392).
# Sejf ten działa inaczej niż normalny: wciśnięcie przycisku z liczbą powoduje dodanie liczby z przycisku
# do liczby na wyświetlaczu. Jeżeli suma jest większa niż 999, to pierwsza cyfra zostaje obcięta. 
# Jest tobie znany PIN oraz cyfry, któe są aktualnie wyświetlane. Znajdź najkrótszą sekwencję nacisnięć
# przycisków, któa pozwoli ci odblokować sejf. Jeżeli taka sekwencja nie istnieje, zwróć None.

from queue import SimpleQueue

def obetnij(number):
    number=int(str(number)[1:])
    return number
ans = []
def answer(p):
    added,curSum = p
    ans.append(added)
    p = p[curSum]

def sejf(pin,liczby):
    q = SimpleQueue()
    visited = [False for i in range(999)]
    #inicialization:
    parent = [[-1,0] for i in range(999)]
    
    for x in liczby:
        q.put([x,x]) #[dodana liczba, aktualna suma]
        visited[x] = True
    ans = []
    flag = 0
    while not q.empty() and flag == 0:
        added,actSum = q.get()
        for elem in liczby:
            curr = actSum + elem
            if curr > 999: curr = obetnij(curr)
            if visited[curr]: continue
            visited[curr] = True
            parent[curr][1] = actSum
            parent[curr][0] = added
            if curr == pin:
                added = elem
                while added != -1:
                    ans.append(added)
                    added,curr = parent[curr] 
                flag = 1
                break
            q.put([elem,curr]) 
        if flag == 1: break
    return ans
    
numbers = [13,223,782,392]
pin = 864
print(sejf(pin,numbers))
