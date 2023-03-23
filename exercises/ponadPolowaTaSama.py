#Mamy dana tablice A z liczbami naturalnymi. Zaproponuj algorytm o zlozonosci O(n), ktory stwierdza, czy w tablicy ponad polowa
#elementow ma jednakową wartość.

def leading_number(arr):
    leader = arr[0]
    k = 1
    for i in range(1,len(arr)):
        if leader == arr[i]: k+=1
        else:
            k-=1
            if k == 0:
                leader = arr[i]
                k = 1 #always set k to 1 with initialization new value for p
    #cheacking leader:
    c = 0
    print(leader)
    for i in range(len(arr)):
        if leader == arr[i]: c+=1
        if c > len(arr)//2: return True
    return False
tab = [6,1,6,1,6,1,6,1,6]

print(leading_number(tab))