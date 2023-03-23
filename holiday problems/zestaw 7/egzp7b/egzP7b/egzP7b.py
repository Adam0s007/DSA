from egzP7btesty import runtests 
	

#poprostu musimy znalezc taki przedzial w ktorym wszystkie powtorzone wartosci nie są wliczane
#O(n^2)


#w rozwiazaniu O(nlogn) mamy pointera idącego do poczatku tablicy do konca
# za kazdym przejsciu pointerem zmienia sie aktualna suma
#kazda liczba wskazuje na następną w tablicy taką samą a ta na kolejną taką samą

# aby rozwiazanie dzialalo w nlogn trzeba zastosowac drzewo przedzialowe
def ogrod( S, V ):
    NOPICKED = 0
    PICKED= 1
    OVERPICKED = 2
    m = len(V)
    n = len(S)
    for i in range(len(S)):
        S[i] -=1

    output = 0
    for i in range(n):
        is_taken = [NOPICKED for _ in range(m)]
        temp_output = 0
        for j in range(i,n):
            if is_taken[S[j]] == NOPICKED:
                temp_output += V[S[j]]
                is_taken[S[j]] = PICKED

            elif is_taken[S[j]] == PICKED:
                output = max(output,temp_output)
                temp_output -= V[S[j]]
                is_taken[S[j]] = OVERPICKED
        
        output = max(output,temp_output)

    return output
    
runtests(ogrod, all_tests = True)