from egz3atesty import runtests

def snow( T, I ):
    # tu prosze wpisac wlasna implementacje
    tab =[] #tablica punktów
    for a,b in I:
        tab.append((a,True))
    for a,b in I:
        tab.append((b,False))
    tab.sort(key=lambda x:x[0])
    counter = 0
    maksim = 0
    for point in tab:
        if point[1]:
            counter +=1
        else:
            maksim = max(maksim,counter)
            counter -=1
    maksim = max(maksim,counter)
    
    return maksim

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
