#Dana jest posortowana tablica T i liczba x
#znajdz i oraz j ktore: T[j] + T[i] = x

def liczba_x(T,x):
    wsk2 = len(T)-1
    wsk1 = 0
    while wsk1 < wsk2:
        if T[wsk1] + T[wsk2] < x:
            wsk1+=1
        elif T[wsk1] + T[wsk2] > x:
            wsk2-=1
        else:
            return wsk1,wsk2
    else:
        return None,None
T = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(liczba_x(T,11))