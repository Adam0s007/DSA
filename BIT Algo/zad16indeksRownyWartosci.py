# Dana jest posortowana rosnąco tablica A wielkości n zawierająca 
# parami różne liczby naturalne. Podaj algorytm, który sprawdzi, czy jest taki indeks i, że
# A[i] == i.
# Co zmieni się, jeżeli liczby będą po prostu całkowite, niekoniecznie naturalne?


#dla liczb naturalnych problem banalnie prosty bo sprawdzamy w O(1) tylko 1. indeks z elementem! ( tablica rosnaca a nie niemalejaca!!!)
#[1,2,3,4,5,6,7,8] - nie mozliwe!
#[0,2,5,6,7,8,9] - T[0] == 0!!

#dla liczb calkowitych:
#BS
def same_ind_val(arr):
    l,r =0, len(arr)-1
    while l <=r:
        mid = (l+r)//2
        if arr[mid] == mid: return True
        if mid > arr[mid]:
            l = mid+1
        else:
            r = mid-1
    return False

t = [-10,-9,-8,3,5,8]
print(same_ind_val(t))
        